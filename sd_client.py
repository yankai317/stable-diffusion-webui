#! /usr/bin/env python
# coding=utf8
import grpc
# coding=utf8
import grpc
from proto import sd_pb2, sd_pb2_grpc
from PIL import Image
import base64
from io import BytesIO
import time
def base64_to_image(base64_str):  # 用 b.show()可以展示
    image = base64.b64decode(base64_str, altchars=None, validate=False)
    image = BytesIO(image)
    image = Image.open(image)
    return image

from threading import Thread

            
def async_infer(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@async_infer
def run_txt2img_asyn():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    # client = sd_pb2_grpc.SdEngineStub(channel=conn)
    request = sd_pb2.SdText2ImgRequest(prompt = "shirt",
        negative_prompt = None,
        width = 512,
        height = 512,
        seed = -1,
        steps = 20,
        batch_size = 4,
        enable_hr = True,
        hr_scale = 2,
        hr_upscaler = "R-ESRGAN 4x+"
        )
    respnse = client.text2img_asyn(request)
    task_id = None
    if respnse.message == "success":
        task_id = respnse.task_id
    print(respnse.status, respnse.message)
    
    request = sd_pb2.SdQueryRequest(task_id = task_id)
    while True:
        time.sleep(1)
        respnse = client.query(request)
        print(respnse.status, respnse.message)
        if respnse.message == "success" or respnse.status == 500:
            break
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_text2img_{i}_{time.time()}.jpg')

@async_infer
def run_txt2img():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    # client = sd_pb2_grpc.SdEngineStub(channel=conn)
    request = sd_pb2.SdText2ImgRequest(prompt = "<lora:LCM_LoRA_Weights_SD15:1>,down jacket",
        negative_prompt = "",
        width = 512,
        height = 512,
        seed = -1,
        steps = 5,
        batch_size = 1,
        enable_hr = False,
        hr_scale = 2,
        hr_upscaler = "R-ESRGAN 4x+",
        cfg_scale = 1.5,
        disable_default_prompt=False
        )
    t = time.time()
    respnse = client.text2img(request)
    print(respnse.status, respnse.message, time.time() - t)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_text2img_{i}_{time.time()}.jpg')

def run_txt2img_engine():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    # client = sd_pb2_grpc.SdServiceStub(channel=conn)
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    request = sd_pb2.SdText2ImgRequest(prompt = "<lora:LCM_LoRA_Weights_SD15:1>,down jacket",
        negative_prompt = "",
        width = 512,
        height = 512,
        seed = -1,
        steps = 5,
        batch_size = 1,
        enable_hr = False,
        hr_scale = 2,
        hr_upscaler = "R-ESRGAN 4x+",
        cfg_scale = 1.5,
        disable_default_prompt=False
        )
    t = time.time()
    respnse = client.text2img(request)
    print(respnse.status, respnse.message, time.time() - t)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_text2img_{i}_{time.time()}.jpg')


@async_infer
def run_img2img_asyn():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    img_path = "/workspace/mnt/storage/yankai/openimage/stable-diffusion-webui/00318-297029471.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    mask_path = "/workspace/mnt/storage/yankai/openimage/stable-diffusion-webui/mask.png"
    with open(mask_path,'rb') as f:
        mask_base64 = base64.b64encode(f.read())

    request = sd_pb2.SdImg2ImgRequest(
        base64_images = [image_base64],
        mask = mask_base64,
        prompt = "shirt, yellow",
        negative_prompt = None,
        width = 1024,
        height = 1024,
        seed = -1,
        steps = 20,
        batch_size = 4)
    respnse = client.img2img_asyn(request)
    task_id = None
    if respnse.message == "success":
        task_id = respnse.task_id
    print(respnse.status, respnse.message)
    
    request = sd_pb2.SdQueryRequest(task_id = task_id)
    while True:
        time.sleep(1)
        respnse = client.query(request)
        print(respnse.status, respnse.message)
        if respnse.message == "success"  or respnse.status == 500:
            break
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_img2img_{i}_{time.time()}.jpg')

@async_infer
def run_img2img():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/00318-297029471.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    mask_path = "/root/stable-diffusion-webui/mask.png"
    with open(mask_path,'rb') as f:
        mask_base64 = base64.b64encode(f.read())

    request = sd_pb2.SdImg2ImgRequest(
        base64_images = [image_base64],
        mask = None,
        prompt = "<lora:LCM_LoRA_Weights_SD15:1>,clothes,yellow pocket",
        negative_prompt = None,
        width = 512,
        height = 512,
        seed = -1,
        steps = 5,
        batch_size = 4,
        cfg_scale = 1.5,
        )
    respnse = client.img2img(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_inpaint_{i}_{time.time()}.jpg')

def run_img2img_engine():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/workspace/mnt/storage/yankai/openimage/stable-diffusion-webui/00318-297029471.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    mask_path = "/workspace/mnt/storage/yankai/openimage/stable-diffusion-webui/mask_test.png"
    with open(mask_path,'rb') as f:
        mask_base64 = base64.b64encode(f.read())
    
    request = sd_pb2.SdImg2ImgRequest(
        base64_images = [image_base64],
        mask = None,
        prompt = "clothes,yellow pocket",
        negative_prompt = None,
        width = 1024,
        height = 1024,
        seed = 482283685,
        steps = 20,
        batch_size = 1)
    respnse = client.img2img(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_img2img_{i}_{time.time()}.jpg')
        
@async_infer        
def run_upscale():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                                 options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ])
    
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/00318-297029471.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdUpscaleRequest(
        base64_image = image_base64,
        upscaling_resize=4,
        )
    respnse = client.upscale(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_upscale_{i}_{time.time()}.jpg')
    
@async_infer
def run_upscale_asyn():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                                 options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    img_path = "/workspace/mnt/storage/yankai/openimage/stable-diffusion-webui/00318-297029471.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdUpscaleRequest(
        base64_image = image_base64
        )
    respnse = client.upscale_asyn(request)
    task_id = None
    if respnse.message == "success":
        task_id = respnse.task_id
    print(respnse.status, respnse.message)
    
    request = sd_pb2.SdQueryRequest(task_id = task_id)
    while True:
        time.sleep(1)
        respnse = client.query(request)
        print(respnse.status, respnse.message)
        if respnse.message == "success" or respnse.status == 500:
            break
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_upscale_{i}_{time.time()}.jpg')
        
def run_upscale_engine():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    img_path = "/workspace/mnt/storage/yankai/openimage/stable-diffusion-webui/ori_273278,d68300006a065702.jpg"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    request = sd_pb2.SdUpscaleRequest(
        base64_image = image_base64
        )
    
    respnse = client.upscale(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_upscale_{i}_{time.time()}.jpg')

def run_imgfuse_engine():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/workspace/mnt/storage/yankai/openimage/debug/stable-diffusion-webui/6b9a3275df244d37aefc100009151303.jpg"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    img_fuse_path = "/workspace/mnt/storage/yankai/openimage/debug/stable-diffusion-webui/buliao.png"
    with open(img_fuse_path,'rb') as f:
        image_base64_fuse = base64.b64encode(f.read())
    mask_path = "/workspace/mnt/storage/yankai/openimage/stable-diffusion-webui/mask_test.png"
    with open(mask_path,'rb') as f:
        mask_base64 = base64.b64encode(f.read())
    
    request = sd_pb2.SdFuseRequest(
        base64_images = [image_base64, image_base64_fuse],
        prompt = "<lora:mj_v1:0.4>,<lora:clothes_v1:0.8>,<lora:add_detail:0.5>,<lora:invisible:1>,mjstyle,",
        negative_prompt = None,
        width = 512,
        height = 512,
        seed = -1,
        steps = 20,
        batch_size = 4,
        denoising_strength = 0.5)
    respnse = client.fuse(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_fuse_{i}_{time.time()}.jpg')

@async_infer
def run_imgfuse():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/00318-297029471.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    fuse_path = "/root/stable-diffusion-webui/1694767484522_7bb27b0d-7777-47b9-b34d-8b9f672a086a.png"
    with open(fuse_path,'rb') as f:
        fuse_base64 = base64.b64encode(f.read())

    request = sd_pb2.SdImgFuseRequest(
        base64_images = [image_base64, fuse_base64],
        prompt = "",
        negative_prompt = None,
        width = 1024,
        height = 1024,
        seed = -1,
        steps = 20,
        batch_size = 4,
        denoising_strength = 0.5
        )
    respnse = client.imgfuse(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_fuse_{i}_{time.time()}.jpg')


@async_infer
def run_ctrl2img():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    # client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/0fd475db-502a-4d53-a7d8-043e9c6b971a.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdCtrl2ImgRequest(
        base64_image = image_base64,
        perference = "BALANCED",
        prompt = "<lora:mj_3k_clean:0.8>,<lora:clothes_v1:0.8>,<lora:invisible:1>,mjstyle,",
        negative_prompt = "",
        width = 512,
        height = 512,
        seed = -1,
        steps = 20,
        batch_size = 4,
        enable_hr = True,
        hr_scale = 2,
        hr_upscaler = "R-ESRGAN 4x+"
        )
    respnse = client.ctrl2img(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_ctrl2img_{i}_{time.time()}.jpg')

def run_ctrl2img_engine():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    # client = sd_pb2_grpc.SdServiceStub(channel=conn)
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/0fd475db-502a-4d53-a7d8-043e9c6b971a.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdCtrl2ImgRequest(
        base64_image = image_base64,
        perference = "BALANCED",
        prompt = "<lora:mj_3k_clean:0.8>,<lora:clothes_v1:0.8>,<lora:invisible:1>,mjstyle,",
        negative_prompt = "",
        width = 512,
        height = 512,
        seed = -1,
        steps = 25,
        batch_size = 4,
        enable_hr = False,
        hr_scale = 2,
        hr_upscaler = "R-ESRGAN 4x+"
        )
    respnse = client.ctrl2img(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_ctrl2img_{i}_{time.time()}.jpg')

@async_infer
def run_interrogate():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    # client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/0fd475db-502a-4d53-a7d8-043e9c6b971a.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdInterrogateRequest(
        base64_image = image_base64,
        )
    respnse = client.interrogate(request)
    print(respnse.status, respnse.message, respnse.prompt)

def run_interrogate_engine():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    # client = sd_pb2_grpc.SdServiceStub(channel=conn)
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/0fd475db-502a-4d53-a7d8-043e9c6b971a.png"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdInterrogateRequest(
        base64_image = image_base64,
        )
    respnse = client.interrogate(request)
    print(respnse.status, respnse.message, respnse.prompt)

@async_infer        
def run_normalize():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                                 options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ])
    
    client = sd_pb2_grpc.SdServiceStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/7e3ede3df712432b9eb1689f7d7063fc.jpg"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdNormalizeRequest(
        base64_image = image_base64,
        resize = True,
        size = 1024,
        model = "transparent_background",
        threshold = 100,
        )
    respnse = client.normalize(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_normalize_{i}_{time.time()}.png')

def run_normalize_engine():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('127.0.0.1:7860',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    # client = sd_pb2_grpc.SdServiceStub(channel=conn)
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/root/stable-diffusion-webui/6eae70ffe204484dbaf9d50d596ce5b6.jpg"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    request = sd_pb2.SdNormalizeRequest(
        base64_image = image_base64,
        resize = True,
        size = 1024,
        model = "transparent_background",
        threshold = 100,
        )
    respnse = client.normalize(request)
    print(respnse.status, respnse.message)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_normalize_{i}_{time.time()}.png')

                      
if __name__ == '__main__':
    MAX_MESSAGE_LENGTH = 256 * 1024 * 1024
    run_normalize()
    # while True:
    #     time.sleep(1)
    
        
