package grpc;
import static io.grpc.MethodDescriptor.generateFullMethodName;
import proto.Sd;
/**
 */
@javax.annotation.Generated(
        value = "by gRPC proto compiler (version 1.56.0)",
        comments = "Source: sd.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class SdEngineGrpc {

  private SdEngineGrpc() {}

  public static final String SERVICE_NAME = "SdEngine";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<Sd.SdText2ImgRequest,
          Sd.SdResponse> getText2imgMethod;

  @io.grpc.stub.annotations.RpcMethod(
          fullMethodName = SERVICE_NAME + '/' + "text2img",
          requestType = Sd.SdText2ImgRequest.class,
          responseType = Sd.SdResponse.class,
          methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<Sd.SdText2ImgRequest,
          Sd.SdResponse> getText2imgMethod() {
    io.grpc.MethodDescriptor<Sd.SdText2ImgRequest, Sd.SdResponse> getText2imgMethod;
    if ((getText2imgMethod = SdEngineGrpc.getText2imgMethod) == null) {
      synchronized (SdEngineGrpc.class) {
        if ((getText2imgMethod = SdEngineGrpc.getText2imgMethod) == null) {
          SdEngineGrpc.getText2imgMethod = getText2imgMethod =
                  io.grpc.MethodDescriptor.<Sd.SdText2ImgRequest, Sd.SdResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "text2img"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdText2ImgRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdEngineMethodDescriptorSupplier("text2img"))
                          .build();
        }
      }
    }
    return getText2imgMethod;
  }

  private static volatile io.grpc.MethodDescriptor<Sd.SdImg2ImgRequest,
          Sd.SdResponse> getImg2imgMethod;

  @io.grpc.stub.annotations.RpcMethod(
          fullMethodName = SERVICE_NAME + '/' + "img2img",
          requestType = Sd.SdImg2ImgRequest.class,
          responseType = Sd.SdResponse.class,
          methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<Sd.SdImg2ImgRequest,
          Sd.SdResponse> getImg2imgMethod() {
    io.grpc.MethodDescriptor<Sd.SdImg2ImgRequest, Sd.SdResponse> getImg2imgMethod;
    if ((getImg2imgMethod = SdEngineGrpc.getImg2imgMethod) == null) {
      synchronized (SdEngineGrpc.class) {
        if ((getImg2imgMethod = SdEngineGrpc.getImg2imgMethod) == null) {
          SdEngineGrpc.getImg2imgMethod = getImg2imgMethod =
                  io.grpc.MethodDescriptor.<Sd.SdImg2ImgRequest, Sd.SdResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "img2img"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdImg2ImgRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdEngineMethodDescriptorSupplier("img2img"))
                          .build();
        }
      }
    }
    return getImg2imgMethod;
  }

  private static volatile io.grpc.MethodDescriptor<Sd.SdUpscaleRequest,
          Sd.SdResponse> getUpscaleMethod;

  @io.grpc.stub.annotations.RpcMethod(
          fullMethodName = SERVICE_NAME + '/' + "upscale",
          requestType = Sd.SdUpscaleRequest.class,
          responseType = Sd.SdResponse.class,
          methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<Sd.SdUpscaleRequest,
          Sd.SdResponse> getUpscaleMethod() {
    io.grpc.MethodDescriptor<Sd.SdUpscaleRequest, Sd.SdResponse> getUpscaleMethod;
    if ((getUpscaleMethod = SdEngineGrpc.getUpscaleMethod) == null) {
      synchronized (SdEngineGrpc.class) {
        if ((getUpscaleMethod = SdEngineGrpc.getUpscaleMethod) == null) {
          SdEngineGrpc.getUpscaleMethod = getUpscaleMethod =
                  io.grpc.MethodDescriptor.<Sd.SdUpscaleRequest, Sd.SdResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "upscale"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdUpscaleRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdEngineMethodDescriptorSupplier("upscale"))
                          .build();
        }
      }
    }
    return getUpscaleMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static SdEngineStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SdEngineStub> factory =
            new io.grpc.stub.AbstractStub.StubFactory<SdEngineStub>() {
              @java.lang.Override
              public SdEngineStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
                return new SdEngineStub(channel, callOptions);
              }
            };
    return SdEngineStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static SdEngineBlockingStub newBlockingStub(
          io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SdEngineBlockingStub> factory =
            new io.grpc.stub.AbstractStub.StubFactory<SdEngineBlockingStub>() {
              @java.lang.Override
              public SdEngineBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
                return new SdEngineBlockingStub(channel, callOptions);
              }
            };
    return SdEngineBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static SdEngineFutureStub newFutureStub(
          io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SdEngineFutureStub> factory =
            new io.grpc.stub.AbstractStub.StubFactory<SdEngineFutureStub>() {
              @java.lang.Override
              public SdEngineFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
                return new SdEngineFutureStub(channel, callOptions);
              }
            };
    return SdEngineFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void text2img(Sd.SdText2ImgRequest request,
                          io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getText2imgMethod(), responseObserver);
    }

    /**
     */
    default void img2img(Sd.SdImg2ImgRequest request,
                         io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getImg2imgMethod(), responseObserver);
    }

    /**
     */
    default void upscale(Sd.SdUpscaleRequest request,
                         io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getUpscaleMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service SdEngine.
   */
  public static abstract class SdEngineImplBase
          implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return SdEngineGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service SdEngine.
   */
  public static final class SdEngineStub
          extends io.grpc.stub.AbstractAsyncStub<SdEngineStub> {
    private SdEngineStub(
            io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SdEngineStub build(
            io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SdEngineStub(channel, callOptions);
    }

    /**
     */
    public void text2img(Sd.SdText2ImgRequest request,
                         io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getText2imgMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void img2img(Sd.SdImg2ImgRequest request,
                        io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getImg2imgMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void upscale(Sd.SdUpscaleRequest request,
                        io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getUpscaleMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service SdEngine.
   */
  public static final class SdEngineBlockingStub
          extends io.grpc.stub.AbstractBlockingStub<SdEngineBlockingStub> {
    private SdEngineBlockingStub(
            io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SdEngineBlockingStub build(
            io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SdEngineBlockingStub(channel, callOptions);
    }

    /**
     */
    public Sd.SdResponse text2img(Sd.SdText2ImgRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getText2imgMethod(), getCallOptions(), request);
    }

    /**
     */
    public Sd.SdResponse img2img(Sd.SdImg2ImgRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getImg2imgMethod(), getCallOptions(), request);
    }

    /**
     */
    public Sd.SdResponse upscale(Sd.SdUpscaleRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getUpscaleMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service SdEngine.
   */
  public static final class SdEngineFutureStub
          extends io.grpc.stub.AbstractFutureStub<SdEngineFutureStub> {
    private SdEngineFutureStub(
            io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SdEngineFutureStub build(
            io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SdEngineFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdResponse> text2img(
            Sd.SdText2ImgRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getText2imgMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdResponse> img2img(
            Sd.SdImg2ImgRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getImg2imgMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdResponse> upscale(
            Sd.SdUpscaleRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getUpscaleMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_TEXT2IMG = 0;
  private static final int METHODID_IMG2IMG = 1;
  private static final int METHODID_UPSCALE = 2;

  private static final class MethodHandlers<Req, Resp> implements
          io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
          io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
          io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
          io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AsyncService serviceImpl;
    private final int methodId;

    MethodHandlers(AsyncService serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_TEXT2IMG:
          serviceImpl.text2img((Sd.SdText2ImgRequest) request,
                  (io.grpc.stub.StreamObserver<Sd.SdResponse>) responseObserver);
          break;
        case METHODID_IMG2IMG:
          serviceImpl.img2img((Sd.SdImg2ImgRequest) request,
                  (io.grpc.stub.StreamObserver<Sd.SdResponse>) responseObserver);
          break;
        case METHODID_UPSCALE:
          serviceImpl.upscale((Sd.SdUpscaleRequest) request,
                  (io.grpc.stub.StreamObserver<Sd.SdResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
            io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  public static final io.grpc.ServerServiceDefinition bindService(AsyncService service) {
    return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
            .addMethod(
                    getText2imgMethod(),
                    io.grpc.stub.ServerCalls.asyncUnaryCall(
                            new MethodHandlers<
                                    Sd.SdText2ImgRequest,
                                    Sd.SdResponse>(
                                    service, METHODID_TEXT2IMG)))
            .addMethod(
                    getImg2imgMethod(),
                    io.grpc.stub.ServerCalls.asyncUnaryCall(
                            new MethodHandlers<
                                    Sd.SdImg2ImgRequest,
                                    Sd.SdResponse>(
                                    service, METHODID_IMG2IMG)))
            .addMethod(
                    getUpscaleMethod(),
                    io.grpc.stub.ServerCalls.asyncUnaryCall(
                            new MethodHandlers<
                                    Sd.SdUpscaleRequest,
                                    Sd.SdResponse>(
                                    service, METHODID_UPSCALE)))
            .build();
  }

  private static abstract class SdEngineBaseDescriptorSupplier
          implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    SdEngineBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return Sd.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("SdEngine");
    }
  }

  private static final class SdEngineFileDescriptorSupplier
          extends SdEngineBaseDescriptorSupplier {
    SdEngineFileDescriptorSupplier() {}
  }

  private static final class SdEngineMethodDescriptorSupplier
          extends SdEngineBaseDescriptorSupplier
          implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    SdEngineMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (SdEngineGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
                  .setSchemaDescriptor(new SdEngineFileDescriptorSupplier())
                  .addMethod(getText2imgMethod())
                  .addMethod(getImg2imgMethod())
                  .addMethod(getUpscaleMethod())
                  .build();
        }
      }
    }
    return result;
  }
}
