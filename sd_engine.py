from __future__ import annotations

import os
import sys
import time
import importlib
import signal
import re
import warnings
import json
from threading import Thread
from typing import Iterable
import torch
import base64
from io import BytesIO
from PIL import Image
from packaging import version
import numpy as np
import logging
import cv2
from enum import Enum

# We can't use cmd_opts for this because it will not have been initialized at this point.
log_level = os.environ.get("SD_WEBUI_LOG_LEVEL")
if log_level:
    log_level = getattr(logging, log_level.upper(), None) or logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

logging.getLogger("torch.distributed.nn").setLevel(logging.ERROR)  # sshh...
logging.getLogger("xformers").addFilter(lambda record: 'A matching Triton is not available' not in record.getMessage())

from modules import timer
startup_timer = timer.startup_timer
startup_timer.record("launcher")

import torch
import pytorch_lightning   # noqa: F401 # pytorch_lightning should be imported after torch, but it re-enables warnings on import so import once to disable them
warnings.filterwarnings(action="ignore", category=DeprecationWarning, module="pytorch_lightning")
warnings.filterwarnings(action="ignore", category=UserWarning, module="torchvision")
startup_timer.record("import torch")

import gradio  # noqa: F401
startup_timer.record("import gradio")

from modules import paths, timer, import_hook, errors, devices  # noqa: F401
startup_timer.record("setup paths")

startup_timer.record("import ldm")

from modules import extra_networks
from modules.call_queue import wrap_gradio_gpu_call, wrap_queued_call, queue_lock  # noqa: F401

# Truncate version number of nightly/local build of PyTorch to not cause exceptions with CodeFormer or Safetensors
if ".dev" in torch.__version__ or "+git" in torch.__version__:
    torch.__long_version__ = torch.__version__
    torch.__version__ = re.search(r'[\d.]+[\d]', torch.__version__).group(0)

from modules import shared, sd_samplers, upscaler, extensions, localization, ui_tempdir, ui_extra_networks, config_states
import modules.codeformer_model as codeformer
import modules.face_restoration
import modules.gfpgan_model as gfpgan
import modules.img2img

import modules.lowvram
import modules.scripts
import modules.sd_hijack
import modules.sd_hijack_optimizations
import modules.sd_models
import modules.sd_vae
import modules.sd_unet
import modules.txt2img
import modules.script_callbacks
import modules.textual_inversion.textual_inversion
import modules.progress

import modules.ui
from modules import modelloader
from modules.shared import cmd_opts
import modules.hypernetworks.hypernetwork
from modules.api.simple_api import SimpleApi, decode_base64_to_image
from modules.api.models import  StableDiffusionTxt2ImgProcessingAPI, StableDiffusionImg2ImgProcessingAPI, ExtrasSingleImageRequest
from modules.processing import StableDiffusionProcessingTxt2Img, StableDiffusionProcessingImg2Img

startup_timer.record("other imports")


if cmd_opts.server_name:
    server_name = cmd_opts.server_name
else:
    server_name = "0.0.0.0" if cmd_opts.listen else None


def fix_asyncio_event_loop_policy():
    """
        The default `asyncio` event loop policy only automatically creates
        event loops in the main threads. Other threads must create event
        loops explicitly or `asyncio.get_event_loop` (and therefore
        `.IOLoop.current`) will fail. Installing this policy allows event
        loops to be created automatically on any thread, matching the
        behavior of Tornado versions prior to 5.0 (or 5.0 on Python 2).
    """

    import asyncio

    if sys.platform == "win32" and hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
        # "Any thread" and "selector" should be orthogonal, but there's not a clean
        # interface for composing policies so pick the right base.
        _BasePolicy = asyncio.WindowsSelectorEventLoopPolicy  # type: ignore
    else:
        _BasePolicy = asyncio.DefaultEventLoopPolicy

    class AnyThreadEventLoopPolicy(_BasePolicy):  # type: ignore
        """Event loop policy that allows loop creation on any thread.
        Usage::

            asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
        """

        def get_event_loop(self) -> asyncio.AbstractEventLoop:
            try:
                return super().get_event_loop()
            except (RuntimeError, AssertionError):
                # This was an AssertionError in python 3.4.2 (which ships with debian jessie)
                # and changed to a RuntimeError in 3.4.3.
                # "There is no current event loop in thread %r"
                loop = self.new_event_loop()
                self.set_event_loop(loop)
                return loop

    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())


