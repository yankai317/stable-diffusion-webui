pip install grpcio
pip install grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./proto/sd.proto
python sd_service.py