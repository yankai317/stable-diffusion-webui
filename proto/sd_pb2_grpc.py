# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import sd_pb2 as proto_dot_sd__pb2


class SdServiceStub(object):
    """定义服务接口
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.text2img = channel.unary_unary(
                '/SdService/text2img',
                request_serializer=proto_dot_sd__pb2.SdText2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.img2img = channel.unary_unary(
                '/SdService/img2img',
                request_serializer=proto_dot_sd__pb2.SdImg2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.upscale = channel.unary_unary(
                '/SdService/upscale',
                request_serializer=proto_dot_sd__pb2.SdUpscaleRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.imgfuse = channel.unary_unary(
                '/SdService/imgfuse',
                request_serializer=proto_dot_sd__pb2.SdImgFuseRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.ctrl2img = channel.unary_unary(
                '/SdService/ctrl2img',
                request_serializer=proto_dot_sd__pb2.SdCtrl2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.text2img_asyn = channel.unary_unary(
                '/SdService/text2img_asyn',
                request_serializer=proto_dot_sd__pb2.SdText2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
                )
        self.img2img_asyn = channel.unary_unary(
                '/SdService/img2img_asyn',
                request_serializer=proto_dot_sd__pb2.SdImg2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
                )
        self.upscale_asyn = channel.unary_unary(
                '/SdService/upscale_asyn',
                request_serializer=proto_dot_sd__pb2.SdUpscaleRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
                )
        self.imgfuse_asyn = channel.unary_unary(
                '/SdService/imgfuse_asyn',
                request_serializer=proto_dot_sd__pb2.SdImgFuseRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
                )
        self.ctrl2img_asyn = channel.unary_unary(
                '/SdService/ctrl2img_asyn',
                request_serializer=proto_dot_sd__pb2.SdCtrl2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
                )
        self.query = channel.unary_unary(
                '/SdService/query',
                request_serializer=proto_dot_sd__pb2.SdQueryRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )


class SdServiceServicer(object):
    """定义服务接口
    """

    def text2img(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def img2img(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upscale(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def imgfuse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ctrl2img(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def text2img_asyn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def img2img_asyn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upscale_asyn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def imgfuse_asyn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ctrl2img_asyn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SdServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'text2img': grpc.unary_unary_rpc_method_handler(
                    servicer.text2img,
                    request_deserializer=proto_dot_sd__pb2.SdText2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'img2img': grpc.unary_unary_rpc_method_handler(
                    servicer.img2img,
                    request_deserializer=proto_dot_sd__pb2.SdImg2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'upscale': grpc.unary_unary_rpc_method_handler(
                    servicer.upscale,
                    request_deserializer=proto_dot_sd__pb2.SdUpscaleRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'imgfuse': grpc.unary_unary_rpc_method_handler(
                    servicer.imgfuse,
                    request_deserializer=proto_dot_sd__pb2.SdImgFuseRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'ctrl2img': grpc.unary_unary_rpc_method_handler(
                    servicer.ctrl2img,
                    request_deserializer=proto_dot_sd__pb2.SdCtrl2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'text2img_asyn': grpc.unary_unary_rpc_method_handler(
                    servicer.text2img_asyn,
                    request_deserializer=proto_dot_sd__pb2.SdText2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdAsynTaskResponse.SerializeToString,
            ),
            'img2img_asyn': grpc.unary_unary_rpc_method_handler(
                    servicer.img2img_asyn,
                    request_deserializer=proto_dot_sd__pb2.SdImg2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdAsynTaskResponse.SerializeToString,
            ),
            'upscale_asyn': grpc.unary_unary_rpc_method_handler(
                    servicer.upscale_asyn,
                    request_deserializer=proto_dot_sd__pb2.SdUpscaleRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdAsynTaskResponse.SerializeToString,
            ),
            'imgfuse_asyn': grpc.unary_unary_rpc_method_handler(
                    servicer.imgfuse_asyn,
                    request_deserializer=proto_dot_sd__pb2.SdImgFuseRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdAsynTaskResponse.SerializeToString,
            ),
            'ctrl2img_asyn': grpc.unary_unary_rpc_method_handler(
                    servicer.ctrl2img_asyn,
                    request_deserializer=proto_dot_sd__pb2.SdCtrl2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdAsynTaskResponse.SerializeToString,
            ),
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=proto_dot_sd__pb2.SdQueryRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SdService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SdService(object):
    """定义服务接口
    """

    @staticmethod
    def text2img(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/text2img',
            proto_dot_sd__pb2.SdText2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def img2img(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/img2img',
            proto_dot_sd__pb2.SdImg2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upscale(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/upscale',
            proto_dot_sd__pb2.SdUpscaleRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def imgfuse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/imgfuse',
            proto_dot_sd__pb2.SdImgFuseRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ctrl2img(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/ctrl2img',
            proto_dot_sd__pb2.SdCtrl2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def text2img_asyn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/text2img_asyn',
            proto_dot_sd__pb2.SdText2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def img2img_asyn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/img2img_asyn',
            proto_dot_sd__pb2.SdImg2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upscale_asyn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/upscale_asyn',
            proto_dot_sd__pb2.SdUpscaleRequest.SerializeToString,
            proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def imgfuse_asyn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/imgfuse_asyn',
            proto_dot_sd__pb2.SdImgFuseRequest.SerializeToString,
            proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ctrl2img_asyn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/ctrl2img_asyn',
            proto_dot_sd__pb2.SdCtrl2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdAsynTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdService/query',
            proto_dot_sd__pb2.SdQueryRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SdEngineStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.text2img = channel.unary_unary(
                '/SdEngine/text2img',
                request_serializer=proto_dot_sd__pb2.SdText2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.img2img = channel.unary_unary(
                '/SdEngine/img2img',
                request_serializer=proto_dot_sd__pb2.SdImg2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.upscale = channel.unary_unary(
                '/SdEngine/upscale',
                request_serializer=proto_dot_sd__pb2.SdUpscaleRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.imgfuse = channel.unary_unary(
                '/SdEngine/imgfuse',
                request_serializer=proto_dot_sd__pb2.SdImgFuseRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )
        self.ctrl2img = channel.unary_unary(
                '/SdEngine/ctrl2img',
                request_serializer=proto_dot_sd__pb2.SdCtrl2ImgRequest.SerializeToString,
                response_deserializer=proto_dot_sd__pb2.SdResponse.FromString,
                )


class SdEngineServicer(object):
    """Missing associated documentation comment in .proto file."""

    def text2img(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def img2img(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upscale(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def imgfuse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ctrl2img(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SdEngineServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'text2img': grpc.unary_unary_rpc_method_handler(
                    servicer.text2img,
                    request_deserializer=proto_dot_sd__pb2.SdText2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'img2img': grpc.unary_unary_rpc_method_handler(
                    servicer.img2img,
                    request_deserializer=proto_dot_sd__pb2.SdImg2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'upscale': grpc.unary_unary_rpc_method_handler(
                    servicer.upscale,
                    request_deserializer=proto_dot_sd__pb2.SdUpscaleRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'imgfuse': grpc.unary_unary_rpc_method_handler(
                    servicer.imgfuse,
                    request_deserializer=proto_dot_sd__pb2.SdImgFuseRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
            'ctrl2img': grpc.unary_unary_rpc_method_handler(
                    servicer.ctrl2img,
                    request_deserializer=proto_dot_sd__pb2.SdCtrl2ImgRequest.FromString,
                    response_serializer=proto_dot_sd__pb2.SdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SdEngine', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SdEngine(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def text2img(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdEngine/text2img',
            proto_dot_sd__pb2.SdText2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def img2img(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdEngine/img2img',
            proto_dot_sd__pb2.SdImg2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upscale(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdEngine/upscale',
            proto_dot_sd__pb2.SdUpscaleRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def imgfuse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdEngine/imgfuse',
            proto_dot_sd__pb2.SdImgFuseRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ctrl2img(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SdEngine/ctrl2img',
            proto_dot_sd__pb2.SdCtrl2ImgRequest.SerializeToString,
            proto_dot_sd__pb2.SdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