def check_versions():
    if shared.cmd_opts.skip_version_check:
        return

    expected_torch_version = "2.0.0"

    if version.parse(torch.__version__) < version.parse(expected_torch_version):
        errors.print_error_explanation(f"""
You are running torch {torch.__version__}.
The program is tested to work with torch {expected_torch_version}.
To reinstall the desired version, run with commandline flag --reinstall-torch.
Beware that this will cause a lot of large files to be downloaded, as well as
there are reports of issues with training tab on the latest version.

Use --skip-version-check commandline argument to disable this check.
        """.strip())

    expected_xformers_version = "0.0.20"
    if shared.xformers_available:
        import xformers

        if version.parse(xformers.__version__) < version.parse(expected_xformers_version):
            errors.print_error_explanation(f"""
You are running xformers {xformers.__version__}.
The program is tested to work with xformers {expected_xformers_version}.
To reinstall the desired version, run with commandline flag --reinstall-xformers.

Use --skip-version-check commandline argument to disable this check.
            """.strip())


def restore_config_state_file():
    config_state_file = shared.opts.restore_config_state_file
    if config_state_file == "":
        return

    shared.opts.restore_config_state_file = ""
    shared.opts.save(shared.config_filename)

    if os.path.isfile(config_state_file):
        print(f"*** About to restore extension state from file: {config_state_file}")
        with open(config_state_file, "r", encoding="utf-8") as f:
            config_state = json.load(f)
            config_states.restore_extension_config(config_state)
        startup_timer.record("restore extension config")
    elif config_state_file:
        print(f"!!! Config state backup not found: {config_state_file}")


def validate_tls_options():
    if not (cmd_opts.tls_keyfile and cmd_opts.tls_certfile):
        return

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
    startup_timer.record("TLS")


def get_gradio_auth_creds() -> Iterable[tuple[str, ...]]:
    """
    Convert the gradio_auth and gradio_auth_path commandline arguments into
    an iterable of (username, password) tuples.
    """
    def process_credential_line(s) -> tuple[str, ...] | None:
        s = s.strip()
        if not s:
            return None
        return tuple(s.split(':', 1))

    if cmd_opts.gradio_auth:
        for cred in cmd_opts.gradio_auth.split(','):
            cred = process_credential_line(cred)
            if cred:
                yield cred

    if cmd_opts.gradio_auth_path:
        with open(cmd_opts.gradio_auth_path, 'r', encoding="utf8") as file:
            for line in file.readlines():
                for cred in line.strip().split(','):
                    cred = process_credential_line(cred)
                    if cred:
                        yield cred


def configure_sigint_handler():
    # make the program just exit at ctrl+c without waiting for anything
    def sigint_handler(sig, frame):
        print(f'Interrupted with signal {sig} in {frame}')
        os._exit(0)

    if not os.environ.get("COVERAGE_RUN"):
        # Don't install the immediate-quit handler when running under coverage,
        # as then the coverage report won't be generated.
        signal.signal(signal.SIGINT, sigint_handler)


def configure_opts_onchange():
    shared.opts.onchange("sd_model_checkpoint", wrap_queued_call(lambda: modules.sd_models.reload_model_weights()), call=False)
    shared.opts.onchange("sd_vae", wrap_queued_call(lambda: modules.sd_vae.reload_vae_weights()), call=False)
    shared.opts.onchange("sd_vae_as_default", wrap_queued_call(lambda: modules.sd_vae.reload_vae_weights()), call=False)
    shared.opts.onchange("temp_dir", ui_tempdir.on_tmpdir_changed)
    shared.opts.onchange("gradio_theme", shared.reload_gradio_theme)
    shared.opts.onchange("cross_attention_optimization", wrap_queued_call(lambda: modules.sd_hijack.model_hijack.redo_hijack(shared.sd_model)), call=False)
    startup_timer.record("opts onchange")


