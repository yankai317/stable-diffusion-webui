import json
import cv2
import os
import glob
import shutil
import numpy as np
import time
# download data and get txt label
save_path = "/data/images/clothes_0718_npwb_padresize/"
json_path = "/data/data_0718.json"
type_list = ['羽绒服', '连衣裙', '工装裤', '牛仔外套', '羽绒夹克', '夹克', '棉服', '羽绒马甲', '童装羽绒服', '皮革外套', '羽绒背夹', '棉衣', '羽绒背心', '风衣', '大衣', '派克服', '羽绒服背心', '外套', '羽绒服连衣裙', '羽绒服外套', '羽绒绒', '羊羔毛外套', '羊羔毛羽绒服', '童装外套', '卫衣', '衬衫', '服饰', '呢料外套', '皮毛一体外套', '羽绒服男士', '男士羽绒服', '衬衫 ', '皮衣', '针织衫', '羽绒外套', '羽绒服半身裙', 'Polo衫', 'polo衫', '毛衣', '童装', '裤子', '男士大衣', '棒球服', '西装', '香风夹克', '冲锋衣', '机车服', '背心', '短袖', '针织毛衣', '连帽短袖', '针织背心', '背夹', '半裙', '马甲', '摇粒绒外套', '男士西服', 'POLO衫', '西服', '皮格外套', '男士风衣', '短裤', '裙子', '针织外套', '防晒衣', '长裤', '羽绒服短裤', '羽绒裤子', '短群', '短裙', '牛仔裤', '羽绒服连体裤', '针织', 'Polo', '马甲外套', '长袖', '羊羔绒外套', '小香风外套', '吊带', '童装裙', '长裙', '女装', '男装', '七分裤', '外套马甲', '连体裤', '背带裤', '衬衣', '开衫', '女装羽绒服', '打底衫', '针织卫衣', '羊毛衫', '皮毛一体', '羊羔绒外套']
eng_type_list = ['down jacket', 'dress', 'Cargo pants', 'denim jacket', 'down jacket', 'jacket', 'padded jacket', 'down vest', 'children down jacket', 'leather jacket', 'down back clip', 'cotton coat', 'down vest', 'windbreaker', 'coat', 'parker', 'down vest', 'jacket', 'down dress', 'down jacket', 'down', ' Lamb Wool Jacket', 'Lamb Wool Down Jacket', 'Kids Jacket', 'Sweater', 'Shirt', 'Apparel', 'Wool Jacket', 'Fur Jacket', 'Men Down Jacket', 'Men Down Jacket', 'Shirt', 'leather', 'knitwear', 'down jacket', 'down jacket skirt', 'Polo shirt', 'polo shirt', 'sweater', 'children clothing', 'pants', 'men coat' , 'baseball uniform', 'suit', 'fragrant jacket', 'jacket', 'bike suit', 'vest', 'short sleeve', 'knitted sweater', 'hooded short sleeve', 'knitted vest' , 'Back clip', 'Skirt', 'Vest', 'Polar fleece jacket', 'Men suit', 'POLO shirt', 'Suit', 'Pig coat', 'Men trench coat', 'Shorts' , 'skirt', 'knit jacket', 'sun protection clothing', 'trousers', 'down jacket shorts', 'down pants', 'short group', 'skirt', 'jeans', 'down jacket jumpsuit' , 'knitting', 'Polo', 'vest jacket', 'long sleeves', 'sherpa jacket', 'chanel style jacket', 'sling', 'children dress', 'long skirt', 'women clothing', 'Men', 'cropped pants', 'coat vest', 'romper', 'overalls', 'shirt', 'cardigan', 'women down jacket', 'bottoming shirt', 'knitted sweater', 'Sweater', 'Fur One', 'Sherpa fleece jacket']

with open(json_path, "r") as json_read:
    imgs_json = json.load(json_read)
    for i, img_json in enumerate(imgs_json):
        if not "纯色背景" in img_json['promptChn'] or not "纯色背景" in img_json['promptChn']:
            continue
        attrs_str = img_json['promptEn']
        attrs_str = eng_type_list[type_list.index(img_json['name'].replace("·","").replace(" ",""))] + ',' + attrs_str
        url = img_json['url']
        file_name = url.split('/')[-1]
        if os.path.exists(save_path+file_name):
            selected_size = [640, 640]
            img = cv2.imread(save_path+file_name)
            if img is None:
                os.remove(save_path+file_name)
                continue
            im_shape = img.shape
            im_scale = min(selected_size[0] / im_shape[0], selected_size[1] / im_shape[1])
            im_scale_x = im_scale
            im_scale_y = im_scale
            img_left_top_value = img[0, 0, ...]          
            im = np.ones((selected_size[0], selected_size[1], 3),
                                     dtype=np.uint8) * img_left_top_value[None, None]
            resize_img = cv2.resize(
                            img,
                            None,
                            None,
                            fx=im_scale_x,
                            fy=im_scale_y)
            padding_top = (selected_size[0] - resize_img.shape[0]) // 2
            padding_left = (selected_size[1] - resize_img.shape[1]) // 2
            im[padding_top: resize_img.shape[0] + padding_top, padding_left: resize_img.shape[1]+padding_left] = resize_img  
            im = np.ascontiguousarray(im)
            cv2.imwrite(save_path+file_name, im)
            print('using cache')
        else:
            headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                }
            import requests

            with open(save_path+file_name,'wb') as f:
                img = requests.get(url,headers = headers).content
                #url是img的url
                f.write(img)
            selected_size = [640, 640]
            img = cv2.imread(save_path+file_name)
            if img is None:
                os.remove(save_path+file_name)
                continue
            im_shape = img.shape
            im_scale = min(selected_size[0] / im_shape[0], selected_size[1] / im_shape[1])
            im_scale_x = im_scale
            im_scale_y = im_scale
            img_left_top_value = img[0, 0, ...]          
            im = np.ones((selected_size[0], selected_size[1], 3),
                                     dtype=np.uint8) * img_left_top_value[None, None]
            resize_img = cv2.resize(
                            img,
                            None,
                            None,
                            fx=im_scale_x,
                            fy=im_scale_y)
            padding_top = (selected_size[0] - resize_img.shape[0]) // 2
            padding_left = (selected_size[1] - resize_img.shape[1]) // 2
            im[padding_top: resize_img.shape[0] + padding_top, padding_left: resize_img.shape[1]+padding_left] = resize_img     
            im = np.ascontiguousarray(im)
            cv2.imwrite(save_path+file_name, im)
        txt_name = file_name.replace('.png','.txt').replace('.jpg','.txt').replace('.bmp','.txt').replace('.jpeg','.txt').replace('.JPG','.txt').replace('.JPEG','.txt')
        time.sleep(0.5)
        with open(save_path+txt_name,'w') as f:
            f.writelines(attrs_str.replace(",Man","").replace(",Woman","") + ",shentu_clothes_npwb_style")
        print('{}: done{}'.format(i, save_path+file_name))
        
# resize 
        
# data_root = "/data/images/clothes_512_filter"
# txt_root = "/data/images/clothes_512"

# imgs_list = glob.glob(data_root+'/*.png')
# for img_path in imgs_list:
#     img_name = img_path.split('/')[-1]
#     txt_path = os.path.join(txt_root, img_name[8:-4] + '.txt')
#     new_txt_path = os.path.join(data_root, img_name[:-4] + '.txt')
#     shutil.copy(txt_path, new_txt_path)
    # import pdb;pdb.set_trace()
    # break