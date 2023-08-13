import json
import cv2
import os
import glob
import shutil
import requests
import time

# download data and get txt label
save_path = "/data/images/clothes_0805/"
json_path = "/data/source/stable-diffusion-webui/data_0805.json"
type_list = ['小香风套装','衬衫裙','针织连衣裙','针织马甲','男生羽绒服','羽绒服', '连衣裙', '工装裤', '牛仔外套', '羽绒夹克', '夹克', '棉服', '羽绒马甲', '童装羽绒服', '皮革外套', '羽绒背夹', '棉衣', '羽绒背心', '风衣', '大衣', '派克服', '羽绒服背心', '外套', '羽绒服连衣裙', '羽绒服外套', '羽绒绒', '羊羔毛外套', '羊羔毛羽绒服', '童装外套', '卫衣', '衬衫', '服饰', '呢料外套', '皮毛一体外套', '羽绒服男士', '男士羽绒服', '衬衫 ', '皮衣', '针织衫', '羽绒外套', '羽绒服半身裙', 'Polo衫', 'polo衫', '毛衣', '童装', '裤子', '男士大衣', '棒球服', '西装', '香风夹克', '冲锋衣', '机车服', '背心', '短袖', '针织毛衣', '连帽短袖', '针织背心', '背夹', '半裙', '马甲', '摇粒绒外套', '男士西服', 'POLO衫', '西服', '皮格外套', '男士风衣', '短裤', '裙子', '针织外套', '防晒衣', '长裤', '羽绒服短裤', '羽绒裤子', '短群', '短裙', '牛仔裤', '羽绒服连体裤', '针织', 'Polo', '马甲外套', '长袖', '羊羔绒外套', '小香风外套', '吊带', '童装裙', '长裙', '女装', '男装', '七分裤', '外套马甲', '连体裤', '背带裤', '衬衣', '开衫', '女装羽绒服', '打底衫', '针织卫衣', '羊毛衫', '皮毛一体', '羊羔绒外套']
eng_type_list = ['chanel style set','Shirt dress','Knit Dress','Knit vest','Boys down jacket','down jacket', 'dress', 'Cargo pants', 'denim jacket', 'down jacket', 'jacket', 'padded jacket', 'down vest', 'children down jacket', 'leather jacket', 'down back clip', 'cotton coat', 'down vest', 'windbreaker', 'coat', 'parker', 'down vest', 'jacket', 'down dress', 'down jacket', 'down', ' Lamb Wool Jacket', 'Lamb Wool Down Jacket', 'Kids Jacket', 'Sweater', 'Shirt', 'Apparel', 'Wool Jacket', 'Fur Jacket', 'Men Down Jacket', 'Men Down Jacket', 'Shirt', 'leather', 'knitwear', 'down jacket', 'down jacket skirt', 'Polo shirt', 'polo shirt', 'sweater', 'children clothing', 'pants', 'men coat' , 'baseball uniform', 'suit', 'fragrant jacket', 'jacket', 'bike suit', 'vest', 'short sleeve', 'knitted sweater', 'hooded short sleeve', 'knitted vest' , 'Back clip', 'Skirt', 'Vest', 'Polar fleece jacket', 'Men suit', 'POLO shirt', 'Suit', 'Pig coat', 'Men trench coat', 'Shorts' , 'skirt', 'knit jacket', 'sun protection clothing', 'trousers', 'down jacket shorts', 'down pants', 'short group', 'skirt', 'jeans', 'down jacket jumpsuit' , 'knitting', 'Polo', 'vest jacket', 'long sleeves', 'sherpa jacket', 'chanel style jacket', 'sling', 'children dress', 'long skirt', 'women clothing', 'Men', 'cropped pants', 'coat vest', 'romper', 'overalls', 'shirt', 'cardigan', 'women down jacket', 'bottoming shirt', 'knitted sweater', 'Sweater', 'Fur One', 'Sherpa fleece jacket']

if not os.path.exists(save_path):
    os.makedirs(save_path)

with open(json_path, "r") as json_read:
    imgs_json = json.load(json_read)
    for i, img_json in enumerate(imgs_json):
        # if not "纯色背景" in img_json['promptChn'] or not "纯色背景" in img_json['promptChn']:
        #     continue
        attrs_str = img_json['promptEn']
        try:
            attrs_str = eng_type_list[type_list.index(img_json['name'].replace("·","").replace(" ","").replace("小香外套","小香风外套").replace("夹克外套","夹克"))] + ',' + attrs_str
        except:
            continue
        url = img_json['url']
        file_name = url.split('/')[-1]
        if os.path.exists(save_path+file_name):
            print('num {} has existed'.format(i))
        else:
            headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                }

            with open(save_path+file_name,'wb') as f:
                img = requests.get(url,headers = headers).content
                #url是img的url
                f.write(img)
                time.sleep(0.3)
        txt_name = file_name.replace('.png','.txt').replace('.jpg','.txt').replace('.bmp','.txt').replace('.jpeg','.txt').replace('.JPG','.txt').replace('.JPEG','.txt')
        with open(save_path+txt_name,'w') as f:
            f.writelines(attrs_str.replace(",Man","").replace(",Woman",""))
        print('{}: download done{}'.format(i, save_path+file_name))
        