def initialize():
    fix_asyncio_event_loop_policy()
    validate_tls_options()
    configure_sigint_handler()
    check_versions()
    modelloader.cleanup_models()
    configure_opts_onchange()

    modules.sd_models.setup_model()
    startup_timer.record("setup SD model")

    codeformer.setup_model(cmd_opts.codeformer_models_path)
    startup_timer.record("setup codeformer")

    gfpgan.setup_model(cmd_opts.gfpgan_models_path)
    startup_timer.record("setup gfpgan")

    initialize_rest(reload_script_modules=False)
    modules.script_callbacks.before_ui_callback()


def initialize_rest(*, reload_script_modules=False):
    """
    Called both from initialize() and when reloading the webui.
    """
    sd_samplers.set_samplers()
    extensions.list_extensions()
    startup_timer.record("list extensions")

    restore_config_state_file()

    if cmd_opts.ui_debug_mode:
        shared.sd_upscalers = upscaler.UpscalerLanczos().scalers
        modules.scripts.load_scripts()
        return

    modules.sd_models.list_models()
    startup_timer.record("list SD models")

    localization.list_localizations(cmd_opts.localizations_dir)

    with startup_timer.subcategory("load scripts"):
        modules.scripts.load_scripts()

    if reload_script_modules:
        for module in [module for name, module in sys.modules.items() if name.startswith("modules.ui")]:
            importlib.reload(module)
        startup_timer.record("reload script modules")

    modelloader.load_upscalers()
    startup_timer.record("load upscalers")

    modules.sd_vae.refresh_vae_list()
    startup_timer.record("refresh VAE")
    modules.textual_inversion.textual_inversion.list_textual_inversion_templates()
    startup_timer.record("refresh textual inversion templates")

    modules.script_callbacks.on_list_optimizers(modules.sd_hijack_optimizations.list_optimizers)
    modules.sd_hijack.list_optimizers()
    startup_timer.record("scripts list_optimizers")

    modules.sd_unet.list_unets()
    startup_timer.record("scripts list_unets")

    def load_model():
        """
        Accesses shared.sd_model property to load model.
        After it's available, if it has been loaded before this access by some extension,
        its optimization may be None because the list of optimizaers has neet been filled
        by that time, so we apply optimization again.
        """

        shared.sd_model  # noqa: B018

        if modules.sd_hijack.current_optimizer is None:
            modules.sd_hijack.apply_optimizations()

    Thread(target=load_model).start()

    Thread(target=devices.first_time_calculation).start()

    shared.reload_hypernetworks()
    startup_timer.record("reload hypernetworks")

    ui_extra_networks.initialize()
    ui_extra_networks.register_default_pages()

    extra_networks.initialize()
    extra_networks.register_default_extra_networks()
    startup_timer.record("initialize extra networks")


def base64_to_image(base64_str):  # 用 b.show()可以展示
    image = base64.b64decode(base64_str, altchars=None, validate=False)
    image = BytesIO(image)
    image = Image.open(image)
    return image

class HashableNpArray(np.ndarray):
    def __new__(cls, input_array):
        # Input array is an instance of ndarray.
        # The view makes the input array and returned array share the same data.
        obj = np.asarray(input_array).view(cls)
        return obj

    def __eq__(self, other) -> bool:
        return np.array_equal(self, other)

    def __hash__(self):
        # Hash the bytes representing the data of the array.
        return hash(self.tobytes())

class ControlMode(Enum):
    """
    The improved guess mode.
    """

    BALANCED = "Balanced"
    PROMPT = "My prompt is more important"
    CONTROL = "ControlNet is more important"
    
