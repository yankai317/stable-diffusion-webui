cd /data/source/stable-diffusion-webui
source venv/bin/activate
pip install grpcio
pip install grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./proto/sd.proto
python /data/source/stable-diffusion-webui/sd_grpc_server.py