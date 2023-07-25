package grpc;

import grpc.SdServiceGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import proto.Sd;

import java.io.*;
import java.util.Base64;
import java.util.List;
import java.util.UUID;

public class SdClient {
    private final SdServiceGrpc.SdServiceBlockingStub blockingStub;
    private static ManagedChannel managedChannel = null;

    /**
     * @param host gRPC服务的主机名
     * @param port gRPC服务的端口
     */
    public SdClient(String host, int port) {
        managedChannel = ManagedChannelBuilder.forAddress(host, port)
                // 使用非安全机制传输
                .usePlaintext()
                .build();

        blockingStub = SdServiceGrpc.newBlockingStub(managedChannel);
    }

    public List<String> text2img(String prompt, String negative_prompt, int batch_size, int width, int height, int seed, int steps){
        Sd.SdText2ImgRequest request = Sd.SdText2ImgRequest.newBuilder()
                .setPrompt(prompt)
                .setNegativePrompt(negative_prompt)
                .setBatchSize(batch_size)
                .setWidth(width)
                .setHeight(height)
                .setSeed(seed)
                .setSteps(steps)
                .build();
        Sd.SdText2ImgResponse resp = blockingStub.text2img(request);

        return resp.getBase64List();
    }

    public List<String> img2img(List<String> base64_images, String mask_base64, String prompt, String negative_prompt, int batch_size, int width, int height, int seed, int steps) {
        Sd.SdImg2ImgRequest request = Sd.SdImg2ImgRequest.newBuilder()
                .addAllBase64Images(base64_images)
                .setMask(mask_base64)
                .setPrompt(prompt)
                .setNegativePrompt(negative_prompt)
                .setBatchSize(batch_size)
                .setWidth(width)
                .setHeight(height)
                .setSeed(seed)
                .setSteps(steps)
                .build();

        Sd.SdImg2ImgResponse resp = blockingStub.img2img(request);

        return resp.getBase64List();
    }

    public void shutdown() {
        managedChannel.shutdown();
    }
}
