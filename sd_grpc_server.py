import json
import os
import sys
import time
import importlib
import signal
import re
from packaging import version

import logging
logging.getLogger("xformers").addFilter(lambda record: 'A matching Triton is not available' not in record.getMessage())

from modules import errors, extra_networks, ui_extra_networks_checkpoints
from modules import extra_networks_hypernet, ui_extra_networks_hypernets, ui_extra_networks_textual_inversion
from modules.call_queue import wrap_queued_call, queue_lock, wrap_gradio_gpu_call

import torch
import base64
from io import BytesIO
from PIL import Image
# Truncate version number of nightly/local build of PyTorch to not cause exceptions with CodeFormer or Safetensors
if ".dev" in torch.__version__ or "+git" in torch.__version__:
    torch.__long_version__ = torch.__version__
    torch.__version__ = re.search(r'[\d.]+[\d]', torch.__version__).group(0)

from modules import shared, devices, sd_samplers, upscaler, extensions, localization, ui_tempdir, ui_extra_networks
import modules.codeformer_model as codeformer
import modules.face_restoration
import modules.gfpgan_model as gfpgan
import modules.img2img

import modules.lowvram
import modules.paths
import modules.scripts
import modules.sd_hijack
import modules.sd_models
import modules.sd_vae
import modules.txt2img
import modules.script_callbacks
import modules.textual_inversion.textual_inversion
import modules.progress

import modules.ui
from modules import modelloader
from modules.shared import cmd_opts
import modules.hypernetworks.hypernetwork

if cmd_opts.server_name:
    server_name = cmd_opts.server_name
else:
    server_name = "0.0.0.0" if cmd_opts.listen else None
from modules.api.simple_api import SimpleApi, StableDiffusionTxt2ImgProcessingAPI, StableDiffusionImg2ImgProcessingAPI
from modules.processing import StableDiffusionProcessingTxt2Img, StableDiffusionProcessingImg2Img
def check_versions():
    if shared.cmd_opts.skip_version_check:
        return

    expected_torch_version = "1.13.1"

    if version.parse(torch.__version__) < version.parse(expected_torch_version):
        errors.print_error_explanation(f"""
You are running torch {torch.__version__}.
The program is tested to work with torch {expected_torch_version}.
To reinstall the desired version, run with commandline flag --reinstall-torch.
Beware that this will cause a lot of large files to be downloaded, as well as
there are reports of issues with training tab on the latest version.

Use --skip-version-check commandline argument to disable this check.
        """.strip())

    expected_xformers_version = "0.0.16rc425"
    if shared.xformers_available:
        import xformers

        if version.parse(xformers.__version__) < version.parse(expected_xformers_version):
            errors.print_error_explanation(f"""
You are running xformers {xformers.__version__}.
The program is tested to work with xformers {expected_xformers_version}.
To reinstall the desired version, run with commandline flag --reinstall-xformers.

Use --skip-version-check commandline argument to disable this check.
            """.strip())


def initialize():
    check_versions()

    extensions.list_extensions()
    localization.list_localizations(cmd_opts.localizations_dir)

    if cmd_opts.ui_debug_mode:
        shared.sd_upscalers = upscaler.UpscalerLanczos().scalers
        modules.scripts.load_scripts()
        return

    modelloader.cleanup_models()
    modules.sd_models.setup_model()
    codeformer.setup_model(cmd_opts.codeformer_models_path)
    gfpgan.setup_model(cmd_opts.gfpgan_models_path)

    modelloader.list_builtin_upscalers()
    modules.scripts.load_scripts()
    modelloader.load_upscalers()

    modules.sd_vae.refresh_vae_list()

    modules.textual_inversion.textual_inversion.list_textual_inversion_templates()

    try:
        modules.sd_models.load_model()
    except Exception as e:
        errors.display(e, "loading stable diffusion model")
        print("", file=sys.stderr)
        print("Stable diffusion model failed to load, exiting", file=sys.stderr)
        exit(1)

    shared.opts.data["sd_model_checkpoint"] = shared.sd_model.sd_checkpoint_info.title

    shared.opts.onchange("sd_model_checkpoint", wrap_queued_call(lambda: modules.sd_models.reload_model_weights()))
    shared.opts.onchange("sd_vae", wrap_queued_call(lambda: modules.sd_vae.reload_vae_weights()), call=False)
    shared.opts.onchange("sd_vae_as_default", wrap_queued_call(lambda: modules.sd_vae.reload_vae_weights()), call=False)
    shared.opts.onchange("temp_dir", ui_tempdir.on_tmpdir_changed)

    shared.reload_hypernetworks()

    ui_extra_networks.intialize()
    ui_extra_networks.register_page(ui_extra_networks_textual_inversion.ExtraNetworksPageTextualInversion())
    ui_extra_networks.register_page(ui_extra_networks_hypernets.ExtraNetworksPageHypernetworks())
    ui_extra_networks.register_page(ui_extra_networks_checkpoints.ExtraNetworksPageCheckpoints())

    extra_networks.initialize()
    extra_networks.register_extra_network(extra_networks_hypernet.ExtraNetworkHypernet())

    if cmd_opts.tls_keyfile is not None and cmd_opts.tls_keyfile is not None:

        try:
            if not os.path.exists(cmd_opts.tls_keyfile):
                print("Invalid path to TLS keyfile given")
            if not os.path.exists(cmd_opts.tls_certfile):
                print(f"Invalid path to TLS certfile: '{cmd_opts.tls_certfile}'")
        except TypeError:
            cmd_opts.tls_keyfile = cmd_opts.tls_certfile = None
            print("TLS setup invalid, running webui without TLS")
        else:
            print("Running with TLS")

    # make the program just exit at ctrl+c without waiting for anything
    def sigint_handler(sig, frame):
        print(f'Interrupted with signal {sig} in {frame}')
        os._exit(0)

    signal.signal(signal.SIGINT, sigint_handler)

