package grpc;
import static io.grpc.MethodDescriptor.generateFullMethodName;
import proto.Sd;

/**
 * <pre>
 *定义服务接口
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.56.0)",
    comments = "Source: sd.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class SdServiceGrpc {

  private SdServiceGrpc() {}

  public static final String SERVICE_NAME = "SdService";

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
    if ((getText2imgMethod = SdServiceGrpc.getText2imgMethod) == null) {
      synchronized (SdServiceGrpc.class) {
        if ((getText2imgMethod = SdServiceGrpc.getText2imgMethod) == null) {
          SdServiceGrpc.getText2imgMethod = getText2imgMethod =
              io.grpc.MethodDescriptor.<Sd.SdText2ImgRequest, Sd.SdResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "text2img"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  Sd.SdText2ImgRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  Sd.SdResponse.getDefaultInstance()))
              .setSchemaDescriptor(new SdServiceMethodDescriptorSupplier("text2img"))
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
    if ((getImg2imgMethod = SdServiceGrpc.getImg2imgMethod) == null) {
      synchronized (SdServiceGrpc.class) {
        if ((getImg2imgMethod = SdServiceGrpc.getImg2imgMethod) == null) {
          SdServiceGrpc.getImg2imgMethod = getImg2imgMethod =
              io.grpc.MethodDescriptor.<Sd.SdImg2ImgRequest, Sd.SdResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "img2img"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  Sd.SdImg2ImgRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  Sd.SdResponse.getDefaultInstance()))
              .setSchemaDescriptor(new SdServiceMethodDescriptorSupplier("img2img"))
              .build();
        }
      }
    }
    return getImg2imgMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static SdServiceStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SdServiceStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SdServiceStub>() {
        @java.lang.Override
        public SdServiceStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SdServiceStub(channel, callOptions);
        }
      };
    return SdServiceStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static SdServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SdServiceBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SdServiceBlockingStub>() {
        @java.lang.Override
        public SdServiceBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SdServiceBlockingStub(channel, callOptions);
        }
      };
    return SdServiceBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static SdServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SdServiceFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SdServiceFutureStub>() {
        @java.lang.Override
        public SdServiceFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SdServiceFutureStub(channel, callOptions);
        }
      };
    return SdServiceFutureStub.newStub(factory, channel);
  }

  /**
   * <pre>
   *定义服务接口
   * </pre>
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
  }

  /**
   * Base class for the server implementation of the service SdService.
   * <pre>
   *定义服务接口
   * </pre>
   */
  public static abstract class SdServiceImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return SdServiceGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service SdService.
   * <pre>
   *定义服务接口
   * </pre>
   */
  public static final class SdServiceStub
      extends io.grpc.stub.AbstractAsyncStub<SdServiceStub> {
    private SdServiceStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SdServiceStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SdServiceStub(channel, callOptions);
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
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service SdService.
   * <pre>
   *定义服务接口
   * </pre>
   */
  public static final class SdServiceBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<SdServiceBlockingStub> {
    private SdServiceBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SdServiceBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SdServiceBlockingStub(channel, callOptions);
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
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service SdService.
   * <pre>
   *定义服务接口
   * </pre>
   */
  public static final class SdServiceFutureStub
      extends io.grpc.stub.AbstractFutureStub<SdServiceFutureStub> {
    private SdServiceFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SdServiceFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SdServiceFutureStub(channel, callOptions);
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
  }

  private static final int METHODID_TEXT2IMG = 0;
  private static final int METHODID_IMG2IMG = 1;

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
        .build();
  }

  private static abstract class SdServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    SdServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return Sd.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("SdService");
    }
  }

  private static final class SdServiceFileDescriptorSupplier
      extends SdServiceBaseDescriptorSupplier {
    SdServiceFileDescriptorSupplier() {}
  }

  private static final class SdServiceMethodDescriptorSupplier
      extends SdServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    SdServiceMethodDescriptorSupplier(String methodName) {
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
      synchronized (SdServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new SdServiceFileDescriptorSupplier())
              .addMethod(getText2imgMethod())
              .addMethod(getImg2imgMethod())
              .build();
        }
      }
    }
    return result;
  }
}
