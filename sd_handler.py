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
                self.sd_server = subprocess.Popen(["python sd_engine.py --port {} --device-id {} --ui-settings-file {} --server-name {} --xformers".format(port, device_id, config_path, host)], shell=True, stdout=log_write, stderr=err_log_wirte)
        
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
                                            hr_upscaler = hr_upscaler
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
        
        request = sd_pb2.SdImg2ImgRequest(
            base64_images = base64_images,
            mask = mask_base64,
            prompt = prompt,
            negative_prompt = negative_prompt,
            width = width,
            height = height,
            seed = seed,
            steps = steps,
            batch_size = batch_size)
        
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
