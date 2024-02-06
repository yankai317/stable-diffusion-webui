import os
import subprocess
from proto import sd_pb2, sd_pb2_grpc
import grpc
import time
import asyncio
from PIL import Image
import base64
from io import BytesIO
from threading import Thread, Lock
import torch

class SdServiceHandler(object):
    def __init__(self, host="127.0.0.1", port=8000, device_id=0, config_path="config.json", log_save_path="log.txt", err_log_save_path="log_err.txt", max_messave_length=256 * 1024 * 1024) -> None:
        with open(log_save_path, 'w') as log_write:
            with open(err_log_save_path, 'w') as err_log_wirte:
                self.sd_server = subprocess.Popen(["python sd_engine.py --port {} --device-id {} --ui-settings-file {} --server-name {} --xformers --disable-safe-unpickle".format(port, device_id, config_path, host)], shell=True, stdout=log_write, stderr=err_log_wirte)
        
        self.device_id = device_id
        self.port = port
        self.config_path = config_path
        self.host = host

    def get_handler_info(self):
        return {
            "host":self.host,
            "port":self.port,
            "device_id":self.device_id,
            "config_path":self.config_path,
        }

    def register(self):
        pass

    def get_status(self):
        pass

    def __del__(self):
        self.sd_server.kill()


class SdClientHandler(object):
    def __init__(self, host, port, max_messave_length=256 * 1024 * 1024) -> None:
        self.port = port
        self.host = host

        conn=grpc.insecure_channel('{}:{}'.format(host, port),
                                options=[ 
            ('grpc.max_send_message_length', max_messave_length), 
            ('grpc.max_receive_message_length', max_messave_length), 
        ])
        self.sd_client = sd_pb2_grpc.SdEngineStub(channel=conn)
        self.isFree = True
        self.lock = Lock()
        
    def run_txt2img(self, kwargs = {}):

        prompt = kwargs['prompt'] if 'prompt' in kwargs.keys() else ""
        negative_prompt = kwargs['negative_prompt'] if 'negative_prompt' in kwargs.keys() else None
        width = kwargs['width'] if 'width' in kwargs.keys() else 512
        height = kwargs['height'] if 'height' in kwargs.keys() else 512
        seed = kwargs['seed'] if 'seed' in kwargs.keys() else -1
        steps = kwargs['steps'] if 'steps' in kwargs.keys() else 20
        batch_size = kwargs['batch_size'] if 'batch_size' in kwargs.keys() else 1
        cfg_scale = kwargs['cfg_scale'] if 'cfg_scale' in kwargs.keys() else 7
        enable_hr = kwargs['enable_hr'] if 'enable_hr' in kwargs.keys() else False
        hr_scale = kwargs['hr_scale'] if 'hr_scale' in kwargs.keys() else 2
        hr_upscaler = kwargs['hr_upscaler'] if 'hr_upscaler' in kwargs.keys() else "Latent"
        
        request = sd_pb2.SdText2ImgRequest(prompt = prompt,
                                            negative_prompt = negative_prompt,
                                            width = width,
                                            height = height,
                                            seed = seed,
                                            steps = steps,
                                            batch_size = batch_size,
                                            enable_hr = enable_hr,
                                            hr_scale = hr_scale,
                                            hr_upscaler = hr_upscaler,
                                            cfg_scale = cfg_scale
                                            )
        with self.lock:
            response = self.sd_client.text2img(request)
        return response

    def run_img2img(self, kwargs = {}):
        '''
        模拟请求服务方法信息
        :return:
        '''
        base64_images = kwargs['base64_images'] if 'base64_images' in kwargs.keys() else ""
        mask_base64 = kwargs['mask'] if 'mask' in kwargs.keys() else None
        prompt = kwargs['prompt'] if 'prompt' in kwargs.keys() else ""
        negative_prompt = kwargs['negative_prompt'] if 'negative_prompt' in kwargs.keys() else None
        width = kwargs['width'] if 'width' in kwargs.keys() else 512
        height = kwargs['height'] if 'height' in kwargs.keys() else 512
        seed = kwargs['seed'] if 'seed' in kwargs.keys() else -1
        steps = kwargs['steps'] if 'steps' in kwargs.keys() else 20
        batch_size = kwargs['batch_size'] if 'batch_size' in kwargs.keys() else 1
        cfg_scale = kwargs['cfg_scale'] if 'cfg_scale' in kwargs.keys() else 7
        denoising_strength = kwargs['denoising_strength'] if 'denoising_strength' in kwargs.keys() else 0.75
        request = sd_pb2.SdImg2ImgRequest(
            base64_images = base64_images,
            mask = mask_base64,
            prompt = prompt,
            negative_prompt = negative_prompt,
            width = width,
            height = height,
            seed = seed,
            steps = steps,
            batch_size = batch_size,
            denoising_strength = denoising_strength,
            cfg_scale = cfg_scale)
        
        with self.lock:
            response = self.sd_client.img2img(request)
        return response
    
    def run_upscale(self, kwargs = {}):
        '''
        模拟请求服务方法信息
        :return:
        '''
        base64_image = kwargs['base64_image'] if 'base64_image' in kwargs.keys() else ""
        upscaling_resize = kwargs['upscaling_resize'] if 'upscaling_resize' in kwargs.keys() else 2
        upscaler_1 = kwargs['upscaler_1'] if 'upscaler_1' in kwargs.keys() else "R-ESRGAN 4x+"
        
        request = sd_pb2.SdUpscaleRequest(
            base64_image = base64_image,
            upscaling_resize = upscaling_resize,
            upscaler_1 = upscaler_1)
        
        with self.lock:
            response = self.sd_client.upscale(request)
        
        return response

    def run_imgfuse(self, kwargs = {}):
        '''
        模拟请求服务方法信息
        :return:
        '''
        base64_images = kwargs['base64_images'] if 'base64_images' in kwargs.keys() else ""
        prompt = kwargs['prompt'] if 'prompt' in kwargs.keys() else ""
        negative_prompt = kwargs['negative_prompt'] if 'negative_prompt' in kwargs.keys() else None
        width = kwargs['width'] if 'width' in kwargs.keys() else 512
        height = kwargs['height'] if 'height' in kwargs.keys() else 512
        seed = kwargs['seed'] if 'seed' in kwargs.keys() else -1
        steps = kwargs['steps'] if 'steps' in kwargs.keys() else 20
        batch_size = kwargs['batch_size'] if 'batch_size' in kwargs.keys() else 1
        denoising_strength = kwargs['denoising_strength'] if 'denoising_strength' in kwargs.keys() else 0.75
        
        request = sd_pb2.SdImgFuseRequest(
            base64_images = base64_images,
            prompt = prompt,
            negative_prompt = negative_prompt,
            width = width,
            height = height,
            seed = seed,
            steps = steps,
            batch_size = batch_size,
            denoising_strength = denoising_strength)
        
        with self.lock:
            response = self.sd_client.imgfuse(request)
        return response

    def run_ctrl2img(self, kwargs = {}):

        base64_image = kwargs['base64_image'] if 'base64_image' in kwargs.keys() else None
        perference = kwargs['perference'] if 'perference' in kwargs.keys() else "BALANCED"
        ctrl_type = kwargs['ctrl_type'] if 'ctrl_type' in kwargs.keys() else "canny"
        resize_mode = kwargs['resize_mode'] if 'resize_mode' in kwargs.keys() else "Resize and Fill"
        threshold_a = kwargs['threshold_a'] if 'threshold_a' in kwargs.keys() else 100
        threshold_b = kwargs['threshold_b'] if 'threshold_b' in kwargs.keys() else 200
        
        prompt = kwargs['prompt'] if 'prompt' in kwargs.keys() else ""
        negative_prompt = kwargs['negative_prompt'] if 'negative_prompt' in kwargs.keys() else None
        width = kwargs['width'] if 'width' in kwargs.keys() else 512
        height = kwargs['height'] if 'height' in kwargs.keys() else 512
        seed = kwargs['seed'] if 'seed' in kwargs.keys() else -1
        steps = kwargs['steps'] if 'steps' in kwargs.keys() else 20
        batch_size = kwargs['batch_size'] if 'batch_size' in kwargs.keys() else 1
        
        enable_hr = kwargs['enable_hr'] if 'enable_hr' in kwargs.keys() else False
        hr_scale = kwargs['hr_scale'] if 'hr_scale' in kwargs.keys() else 2
        hr_upscaler = kwargs['hr_upscaler'] if 'hr_upscaler' in kwargs.keys() else "Latent"
        
        request = sd_pb2.SdCtrl2ImgRequest(
                                            base64_image = base64_image,
                                            perference = perference,
                                            prompt = prompt,
                                            negative_prompt = negative_prompt,
                                            width = width,
                                            height = height,
                                            seed = seed,
                                            steps = steps,
                                            batch_size = batch_size,
                                            enable_hr = enable_hr,
                                            hr_scale = hr_scale,
                                            hr_upscaler = hr_upscaler
                                            )
        with self.lock:
            response = self.sd_client.ctrl2img(request)
        return response

    def run_interrogate(self, kwargs = {}):

        base64_image = kwargs['base64_image'] if 'base64_image' in kwargs.keys() else None
        
        request = sd_pb2.SdInterrogateRequest(
                                            base64_image = base64_image
                                            )
        with self.lock:
            response = self.sd_client.interrogate(request)
        return response
    
    def run_normalize(self, kwargs = {}):

        base64_image = kwargs['base64_image'] if 'base64_image' in kwargs.keys() else None
        resize = kwargs['resize'] if 'resize' in kwargs.keys() else False
        size = kwargs['size'] if 'size' in kwargs.keys() else 512
        model = kwargs['model'] if 'model' in kwargs.keys() else "transparent_background"
        threshold = kwargs['threshold'] if 'threshold' in kwargs.keys() else 10
        
        request = sd_pb2.SdNormalizeRequest(
                                            base64_image = base64_image,
                                            resize = resize,
                                            size = size,
                                            model = model,
                                            threshold = threshold
                                            )
        with self.lock:
            response = self.sd_client.normalize(request)
        return response
    
    def run_canny(self, kwargs = {}):
        base64_image = kwargs['base64_image'] if 'base64_image' in kwargs.keys() else None
        low_threshold = kwargs['low_threshold'] if 'low_threshold' in kwargs.keys() else 100
        high_threshold = kwargs['high_threshold'] if 'high_threshold' in kwargs.keys() else 200
        reverse = kwargs['reverse'] if 'reverse' in kwargs.keys() else False
        
        request = sd_pb2.SdCannyRequest(
                                            base64_image = base64_image,
                                            low_threshold = low_threshold,
                                            high_threshold = high_threshold,
                                            reverse = reverse
                                            )
        with self.lock:
            response = self.sd_client.canny(request)
        return response
    
    def run_anydoor(self, kwargs = {}):
        image = kwargs['image'] if 'image' in kwargs.keys() else None
        mask = kwargs['mask'] if 'mask' in kwargs.keys() else None
        ref_image = kwargs['ref_image'] if 'ref_image' in kwargs.keys() else None
        ref_mask = kwargs['ref_mask'] if 'ref_mask' in kwargs.keys() else None
        strength = kwargs['strength'] if 'strength' in kwargs.keys() else 1
        ddim_steps = kwargs['ddim_steps'] if 'ddim_steps' in kwargs.keys() else 30
        scale = kwargs['scale'] if 'scale' in kwargs.keys() else 3
        seed = kwargs['seed'] if 'seed' in kwargs.keys() else -1
        enable_shape_control = kwargs['enable_shape_control'] if 'enable_shape_control' in kwargs.keys() else False
        
        request = sd_pb2.SdAnydoorRequest(
                                            image = image,
                                            mask = mask,
                                            ref_image = ref_image,
                                            ref_mask = ref_mask,
                                            strength = strength,
                                            ddim_steps = ddim_steps,
                                            scale = scale,
                                            seed = seed,
                                            enable_shape_control = enable_shape_control
                                            )
        with self.lock:
            response = self.sd_client.anydoor(request)
        return response
        
    def __enter__(self):
        self.isFree = False

    def __exit__(self, type, value, traceback):
        self.isFree = True

    def __del__(self):
        del self.sd_client
    
# 调用异步函数
if __name__ == "__main__":
    s1 = SdServiceHandler(device_id=0, port=8000, config_path="config.json", log_save_path="log_1.txt",err_log_save_path="log_err_1.txt",)
    s2 = SdServiceHandler(device_id=1, port=8001, config_path="config_1.json", log_save_path="log_2.txt",err_log_save_path="log_err_2.txt")
    time.sleep(20)
    with s1:
        s1.run_txt2img(kwargs = {'prompt':"car"})
    with s2:
        s2.run_txt2img(kwargs = {'prompt':"car"})