def base64_to_image(base64_str):  # 用 b.show()可以展示
    image = base64.b64decode(base64_str, altchars=None, validate=False)
    image = BytesIO(image)
    image = Image.open(image)
    return image

class SDhandler:
    def __init__(self):
        initialize()
        self.api = SimpleApi(queue_lock)

    def run_text2img(self,
                    prompt: str = "",
                    negative_prompt: str = None,
                    width: int = 512,
                    height: int = 512,
                    seed: int = -1,
                    steps: int = 50,
                    batch_size: int = 1,
                    **kwargs):
        txt2imgreq = StableDiffusionTxt2ImgProcessingAPI(prompt=prompt, negative_prompt=negative_prompt,width=width, height=height, seed=seed, steps=steps, batch_size=batch_size, **kwargs)

        try:
            response = self.api.text2imgapi(txt2imgreq)
        except Exception as e:
            raise e
        return response.images
        # for i, img_base64 in enumerate(response.images):
        #     save_path_img = os.path.join(save_path, f"{i}.jpg")
        #     img_pil = base64_to_image(img_base64)
        #     img_pil.save(save_path_img)

    def run_img2img(self,
                    base64_images : list,
                    mask: str = None,
                    prompt: str = "",
                    negative_prompt: str = None,
                    width: int = 512,
                    height: int = 512,
                    seed: int = -1,
                    steps: int = 50,
                    batch_size: int = 1,
                    **kwargs):
        init_images = []
        for base64_image in base64_images:
            init_images.append(base64_to_image(base64_image))
        # in_mask = base64_to_image(mask)
        img2imgreq = StableDiffusionImg2ImgProcessingAPI(init_images=init_images,
                                                         mask=mask,
                                                         prompt=prompt,
                                                         negative_prompt=negative_prompt,
                                                         width=width,
                                                         height=height,
                                                         seed=seed,
                                                         steps=steps,
                                                         batch_size=batch_size, **kwargs)
        try:
            response = self.api.img2imgapi(img2imgreq)
        except Exception as e:
            raise e
        return response.images

import grpc
from proto import sd_pb2, sd_pb2_grpc
from concurrent import futures

class SDService(sd_pb2_grpc.SdServiceServicer):
    '''
    继承GrpcServiceServicer,实现hello方法
    '''
    def __init__(self):
        self.sd_handler = SDhandler()

    def text2img(self, request, context):
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width
        height = request.height
        seed = request.seed
        steps = request.steps
        batch_size = request.batch_size

        imgs_base64 = self.sd_handler.run_text2img(prompt, negative_prompt, width, height, seed, steps, batch_size)
        return sd_pb2.SdText2ImgResponse(base64=imgs_base64)
    
    def img2img(self, request, context):
        base64_images = request.base64_images
        mask = request.mask
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width
        height = request.height
        seed = request.seed
        steps = request.steps
        batch_size = request.batch_size

        imgs_base64 = self.sd_handler.run_img2img(base64_images, mask, prompt, negative_prompt, width, height, seed, steps, batch_size)
        return sd_pb2.SdImg2ImgResponse(base64=imgs_base64)

def run():
    '''
    模拟服务启动
    :return:
    '''
    MAX_MESSAGE_LENGTH = 256 * 1024 * 1024
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=[
                ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
    sd_pb2_grpc.add_SdServiceServicer_to_server(SDService(),server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("start service...")
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run()