class SdInference:
    def __init__(self):
        initialize()
        self.api = SimpleApi(queue_lock)
        scripts = modules.scripts
        self.script_runner = scripts.scripts_txt2img
        if not self.script_runner.scripts:
            self.script_runner.initialize_scripts(False)
            modules.ui.create_ui()
            
    def run_text2img(self,
                    prompt: str = "",
                    negative_prompt: str = None,
                    width: int = 512,
                    height: int = 512,
                    seed: int = -1,
                    steps: int = 20,
                    batch_size: int = 1,
                    enable_hr: bool = False,
                    hr_scale: float = 2.0,
                    hr_upscaler: str = "R-ESRGAN 4x+",
                    sampler_index: str = "Euler a",
                    denoising_strength: float = 0.2,
                    hr_second_pass_steps: int = 20,
                    prompt_styles: list = [],
                    restore_faces: bool = False,
                    tiling: bool = False,
                    n_iter: int = 1,
                    cfg_scale: float = 7, 
                    subseed: int = -1, 
                    subseed_strength: float = 0, 
                    seed_resize_from_h: int = 0, 
                    seed_resize_from_w: int = 0, 
                    seed_enable_extras: bool = False, 
                    hr_resize_x: int = 0, 
                    hr_resize_y: int = 0, 
                    hr_sampler_index: int = 0, 
                    hr_prompt: str = "", 
                    hr_negative_prompt: str = "", 
                    override_settings_texts = None,
                    **kwargs):
        txt2imgreq = StableDiffusionTxt2ImgProcessingAPI(prompt=prompt, 
                                                         negative_prompt=negative_prompt,
                                                         width=width, 
                                                         height=height, 
                                                         seed=seed, 
                                                         steps=steps, 
                                                         batch_size=batch_size, 
                                                         sampler_index=sampler_index, 
                                                         enable_hr=enable_hr, 
                                                         hr_scale=hr_scale, 
                                                         hr_upscaler=hr_upscaler, 
                                                         denoising_strength = denoising_strength,
                                                         hr_second_pass_steps = hr_second_pass_steps,
                                                         prompt_styles = prompt_styles,
                                                         restore_faces = restore_faces,
                                                         tiling = tiling,
                                                         n_iter = n_iter,
                                                         cfg_scale = cfg_scale, 
                                                         subseed = subseed, 
                                                         subseed_strength = subseed_strength, 
                                                         seed_resize_from_h = seed_resize_from_h, 
                                                         seed_resize_from_w = seed_resize_from_h, 
                                                         seed_enable_extras = seed_enable_extras, 
                                                         hr_resize_x = hr_resize_x, 
                                                         hr_resize_y = hr_resize_y, 
                                                         hr_sampler_index = hr_sampler_index, 
                                                         hr_prompt = hr_prompt, 
                                                         hr_negative_prompt = hr_negative_prompt, 
                                                         override_settings_texts = override_settings_texts,
                                                         **kwargs)

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
                    steps: int = 20,
                    batch_size: int = 1,
                    sampler_index: str = "Euler a",
                    inpaint_full_res: bool = False,
                    denoising_strength: float = 0.75,
                    inpainting_fill: int = 1,
                    cfg_scale: float = 7, 
                    **kwargs):
        init_images = []
        for base64_image in base64_images:
            init_images.append(decode_base64_to_image(base64_image))
        # in_mask = base64_to_image(mask)
        img2imgreq = StableDiffusionImg2ImgProcessingAPI(init_images=init_images,
                                                         mask=mask,
                                                         prompt=prompt,
                                                         negative_prompt=negative_prompt,
                                                         width=width,
                                                         height=height,
                                                         seed=seed,
                                                         steps=steps,
                                                         sampler_index=sampler_index,
                                                         inpaint_full_res=inpaint_full_res,
                                                         denoising_strength=denoising_strength,
                                                         inpainting_fill = inpainting_fill,
                                                         batch_size=batch_size, cfg_scale=cfg_scale, **kwargs)
        try:
            response = self.api.img2imgapi(img2imgreq)
        except Exception as e:
            raise e
        return response.images

    def run_upscale(self,
                    image : str,
                    resize_mode: int = 0,
                    show_extras_results: bool = True,
                    gfpgan_visibility: float = 0,
                    codeformer_visibility: float = 0,
                    codeformer_weight: float = 0,
                    upscaling_resize: float = 2,
                    upscaling_resize_w: int = 512,
                    upscaling_resize_h: int = 512,
                    upscaling_crop: bool = True,
                    upscaler_1: str = "R-ESRGAN 4x+",
                    upscaler_2: str = "None",
                    extras_upscaler_2_visibility: float = 0,
                    upscale_first: bool = False,
                    **kwargs):


        upscalereq = ExtrasSingleImageRequest(image=image,
                                                resize_mode=resize_mode,
                                                show_extras_results=show_extras_results,
                                                gfpgan_visibility=gfpgan_visibility,
                                                codeformer_visibility=codeformer_visibility,
                                                codeformer_weight=codeformer_weight,
                                                upscaling_resize=upscaling_resize,
                                                upscaling_resize_w=upscaling_resize_w,
                                                upscaling_resize_h=upscaling_resize_h,
                                                upscaling_crop=upscaling_crop,
                                                upscaler_1=upscaler_1,
                                                upscaler_2=upscaler_2,
                                                extras_upscaler_2_visibility=extras_upscaler_2_visibility,
                                                upscale_first=upscale_first,
                                                **kwargs)

        try:
            response = self.api.extras_single_image_api(upscalereq)
        except Exception as e:
            raise e
        return response.image

    def run_imgfuse(self,
                    base64_images : list,
                    mask: str = None,
                    prompt: str = "",
                    negative_prompt: str = None,
                    width: int = 512,
                    height: int = 512,
                    seed: int = -1,
                    steps: int = 20,
                    batch_size: int = 1,
                    sampler_index: str = "Euler a",
                    inpaint_full_res: bool = False,
                    denoising_strength: float = 0.75,
                    **kwargs):
        init_images = []
        for base64_image in base64_images:
            init_images.append(decode_base64_to_image(base64_image))
        # in_mask = base64_to_image(mask)
        img2imgreq = StableDiffusionImg2ImgProcessingAPI(init_images=init_images,
                                                         mask=mask,
                                                         prompt=prompt,
                                                         negative_prompt=negative_prompt,
                                                         width=width,
                                                         height=height,
                                                         seed=seed,
                                                         steps=steps,
                                                         sampler_index=sampler_index,
                                                         inpaint_full_res=inpaint_full_res,
                                                         denoising_strength=denoising_strength,
                                                         batch_size=batch_size, **kwargs)
        try:
            response = self.api.imgfuseapi(img2imgreq)
        except Exception as e:
            raise e
        return response.images
    
    def run_ctrl2img(self, 
                    base_image: str,
                    ctrl_type: str = 'canny',
                    perference: str = 'BALANCED',
                    resize_mode: str = "Resize and Fill",
                    threshold_a: int = 100,
                    threshold_b: int = 200,
                    prompt: str = "",
                    negative_prompt: str = None,
                    width: int = 512,
                    height: int = 512,
                    seed: int = -1,
                    steps: int = 20,
                    batch_size: int = 1,
                    enable_hr: bool = False,
                    hr_scale: float = 2.0,
                    hr_upscaler: str = "R-ESRGAN 4x+",
                    sampler_index: str = "Euler a",
                    denoising_strength: float = 0.2,
                    hr_second_pass_steps: int = 20,
                    prompt_styles: list = [],
                    restore_faces: bool = False,
                    tiling: bool = False,
                    n_iter: int = 1,
                    cfg_scale: float = 7, 
                    subseed: int = -1, 
                    subseed_strength: float = 0, 
                    seed_resize_from_h: int = 0, 
                    seed_resize_from_w: int = 0, 
                    seed_enable_extras: bool = False, 
                    hr_resize_x: int = 0, 
                    hr_resize_y: int = 0, 
                    hr_sampler_index: int = 0, 
                    hr_prompt: str = "", 
                    hr_negative_prompt: str = "", 
                    override_settings_texts = None,
                    **kwargs):
        controlnet_unit_module_map = {
            'canny' : 'control_v11p_sd15_canny [d14c016b]',
        }
        controlnet_unit_mode_map = {
            'BALANCED': ControlMode.BALANCED,
            'PROMPT' : ControlMode.PROMPT,
            "CONTROL" : ControlMode.CONTROL
        }
        ctrl_image = decode_base64_to_image(base_image)
        for script in self.script_runner.alwayson_scripts:
            if "controlnet.py.Script" in script.__str__():
                controlnet_unit = script.get_default_ui_unit(False)
                ctrl_image_array = np.asarray(ctrl_image)
                ctrl_image_array = ctrl_image_array[..., 0] if ctrl_image_array.shape[-1] == 2 else ctrl_image_array
                ctrl_image_np_hash = HashableNpArray(ctrl_image_array)
                ctrl_image_preprocessed = script.preprocessor[ctrl_type](ctrl_image_np_hash)[0]
                controlnet_unit.image = {'image': ctrl_image_preprocessed, 'mask':None}
                controlnet_unit.enabled = True
                controlnet_unit.model = controlnet_unit_module_map[ctrl_type]
                controlnet_unit.module = ctrl_type
                controlnet_unit.resize_mode = resize_mode
                controlnet_unit.threshold_a = threshold_a
                controlnet_unit.threshold_b = threshold_b
                controlnet_unit.control_mode = controlnet_unit_mode_map[perference].value
        alwayson_scripts = {
            'controlnet':{
                'args': [controlnet_unit]
            }

        }
        txt2imgreq = StableDiffusionTxt2ImgProcessingAPI(prompt=prompt, 
                                                         negative_prompt=negative_prompt,
                                                         width=width, 
                                                         height=height, 
                                                         seed=seed, 
                                                         steps=steps, 
                                                         batch_size=batch_size, 
                                                         sampler_index=sampler_index, 
                                                         enable_hr=enable_hr, 
                                                         hr_scale=hr_scale, 
                                                         hr_upscaler=hr_upscaler, 
                                                         denoising_strength = denoising_strength,
                                                         hr_second_pass_steps = hr_second_pass_steps,
                                                         prompt_styles = prompt_styles,
                                                         restore_faces = restore_faces,
                                                         tiling = tiling,
                                                         n_iter = n_iter,
                                                         cfg_scale = cfg_scale, 
                                                         subseed = subseed, 
                                                         subseed_strength = subseed_strength, 
                                                         seed_resize_from_h = seed_resize_from_h, 
                                                         seed_resize_from_w = seed_resize_from_h, 
                                                         seed_enable_extras = seed_enable_extras, 
                                                         hr_resize_x = hr_resize_x, 
                                                         hr_resize_y = hr_resize_y, 
                                                         hr_sampler_index = hr_sampler_index, 
                                                         hr_prompt = hr_prompt, 
                                                         hr_negative_prompt = hr_negative_prompt, 
                                                         override_settings_texts = override_settings_texts,
                                                         alwayson_scripts = alwayson_scripts,
                                                         **kwargs)

        try:
            response = self.api.text2imgapi(txt2imgreq)
        except Exception as e:
            raise e
        return response.images
    
