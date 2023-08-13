package org.example;
import grpc.SdClient;

import java.util.ArrayList;
import java.util.List;
import tools.ImageUtil;

public class Main {
    public static void main(String[] args) {
        SdClient client = new SdClient("127.0.0.1", 7860);
        List<String> base64s_text2img = client.text2img("cat", "", 1, 512, 512, -1, 20, true, 2.0F, "R-ESRGAN 4x+");
        ImageUtil.convertBase64StrToImage(base64s_text2img.get(0), "text2img.jpg");


        String img_path = "C:\\Users\\28964\\source\\sd_grpc\\ori_273278,d68300006a065702.jpg";
        String mask_path = "C:\\Users\\28964\\source\\sd_grpc\\mask.png";
        ArrayList <String> base64s_img = new ArrayList<String>();
        base64s_img.add(ImageUtil.convertImageToBase64Str(img_path));
        String mask = ImageUtil.convertImageToBase64Str(mask_path);
        List<String> base64s_img2img = client.img2img(base64s_img, mask, "nothing", "", 1, 512, 512, -1, 20);

        ImageUtil.convertBase64StrToImage(base64s_img2img.get(0), "img2img.jpg");
    }
}