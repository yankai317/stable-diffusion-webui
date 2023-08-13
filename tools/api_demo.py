import requests
import json
import base64
from PIL import Image
from io import BytesIO

url = "http://192.168.0.107:7860/sdapi/v1/img2img"

def base64_to_image(base64_str):  # 用 b.show()可以展示
    image = base64.b64decode(base64_str, altchars=None, validate=False)
    image = BytesIO(image)
    image = Image.open(image)
    return image

img_path = "/data/source/stable-diffusion-webui/ori_273278,d68300006a065702.jpg"
with open(img_path,'rb') as f:
    image_base64 = base64.b64encode(f.read())
mask_path = "/data/source/stable-diffusion-webui/mask.png"
with open(mask_path,'rb') as f:
    mask_base64 = base64.b64encode(f.read())
    
payload = json.dumps({
    "prompt":"",
    "negative_prompt":"",
    "batch_size":1,
    "steps": 20,
    "width": 512,
    "height": 512,
    "sampler_index": "Euler",
    "init_images": [image_base64.decode()],
    "mask": mask_base64.decode()
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

import pdb;pdb.set_trace()
print(response.text)