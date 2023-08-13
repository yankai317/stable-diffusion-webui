from ultralytics import YOLO
import os.path
import sys
import cv2
import json
import numpy as np
import torch
import glob
import shutil

from segment_anything import sam_model_registry, SamPredictor

sam_checkpoint = "/data/source/stable-diffusion-webui/extensions/sd-webui-segment-anything/models/sam/sam_vit_h_4b8939.pth"
yolo_checkpoint = "/data/source/segment-anything/yolov8n-clothes.pt"
device = "cuda"
model_type = "default"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
sam.mask_threshold = 0
predictor = SamPredictor(sam)

yolov8n_predictor = YOLO(yolo_checkpoint)

img_dir = "/data/images/clothes_0805/"
out_dir = "/data/images/segment_0805_expand_with_hd/"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

img_paths = glob.glob(os.path.join(img_dir, "*.png")) + glob.glob(os.path.join(img_dir, "*.jpg")) + \
      glob.glob(os.path.join(img_dir, "*.jpeg")) + glob.glob(os.path.join(img_dir, "*.bmp"))

for i, img_path in enumerate(img_paths):
        print(i, img_path)
        file_name = img_path.split('/')[-1]
        txt_file_name = img_path.replace('.jpg', '.txt').replace('.bmp', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt').replace('.bmp', '.txt')
        save_path = os.path.join(out_dir, file_name.replace('.jpg', '.png').replace('.bmp', '.png').replace('.jpeg', '.png'))
        txt_save_path = os.path.join(out_dir, file_name.replace('.jpg', '.txt').replace('.png', '.txt').replace('.bmp', '.txt').replace('.jpeg', '.txt'))
        if os.path.exists(save_path):
             continue
        try:
            results = yolov8n_predictor(img_path)
        except:
             continue
        image = results[0].orig_img
        boxes = results[0].boxes.xyxy
        if len(boxes) == 0:
            continue
        x_min, y_min, x_max, y_max, = int(boxes[0][0]), int(boxes[0][1]),int(boxes[0][2]),int(boxes[0][3])
        cx = (x_min + x_max) // 2
        cy = (y_min + y_max) // 2

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        predictor.set_image(image_rgb)
        input_boxes = []
        input_boxes.append(np.array([x_min, y_min,x_max,y_max]))
        input_boxes = torch.from_numpy(np.stack(input_boxes ,axis=0)).to(predictor.device)
        transformed_boxes = predictor.transform.apply_boxes_torch(input_boxes, image.shape[:2])
        addition_points = np.stack(np.array([[cx, cy], [0,0]]), axis=0)
        addition_points_labels = np.ones_like(addition_points)[..., 0]
        addition_points_labels[1] = -1
        addition_points =  torch.from_numpy(addition_points).to(predictor.device)[None]

        addition_points_labels =  torch.from_numpy(addition_points_labels).to(predictor.device)[None]

        masks, _, _ = predictor.predict_torch(
            point_coords=None,
            point_labels=None,
            boxes=transformed_boxes,
            mask_input=None,
            multimask_output=False
        )
        mask_np = masks[0][0].cpu().numpy().astype(np.uint8)
        # mask_np = cv2.erode(mask_np, np.ones((5, 5), np.uint8), iterations=3)
        # mask_np = cv2.dilate(mask_np, np.ones((5, 5), np.uint8), iterations=3)
        # mask_np = cv2.dilate(mask_np, np.ones((3, 3), np.uint8), iterations=1)
        contours, hierarchy = cv2.findContours(mask_np, cv2.RETR_EXTERNAL,
                                              cv2.CHAIN_APPROX_TC89_L1)
        img_mask = cv2.fillPoly(mask_np, contours, (1))
        nonzero = np.nonzero(img_mask)
        # mask_np = cv2.dilate(mask_np, np.ones((3, 3), np.uint8), iterations=1)
        # mask_np = mask_np > 0
        # masks = [[mask_np]]
        # color_masks = [
        #     np.random.randint(0, 256, (1, 3), dtype=np.uint8)
        #     for _ in range(len([mask_np]))
        # ]
        # for ind, mask in enumerate(masks):
        #     mask_np = mask[0]
        #     image[mask_np] = image[mask_np] * 0.5 + np.tile(mask_np[mask_np][..., None], [1, 3]) * 0.5 * color_masks[ind]
        # image = image[...,::-1]
        x_min = nonzero[1].min()
        y_min = nonzero[0].min()

        x_max = nonzero[1].max()
        y_max = nonzero[0].max()

        # img_mask = np.stack([img_mask, img_mask, img_mask], axis=-1)

        image[img_mask == 0, ...] = 255
        image_crop = image[y_min:y_max, x_min:x_max]
        img_mask = img_mask[y_min:y_max, x_min:x_max]

        long_edge = max(x_max - x_min, y_max - y_min)
        short_edge = min(x_max - x_min, y_max - y_min)
        left_pad = (long_edge - (x_max - x_min)) // 2
        top_pad = (long_edge - (y_max - y_min)) // 2

        expand_long_edge = int(long_edge * 1.1)
        expand_pixel = (expand_long_edge - long_edge) // 2
        top_pad += expand_pixel
        left_pad += expand_pixel
        new_image = np.ones([expand_long_edge , expand_long_edge , 4]) * 255

        new_image[ top_pad:top_pad + (y_max - y_min), left_pad: left_pad+ (x_max - x_min),:3] = image_crop
        # new_image[ top_pad:top_pad + (y_max - y_min), left_pad: left_pad+ (x_max - x_min), 3] = img_mask*255
        # cv2.imwrite(os.path.join(out_dir,'mask_' + file_name.replace('.jpg', '.png').replace('.bmp', '.png').replace('.jpeg','.png')),img_mask*255)
        # image = cv2.rectangle(image, (bboxes_x, bboxes_y), (bboxes_x +bboxes_width, bboxes_y + bboxes_height), color=(0,255,0), thickness=1 )
        new_image = cv2.resize(new_image, (512,512))
        cv2.imwrite(save_path, new_image)
        if (os.path.getsize(save_path) < 1024 * 150):
            os.remove(save_path)
            continue
        if (short_edge > 512 and os.path.getsize(img_path) > 1024 * 250):
            with open(txt_file_name, "r") as txt_read:
                with open(txt_save_path, "w") as txt_wirte:
                    ori_label = txt_read.readlines()
                    txt_wirte.writelines(ori_label[0] + ", hd")
        else:
            shutil.copy(txt_file_name, txt_save_path)