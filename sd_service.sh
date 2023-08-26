cd /root/stable-diffusion-webui
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./proto/sd.proto
python sd_service.py --port 7860 --xformers --listen
tail -f /dev/null