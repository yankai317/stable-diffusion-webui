from sd_handler import SdServiceHandler, SdClientHandler
from queue import Queue
from threading import Thread
import uuid
import time

            
def async_infer(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
    
class SdDispatch(object):
    def __init__(self, max_queue_size=100, sd_node_service_configs = []) -> None:
        self.sd_service_txt2img_handlers = []
        self.sd_client_txt2img_handlers = []
        
        self.sd_service_img2img_handlers = []
        self.sd_client_img2img_handlers = []
        
        self.txt2img_task_queue = Queue()
        self.img2img_task_queue = Queue()
        self.task_status = {}
        self.task_timest = {}
        self.results = {}
        self.max_queue_size = max_queue_size
        
        for sd_node_service_config in sd_node_service_configs:
            host = sd_node_service_config['host']
            port = sd_node_service_config['port']
            device_id = sd_node_service_config['device_id']
            config_path = sd_node_service_config['config_path']
            log_save_path = sd_node_service_config['log_save_path']
            err_log_save_path = sd_node_service_config['err_log_save_path']
            task_type = sd_node_service_config['task_type']
            
            sd_service_handler = SdServiceHandler(host=host, port=port, device_id=device_id, config_path=config_path, log_save_path=log_save_path,err_log_save_path=err_log_save_path )
            sd_client_handler = SdClientHandler(host=host, port=port)
            if task_type == "txt2img":
                self.sd_service_txt2img_handlers.append(sd_service_handler)
                self.sd_client_txt2img_handlers.append(sd_client_handler)
            if task_type == "img2img":
                self.sd_service_img2img_handlers.append(sd_service_handler)
                self.sd_client_img2img_handlers.append(sd_client_handler)
                
        self.txt2img_dispatch()
        self.img2img_dispatch()
        self.clean_timeout_result()
        
    def get_task_status(self, task_id):
        if task_id in self.task_status.keys():
            return self.task_status[task_id]
        else:
            return None
        
    def get_task_result(self, task_id):
        if self.task_status[task_id] == 2 or self.task_status[task_id] == -1:
            result = self.results[task_id]
            self.results.pop(task_id)
            self.task_timest.pop(task_id)
            self.task_status.pop(task_id)
            return result
        else:
            return None
        
    # txt2img
    def txt2img_in_queue(self, args):
        task_id = str(uuid.uuid1())
        data = {"task_id": task_id, "args": args}
        while True:
            time.sleep(1)
            if self.txt2img_task_queue.qsize() < self.max_queue_size:
                self.txt2img_task_queue.put(data)
                self.task_status[task_id] = 0
                return task_id
            
    @async_infer
    def txt2img(self, sd_client_handler, data):
        task_id = data['task_id']
        args = data['args']
        try:
            with sd_client_handler:
                result = sd_client_handler.run_txt2img(args)
            if result.status == 200:
                self.task_status[task_id] = 2
                self.results[task_id] = result
                self.task_timest[task_id] = time.time()
            else:
                self.task_status[task_id] = -1
                self.results[task_id] = result
                self.task_timest[task_id] = time.time()
        except Exception as e:
            self.task_status[task_id] = -1
            self.results[task_id] = e
            self.task_timest[task_id] = time.time()

    
    @async_infer
    def txt2img_dispatch(self):
        while True:
            time.sleep(1)
            for sd_client_handler in self.sd_client_txt2img_handlers:
                if sd_client_handler.isFree and not self.txt2img_task_queue.empty():
                    data = self.txt2img_task_queue.get()
                    self.txt2img(sd_client_handler, data)
                    self.task_status[data['task_id']] = 1
                    
    # img2img
    def img2img_in_queue(self, args):
        task_id = str(uuid.uuid1())
        data = {"task_id": task_id, "args": args}
        while True:
            time.sleep(1)
            if self.img2img_task_queue.qsize() < self.max_queue_size:
                self.img2img_task_queue.put(data)
                self.task_status[task_id] = 0
                return task_id
            
    @async_infer
    def img2img(self, sd_client_handler, data):
        task_id = data['task_id']
        args = data['args']
        try:
            with sd_client_handler:
                result = sd_client_handler.run_img2img(args)
            if result.status == 200:
                self.task_status[task_id] = 2
                self.results[task_id] = result
                self.task_timest[task_id] = time.time()
            else:
                self.task_status[task_id] = -1
                self.results[task_id] = result
                self.task_timest[task_id] = time.time()
        except Exception as e:
            self.task_status[task_id] = -1
            self.results[task_id] = e
            self.task_timest[task_id] = time.time()
    
    @async_infer
    def img2img_dispatch(self):
        while True:
            time.sleep(1)
            for sd_client_handler in self.sd_client_img2img_handlers:
                if sd_client_handler.isFree and not self.img2img_task_queue.empty():
                    data = self.img2img_task_queue.get()
                    self.img2img(sd_client_handler, data)
                    self.task_status[data['task_id']] = 1
                    
    @async_infer
    def clean_timeout_result(self):
        while True:
            time.sleep(2)
            for task_id in list(self.task_timest.keys()):
                timest = self.task_timest[task_id]
                if time.time() - timest > 30:
                    self.results.pop(task_id)
                    self.task_timest.pop(task_id)
                    self.task_status.pop(task_id)
                    
from PIL import Image
import base64
from io import BytesIO
import time
def base64_to_image(base64_str):  # 用 b.show()可以展示
    image = base64.b64decode(base64_str, altchars=None, validate=False)
    image = BytesIO(image)
    image = Image.open(image)
    return image

if __name__ == '__main__':
    configs = [
        {"host": "127.0.0.1", "port": 8000, "device_id": 0, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_1.txt","err_log_save_path":"logs/log_err_1.txt", "task_type": "txt2img"},
        {"host": "127.0.0.1", "port": 8001, "device_id": 1, "config_path":"setting_configs/config_0.json","log_save_path":"logs/log_2.txt","err_log_save_path":"logs/log_err_2.txt", "task_type": "img2img"}
    ]
    sd_dis = SdDispatch(max_queue_size=100, sd_node_service_configs=configs)

    task_num = 4
    task_ids = []
    task_ids_complete = []
    time.sleep(20)
    for i in range(task_num):
        task_ids.append(sd_dis.txt2img_in_queue({"prompt":"car"}))
    
    img_path = "/workspace/mnt/storage/yankai/data/stable-diffusion-webui/ori_273278,d68300006a065702.jpg"
    with open(img_path,'rb') as f:
        base64_images = base64.b64encode(f.read())
    mask_path = "/workspace/mnt/storage/yankai/data/stable-diffusion-webui/mask.png"
    with open(mask_path,'rb') as f:
        mask_base64 = base64.b64encode(f.read())
    for i in range(task_num):
        task_ids.append(sd_dis.img2img_in_queue({"base64_images":[base64_images], "mask":mask_base64}))
        
    