import grpc
from proto import sd_pb2, sd_pb2_grpc
from concurrent import futures

class SdEngine(sd_pb2_grpc.SdEngineServicer):
    '''
    继承GrpcServiceServicer,实现hello方法
    '''
    def __init__(self):
        self.sd_inference = SdInference()

    def text2img(self, request, context):
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1
        cfg_scale = request.cfg_scale if request.cfg_scale != 0 else 7
        enable_hr = request.enable_hr
        hr_scale = request.hr_scale if request.hr_scale != 0 else 2
        hr_upscaler = request.hr_upscaler if request.hr_upscaler else "Latent"
        
        try:
            status = 200
            message = "success"
            imgs_base64 = self.sd_inference.run_text2img(prompt, negative_prompt, width, height, seed, steps, batch_size, enable_hr, hr_scale, hr_upscaler, cfg_scale=cfg_scale)
        except Exception as e:
            status = 500
            message = e.__str__()
            imgs_base64 = ""
        return sd_pb2.SdResponse(status=status, message=message, base64=imgs_base64)
    
    def img2img(self, request, context):
        base64_images = request.base64_images
        mask = request.mask if request.mask != "" else None
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1
        cfg_scale = request.cfg_scale if request.cfg_scale != 0 else 7
        denoising_strength = request.denoising_strength if request.denoising_strength != 0 else 0.75
        try:
            status = 200
            message = "success"
            imgs_base64 = self.sd_inference.run_img2img(base64_images, mask, prompt, negative_prompt, width, height, seed, steps, batch_size, denoising_strength=denoising_strength, cfg_scale=cfg_scale)
        except Exception as e:
            status = 500
            message = e.__str__()
            imgs_base64 = ""
        return sd_pb2.SdResponse(status=status, message=message, base64=imgs_base64)

    def upscale(self, request, context):
        base64_image = request.base64_image
        upscaling_resize = request.upscaling_resize if request.upscaling_resize != 0 else 2
        upscaler_1 = request.upscaler_1 if request.upscaler_1 else "R-ESRGAN 4x+"

        try:
            status = 200
            message = "success"
            img_base64 = self.sd_inference.run_upscale(image = base64_image, upscaling_resize=upscaling_resize, upscaler_1=upscaler_1)
        except Exception as e:
            status = 500
            message = e.__str__()
            img_base64 = ""
        return sd_pb2.SdResponse(status=status, message=message, base64=[img_base64])

    def imgfuse(self, request, context):
        base64_images = request.base64_images
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1
        denoising_strength = request.denoising_strength if request.denoising_strength != 0 else 0.75
        try:
            status = 200
            message = "success"
            imgs_base64 = self.sd_inference.run_imgfuse(base64_images, None, prompt, negative_prompt, width, height, seed, steps, batch_size, denoising_strength=denoising_strength)
        except Exception as e:
            status = 500
            message = e.__str__()
            imgs_base64 = ""
        return sd_pb2.SdResponse(status=status, message=message, base64=imgs_base64)
    
    def ctrl2img(self, request, context):
        base64_image = request.base64_image
        ctrl_type = "canny"
        resize_mode = "Resize and Fill"
        threshold_a = 100
        threshold_b = 200
        perference = request.perference
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1

        enable_hr = request.enable_hr
        hr_scale = request.hr_scale if request.hr_scale != 0 else 2
        hr_upscaler = request.hr_upscaler if request.hr_upscaler else "Latent"
        
        try:
            status = 200
            message = "success"
            imgs_base64 = self.sd_inference.run_ctrl2img(base64_image, ctrl_type, perference, resize_mode,  threshold_a, threshold_b, prompt, negative_prompt, width, height, seed, steps, batch_size, enable_hr, hr_scale, hr_upscaler)
            imgs_base64 = imgs_base64[:batch_size]
        except Exception as e:
            status = 500
            message = e.__str__()
            imgs_base64 = ""
        return sd_pb2.SdResponse(status=status, message=message, base64=imgs_base64)
        
def run(host="127.0.0.1", port=8000, max_messave_length=256 * 1024 * 1024):

    MAX_MESSAGE_LENGTH = max_messave_length
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=[
                ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
    sd_pb2_grpc.add_SdEngineServicer_to_server(SdEngine(),server)
    server.add_insecure_port('{}:{}'.format(host, port))
    server.start()
    print("start service...")
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    port = shared.cmd_opts.port
    host = shared.cmd_opts.server_name
    if host is not None:
        run(host=host, port=port)
    else:
        run(port=port)
    while True:
        time.sleep(10)