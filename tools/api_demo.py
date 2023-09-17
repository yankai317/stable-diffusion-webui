import requests
import json
import base64
from PIL import Image
from io import BytesIO

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

def base64_to_image(base64_str):  # 用 b.show()可以展示
    image = base64.b64decode(base64_str, altchars=None, validate=False)
    image = BytesIO(image)
    image = Image.open(image)
    return image

# img_path = "/data/source/stable-diffusion-webui/ori_273278,d68300006a065702.jpg"
# with open(img_path,'rb') as f:
#     image_base64 = base64.b64encode(f.read())
# mask_path = "/data/source/stable-diffusion-webui/mask.png"
# with open(mask_path,'rb') as f:
#     mask_base64 = base64.b64encode(f.read())
    
payload = json.dumps({
    "prompt":"<hypernet:jiangyi_v0-100000-200000-320000:1>,<lora:OLD_oneitemV1:0.8>,<lora:add_detail:0.8>,[(white background:0.5),::5],(volumetric lighting:1.2),(8k,hdr,hd:1.1),(sharp focus:1.2),(oneitem:1.2),(simple_background:1.2),mid-shot,post-processing,extremely hyperdetailed,concept art,dress,colorful,summer,Chinese dragon pattern",
    "negative_prompt":"(worst quality:2),(low quality:2),(normal quality:2),overexposure,easynegative",
    "batch_size":1,
    "steps": 20,
    "width": 512,
    "height": 512,
    "sampler_index": "Euler",
    # "init_images": [image_base64.decode()],
    # "mask": mask_base64.decode()
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
import time
base64s = json.loads(response.text)['images']
for i, img_base64 in enumerate(base64s):
    img = base64_to_image(img_base64)
    img.save(f'result_text2img_{i}_{time.time()}.jpg')