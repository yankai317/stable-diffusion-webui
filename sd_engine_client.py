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

def run_txt2img():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('localhost:8000',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    request = sd_pb2.SdText2ImgRequest(prompt = "<hypernet:shentu_clothes_0718-100000:1>,quixel,megascans render depth of field 8k hyper quality high resolution realistic details texture details,Fur Jacket,Acrylic fiber,Adjusting buckle,All in one skin,Artificial wool,Atmospheric style,Bright surface,Brown,Brushed fabric,Cashmere wool,Casual,Chiffon,Collegiate style,Commuting style,Cotton,Cotton blend cloth,Cotton-linen blend,Cover the length of your hips,Debutante style,Deep Cowboy,denseness,Down,elasticity,Elegant,European style,Exquisite style,fade,fancy,Fashion,fine and smooth,Flax,fleecing,fluffy,Fresh,front,Gentle,Genuine leather,H-shaped fit,Hemmed hem,Hemp,Hemp-cotton blend,insert pocket,Japanese style,knit,Knitted sweater fabric,Korean style,Lamb wool composite leather,Lamb wool composite small particles,Lamb wool hem,Leather,Light and thin spinning,Long-sleeve,Matte finish,Metal zipper,Mink hair,Mink hair hem,Neckline adjustment clasp,No model,no person,noble,nylon,Off-shoulder,Plush liner,Polar fleece composite leather,polyamide,Polyester fiber,Pure cotton,Pure wool,Raw hem,Satin material,Sense of concavo-convex,Sheepskin,Silk,Silk cotton,Simple style,Skin-friendly,Slightly mature,soft,Soft and glu,",
        negative_prompt = None,
        width = 512,
        height = 512,
        seed = -1,
        steps = 50,
        batch_size = 1,
        enable_hr=True,
        hr_scale = 2,
        hr_upscaler = "R-ESRGAN 4x+"
        )
    respnse = client.text2img(request)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_text2img_{i}_{time.time()}.jpg')

def run_img2img():
    '''
    模拟请求服务方法信息
    :return:
    '''
    conn=grpc.insecure_channel('localhost:8000',
                               options=[ 
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), 
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), 
    ])
    client = sd_pb2_grpc.SdEngineStub(channel=conn)
    img_path = "/data/source/stable-diffusion-webui/ori_273278,d68300006a065702.jpg"
    with open(img_path,'rb') as f:
        image_base64 = base64.b64encode(f.read())
    mask_path = "/data/source/stable-diffusion-webui/mask.png"
    with open(mask_path,'rb') as f:
        mask_base64 = base64.b64encode(f.read())

    request = sd_pb2.SdImg2ImgRequest(
        base64_images = [image_base64],
        mask = mask_base64,
        prompt = "nothing",
        negative_prompt = None,
        width = 512,
        height = 512,
        seed = -1,
        steps = 50,
        batch_size = 1)
    respnse = client.img2img(request)
    for i, img_base64 in enumerate(respnse.base64):
        img = base64_to_image(img_base64)
        img.save(f'result_img2img_{i}_{time.time()}.jpg')

if __name__ == '__main__':
    MAX_MESSAGE_LENGTH = 256 * 1024 * 1024
    run_img2img()
