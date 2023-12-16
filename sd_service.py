import grpc
from proto import sd_pb2, sd_pb2_grpc
from concurrent import futures
from sd_dispatch import SdDispatch
import time
import datetime

class SdService(sd_pb2_grpc.SdServiceServicer):
    '''
    继承GrpcServiceServicer,实现hello方法
    '''
    def __init__(self, max_queue_size, configs):

        self.dispatch = SdDispatch(max_queue_size=100, sd_node_service_configs=configs)

    def text2img(self, request, context):
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 25
        batch_size = request.batch_size if request.batch_size != 0 else 1

        enable_hr = request.enable_hr
        hr_scale = request.hr_scale if request.hr_scale != 0 else 2
        cfg_scale = request.cfg_scale if request.cfg_scale != 0 else 7
        hr_upscaler = request.hr_upscaler if request.hr_upscaler else "R-ESRGAN 4x+"
        disable_default_prompt = request.disable_default_prompt
        default_prompt = "<lora:mj_3k_clean:0.8>,<lora:clothes_v1:0.8>,<lora:invisible:1>,mjstyle," if not disable_default_prompt else ""
        default_negative_prompt = ""
        
        args = {
            "prompt":default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "enable_hr":enable_hr,
            "hr_scale": hr_scale,
            "hr_upscaler":hr_upscaler,
            "cfg_scale": cfg_scale
        }
        
        task_id = self.dispatch.txt2img_in_queue(args)

        print(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, task_type: txt2img, task_id: {task_id}, args: {args}")

        while True:
            time.sleep(0.5)
            task_status = self.dispatch.get_task_status(task_id)
            if task_status == 2 or task_status == -1:
                result = self.dispatch.get_task_result(task_id)
                break
        
        if task_status == 2:
            return sd_pb2.SdResponse(status=result.status, message=result.message, base64=result.base64)
        else:
            return sd_pb2.SdResponse(status=500, message=result.message, base64="")
    
    def img2img(self, request, context):
        base64_images = request.base64_images
        mask = request.mask if request.mask != "" else None
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 25
        batch_size = request.batch_size if request.batch_size != 0 else 1
        denoising_strength = request.denoising_strength if request.denoising_strength != 0 else 0.75
        disable_default_prompt = request.disable_default_prompt
        default_prompt = "<lora:mj_3k_clean:0.8>,<lora:clothes_v1:0.8>,<lora:invisible:1>,mjstyle," if not disable_default_prompt else ""
        default_negative_prompt = ""
        cfg_scale = request.cfg_scale if request.cfg_scale != 0 else 7
        args = {
            "base64_images":base64_images,
            "mask": mask,
            "prompt":default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "denoising_strength":denoising_strength,
            "cfg_scale": cfg_scale
        }
        task_id = self.dispatch.img2img_in_queue(args)
        show_dict = {
            "prompt":default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size
        }
        print(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, task_type: img2img, task_id: {task_id}, args: {show_dict}")
        if mask is None:
            task_id = self.dispatch.img2img_in_queue(args)
        else:
            task_id = self.dispatch.imginpaint_in_queue(args)
            
        while True:
            time.sleep(0.5)
            task_status = self.dispatch.get_task_status(task_id)
            if task_status == 2 or task_status == -1:
                result = self.dispatch.get_task_result(task_id)
                break
        
        if task_status == 2:
            return sd_pb2.SdResponse(status=result.status, message=result.message, base64=result.base64)
        else:
            return sd_pb2.SdResponse(status=500, message=result.message, base64="")

    def upscale(self, request, context):
        base64_image = request.base64_image
        upscaling_resize = request.upscaling_resize if request.upscaling_resize != 0 else 2
        upscaler_1 = request.upscaler_1 if not request.upscaler_1 else "R-ESRGAN 4x+"
        
        args = {
            "base64_image": base64_image,
            "upscaling_resize": upscaling_resize,
            "upscaler_1": upscaler_1
        }
        task_id = self.dispatch.upscale_in_queue(args)
        print(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, task_type: upscale, task_id: {task_id}")
        while True:
            time.sleep(0.5)
            task_status = self.dispatch.get_task_status(task_id)
            if task_status == 2 or task_status == -1:
                result = self.dispatch.get_task_result(task_id)
                break
        if task_status == 2:
            return sd_pb2.SdResponse(status=result.status, message=result.message, base64=result.base64)
        else:
            return sd_pb2.SdResponse(status=500, message=result.message, base64="")
    
    def imgfuse(self, request, context):
        base64_images = request.base64_images
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1
        denoising_strength = request.denoising_strength if request.denoising_strength != 0 else 0.75
        disable_default_prompt = request.disable_default_prompt
        default_prompt = "<lora:mj_3k_clean:0.8>,<lora:clothes_v1:0.8>,<lora:invisible:1>,mjstyle," if not disable_default_prompt else ""
        default_negative_prompt = ""
        
        args = {
            "base64_images":base64_images,
            "prompt":default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "denoising_strength":denoising_strength
        }
        task_id = self.dispatch.imgfuse_in_queue(args)
        show_dict = {
            "prompt":default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size
        }
        print(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, task_type: imgfuse, task_id: {task_id}, args: {show_dict}")
        while True:
            time.sleep(0.5)
            task_status = self.dispatch.get_task_status(task_id)
            if task_status == 2 or task_status == -1:
                result = self.dispatch.get_task_result(task_id)
                break
        if task_status == 2:
            return sd_pb2.SdResponse(status=result.status, message=result.message, base64=result.base64)
        else:
            return sd_pb2.SdResponse(status=500, message=result.message, base64="")

    def ctrl2img(self, request, context):
        base64_image = request.base64_image
        perference = request.perference if request.perference != "" else "BALANCED"
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1

        enable_hr = request.enable_hr
        hr_scale = request.hr_scale if request.hr_scale != 0 else 2
        hr_upscaler = request.hr_upscaler if not request.hr_upscaler else "R-ESRGAN 4x+"

        disable_default_prompt = request.disable_default_prompt
        default_prompt = "<lora:mj_3k_clean:0.8>,<lora:clothes_v1:0.8>,<lora:invisible:1>,mjstyle," if not disable_default_prompt else ""
        default_negative_prompt = ""
        
        args = {
            "base64_image":base64_image,
            "perference": perference,
            "prompt": default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "enable_hr":enable_hr,
            "hr_scale": hr_scale,
            "hr_upscaler":hr_upscaler
        }
        
        show_dict = {
            "perference": perference,
            "prompt": default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "enable_hr":enable_hr,
            "hr_scale": hr_scale,
            "hr_upscaler":hr_upscaler
        }
        task_id = self.dispatch.ctrl2img_in_queue(args)
        print(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, task_type: ctrl2img, task_id: {task_id}, args: {show_dict}")
        while True:
            time.sleep(0.5)
            task_status = self.dispatch.get_task_status(task_id)
            if task_status == 2 or task_status == -1:
                result = self.dispatch.get_task_result(task_id)
                break
            
        if task_status == 2:
            return sd_pb2.SdResponse(status=result.status, message=result.message, base64=result.base64)
        else:
            return sd_pb2.SdResponse(status=500, message=result.message, base64="")
        
    def text2img_asyn(self, request, context):
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 25
        batch_size = request.batch_size if request.batch_size != 0 else 1

        enable_hr = request.enable_hr
        hr_scale = request.hr_scale if request.hr_scale != 0 else 2
        hr_upscaler = request.hr_upscaler if not request.hr_upscaler else "R-ESRGAN 4x+"
        default_prompt = "<lora:mj_3k_clean:0.8>,<lora:clothes_v1:0.8>,<lora:invisible:1>,mjstyle,"
        default_negative_prompt = ""
        
        args = {
            "prompt": default_prompt + prompt,
            "negative_prompt": default_negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "enable_hr":enable_hr,
            "hr_scale": hr_scale,
            "hr_upscaler":hr_upscaler
        }
        try:
            task_id = self.dispatch.txt2img_in_queue(args)
            return sd_pb2.SdAsynTaskResponse(status=200, message="success", task_id=task_id)
        except Exception as e:
            return sd_pb2.SdAsynTaskResponse(status=500, message=e.__str__(), task_id="")

    def img2img_asyn(self, request, context):
        base64_images = request.base64_images
        mask = request.mask if request.mask != "" else None
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1
        denoising_strength = request.denoising_strength if request.denoising_strength != 0 else 0.75
        args = {
            "base64_images":base64_images,
            "mask": mask,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "denoising_strength":denoising_strength
        }
        try:
            task_id = self.dispatch.img2img_in_queue(args)
            return sd_pb2.SdAsynTaskResponse(status=200, message="success", task_id=task_id)
        except Exception as e:
            return sd_pb2.SdAsynTaskResponse(status=500, message=e.__str__(), task_id="")

    def upscale_asyn(self, request, context):
        base64_image = request.base64_image
        upscaling_resize = request.upscaling_resize if request.upscaling_resize != 0 else 2
        upscaler_1 = request.upscaler_1 if not request.upscaler_1 else "R-ESRGAN 4x+"
        
        args = {
            "base64_image": base64_image,
            "upscaling_resize": upscaling_resize,
            "upscaler_1": upscaler_1
        }
        try:
            task_id = self.dispatch.upscale_in_queue(args)
            return sd_pb2.SdAsynTaskResponse(status=200, message="success", task_id=task_id)
        except Exception as e:
            return sd_pb2.SdAsynTaskResponse(status=500, message=e.__str__(), task_id="")
    
    def imgfuse_asyn(self, request, context):
        base64_images = request.base64_images
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1
        denoising_strength = request.denoising_strength if request.denoising_strength != 0 else 0.75
        
        args = {
            "base64_images":base64_images,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "denoising_strength":denoising_strength
        }
        try:
            task_id = self.dispatch.imgfuse_in_queue(args)
            return sd_pb2.SdAsynTaskResponse(status=200, message="success", task_id=task_id)
        except Exception as e:
            return sd_pb2.SdAsynTaskResponse(status=500, message=e.__str__(), task_id="")
    
    def ctrl2img_asyn(self, request, context):
        base64_image = request.base64_image
        perference = request.perference if request.perference != "" else "default"
        prompt = request.prompt
        negative_prompt = request.negative_prompt
        width = request.width if request.width != 0 else 512
        height = request.height if request.height != 0 else 512
        seed = request.seed if request.seed != 0 else -1
        steps = request.steps if request.steps != 0 else 20
        batch_size = request.batch_size if request.batch_size != 0 else 1

        enable_hr = request.enable_hr
        hr_scale = request.hr_scale if request.hr_scale != 0 else 2
        hr_upscaler = request.hr_upscaler if not request.hr_upscaler else "R-ESRGAN 4x+"

        args = {
            "base64_image":base64_image,
            "perference": perference,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "seed":seed,
            "steps": steps,
            "batch_size":batch_size,
            "enable_hr":enable_hr,
            "hr_scale": hr_scale,
            "hr_upscaler":hr_upscaler
        }
        try:
            task_id = self.dispatch.ctrl2img_in_queue(args)
            return sd_pb2.SdAsynTaskResponse(status=200, message="success", task_id=task_id)
        except Exception as e:
            return sd_pb2.SdAsynTaskResponse(status=500, message=e.__str__(), task_id="")
        
    def query(self, request, context):
        task_id = request.task_id
        task_status = self.dispatch.get_task_status(task_id)
        if task_status is None:
            return sd_pb2.SdResponse(status=500, message="task not exist, please check task id.", 
                                     base64="")
        if task_status == 2 or task_status == -1:
            result = self.dispatch.get_task_result(task_id)
            if task_status == 2:
                return sd_pb2.SdResponse(status=result.status, message=result.message, base64=result.base64)
            else:
                return sd_pb2.SdResponse(status=500, message=result.message, base64="")
        else:
            if task_status == 0:
                return sd_pb2.SdResponse(status=200, message="queueing", base64="")
            if task_status == 1:
                return sd_pb2.SdResponse(status=200, message="processing", base64="")
        
def run(configs, host="0.0.0.0", port=7860, max_messave_length=256 * 1024 * 1024,):

    MAX_MESSAGE_LENGTH = max_messave_length
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=[
                ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
    sd_service = SdService(100, configs)
    sd_pb2_grpc.add_SdServiceServicer_to_server(sd_service,server)
    server.add_insecure_port('{}:{}'.format(host, port))
    server.start()
    print("start sd service...")
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    configs = [
        {"host": "127.0.0.1", "port": 8001, "device_id": 0, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_0.txt","err_log_save_path":"logs/log_err_0.txt", "task_type": "general"},
        {"host": "127.0.0.1", "port": 8002, "device_id": 1, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_1.txt","err_log_save_path":"logs/log_err_1.txt", "task_type": "general"},
        {"host": "127.0.0.1", "port": 8003, "device_id": 2, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_2.txt","err_log_save_path":"logs/log_err_2.txt", "task_type": "general"},
        {"host": "127.0.0.1", "port": 8004, "device_id": 3, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_3.txt","err_log_save_path":"logs/log_err_3.txt", "task_type": "general"},
        {"host": "127.0.0.1", "port": 8005, "device_id": 4, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_4.txt","err_log_save_path":"logs/log_err_4.txt", "task_type": "general"},
        # {"host": "127.0.0.1", "port": 8006, "device_id": 5, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_5.txt","err_log_save_path":"logs/log_err_5.txt", "task_type": "txt2img"},
        {"host": "127.0.0.1", "port": 8007, "device_id": 6, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_6.txt","err_log_save_path":"logs/log_err_6.txt", "task_type": "general"},
        {"host": "127.0.0.1", "port": 8008, "device_id": 7, "config_path":"setting_configs/config_7.json","log_save_path":"logs/log_7.txt","err_log_save_path":"logs/log_err_7.txt", "task_type": "inpaint"}
    ]
    run(configs)