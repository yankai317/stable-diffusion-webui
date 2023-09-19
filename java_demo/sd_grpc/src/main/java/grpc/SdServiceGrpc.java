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
    if ((getUpscaleMethod = SdServiceGrpc.getUpscaleMethod) == null) {
      synchronized (SdServiceGrpc.class) {
        if ((getUpscaleMethod = SdServiceGrpc.getUpscaleMethod) == null) {
          SdServiceGrpc.getUpscaleMethod = getUpscaleMethod =
                  io.grpc.MethodDescriptor.<Sd.SdUpscaleRequest, Sd.SdResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "upscale"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdUpscaleRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdServiceMethodDescriptorSupplier("upscale"))
                          .build();
        }
      }
    }
    return getUpscaleMethod;
  }

  private static volatile io.grpc.MethodDescriptor<Sd.SdText2ImgRequest,
          Sd.SdAsynTaskResponse> getText2imgAsynMethod;

  @io.grpc.stub.annotations.RpcMethod(
          fullMethodName = SERVICE_NAME + '/' + "text2img_asyn",
          requestType = Sd.SdText2ImgRequest.class,
          responseType = Sd.SdAsynTaskResponse.class,
          methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<Sd.SdText2ImgRequest,
          Sd.SdAsynTaskResponse> getText2imgAsynMethod() {
    io.grpc.MethodDescriptor<Sd.SdText2ImgRequest, Sd.SdAsynTaskResponse> getText2imgAsynMethod;
    if ((getText2imgAsynMethod = SdServiceGrpc.getText2imgAsynMethod) == null) {
      synchronized (SdServiceGrpc.class) {
        if ((getText2imgAsynMethod = SdServiceGrpc.getText2imgAsynMethod) == null) {
          SdServiceGrpc.getText2imgAsynMethod = getText2imgAsynMethod =
                  io.grpc.MethodDescriptor.<Sd.SdText2ImgRequest, Sd.SdAsynTaskResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "text2img_asyn"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdText2ImgRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdAsynTaskResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdServiceMethodDescriptorSupplier("text2img_asyn"))
                          .build();
        }
      }
    }
    return getText2imgAsynMethod;
  }

  private static volatile io.grpc.MethodDescriptor<Sd.SdImg2ImgRequest,
          Sd.SdAsynTaskResponse> getImg2imgAsynMethod;

  @io.grpc.stub.annotations.RpcMethod(
          fullMethodName = SERVICE_NAME + '/' + "img2img_asyn",
          requestType = Sd.SdImg2ImgRequest.class,
          responseType = Sd.SdAsynTaskResponse.class,
          methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<Sd.SdImg2ImgRequest,
          Sd.SdAsynTaskResponse> getImg2imgAsynMethod() {
    io.grpc.MethodDescriptor<Sd.SdImg2ImgRequest, Sd.SdAsynTaskResponse> getImg2imgAsynMethod;
    if ((getImg2imgAsynMethod = SdServiceGrpc.getImg2imgAsynMethod) == null) {
      synchronized (SdServiceGrpc.class) {
        if ((getImg2imgAsynMethod = SdServiceGrpc.getImg2imgAsynMethod) == null) {
          SdServiceGrpc.getImg2imgAsynMethod = getImg2imgAsynMethod =
                  io.grpc.MethodDescriptor.<Sd.SdImg2ImgRequest, Sd.SdAsynTaskResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "img2img_asyn"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdImg2ImgRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdAsynTaskResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdServiceMethodDescriptorSupplier("img2img_asyn"))
                          .build();
        }
      }
    }
    return getImg2imgAsynMethod;
  }

  private static volatile io.grpc.MethodDescriptor<Sd.SdUpscaleRequest,
          Sd.SdAsynTaskResponse> getUpscaleAsynMethod;

  @io.grpc.stub.annotations.RpcMethod(
          fullMethodName = SERVICE_NAME + '/' + "upscale_asyn",
          requestType = Sd.SdUpscaleRequest.class,
          responseType = Sd.SdAsynTaskResponse.class,
          methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<Sd.SdUpscaleRequest,
          Sd.SdAsynTaskResponse> getUpscaleAsynMethod() {
    io.grpc.MethodDescriptor<Sd.SdUpscaleRequest, Sd.SdAsynTaskResponse> getUpscaleAsynMethod;
    if ((getUpscaleAsynMethod = SdServiceGrpc.getUpscaleAsynMethod) == null) {
      synchronized (SdServiceGrpc.class) {
        if ((getUpscaleAsynMethod = SdServiceGrpc.getUpscaleAsynMethod) == null) {
          SdServiceGrpc.getUpscaleAsynMethod = getUpscaleAsynMethod =
                  io.grpc.MethodDescriptor.<Sd.SdUpscaleRequest, Sd.SdAsynTaskResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "upscale_asyn"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdUpscaleRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdAsynTaskResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdServiceMethodDescriptorSupplier("upscale_asyn"))
                          .build();
        }
      }
    }
    return getUpscaleAsynMethod;
  }

  private static volatile io.grpc.MethodDescriptor<Sd.SdQueryRequest,
          Sd.SdResponse> getQueryMethod;

  @io.grpc.stub.annotations.RpcMethod(
          fullMethodName = SERVICE_NAME + '/' + "query",
          requestType = Sd.SdQueryRequest.class,
          responseType = Sd.SdResponse.class,
          methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<Sd.SdQueryRequest,
          Sd.SdResponse> getQueryMethod() {
    io.grpc.MethodDescriptor<Sd.SdQueryRequest, Sd.SdResponse> getQueryMethod;
    if ((getQueryMethod = SdServiceGrpc.getQueryMethod) == null) {
      synchronized (SdServiceGrpc.class) {
        if ((getQueryMethod = SdServiceGrpc.getQueryMethod) == null) {
          SdServiceGrpc.getQueryMethod = getQueryMethod =
                  io.grpc.MethodDescriptor.<Sd.SdQueryRequest, Sd.SdResponse>newBuilder()
                          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
                          .setFullMethodName(generateFullMethodName(SERVICE_NAME, "query"))
                          .setSampledToLocalTracing(true)
                          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdQueryRequest.getDefaultInstance()))
                          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                                  Sd.SdResponse.getDefaultInstance()))
                          .setSchemaDescriptor(new SdServiceMethodDescriptorSupplier("query"))
                          .build();
        }
      }
    }
    return getQueryMethod;
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

    /**
     */
    default void upscale(Sd.SdUpscaleRequest request,
                         io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getUpscaleMethod(), responseObserver);
    }

    /**
     */
    default void text2imgAsyn(Sd.SdText2ImgRequest request,
                              io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getText2imgAsynMethod(), responseObserver);
    }

    /**
     */
    default void img2imgAsyn(Sd.SdImg2ImgRequest request,
                             io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getImg2imgAsynMethod(), responseObserver);
    }

    /**
     */
    default void upscaleAsyn(Sd.SdUpscaleRequest request,
                             io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getUpscaleAsynMethod(), responseObserver);
    }

    /**
     */
    default void query(Sd.SdQueryRequest request,
                       io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getQueryMethod(), responseObserver);
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

    /**
     */
    public void upscale(Sd.SdUpscaleRequest request,
                        io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getUpscaleMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void text2imgAsyn(Sd.SdText2ImgRequest request,
                             io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getText2imgAsynMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void img2imgAsyn(Sd.SdImg2ImgRequest request,
                            io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getImg2imgAsynMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void upscaleAsyn(Sd.SdUpscaleRequest request,
                            io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getUpscaleAsynMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void query(Sd.SdQueryRequest request,
                      io.grpc.stub.StreamObserver<Sd.SdResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
              getChannel().newCall(getQueryMethod(), getCallOptions()), request, responseObserver);
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

    /**
     */
    public Sd.SdResponse upscale(Sd.SdUpscaleRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getUpscaleMethod(), getCallOptions(), request);
    }

    /**
     */
    public Sd.SdAsynTaskResponse text2imgAsyn(Sd.SdText2ImgRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getText2imgAsynMethod(), getCallOptions(), request);
    }

    /**
     */
    public Sd.SdAsynTaskResponse img2imgAsyn(Sd.SdImg2ImgRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getImg2imgAsynMethod(), getCallOptions(), request);
    }

    /**
     */
    public Sd.SdAsynTaskResponse upscaleAsyn(Sd.SdUpscaleRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getUpscaleAsynMethod(), getCallOptions(), request);
    }

    /**
     */
    public Sd.SdResponse query(Sd.SdQueryRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
              getChannel(), getQueryMethod(), getCallOptions(), request);
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

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdResponse> upscale(
            Sd.SdUpscaleRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getUpscaleMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdAsynTaskResponse> text2imgAsyn(
            Sd.SdText2ImgRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getText2imgAsynMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdAsynTaskResponse> img2imgAsyn(
            Sd.SdImg2ImgRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getImg2imgAsynMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdAsynTaskResponse> upscaleAsyn(
            Sd.SdUpscaleRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getUpscaleAsynMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<Sd.SdResponse> query(
            Sd.SdQueryRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
              getChannel().newCall(getQueryMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_TEXT2IMG = 0;
  private static final int METHODID_IMG2IMG = 1;
  private static final int METHODID_UPSCALE = 2;
  private static final int METHODID_TEXT2IMG_ASYN = 3;
  private static final int METHODID_IMG2IMG_ASYN = 4;
  private static final int METHODID_UPSCALE_ASYN = 5;
  private static final int METHODID_QUERY = 6;

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
        case METHODID_TEXT2IMG_ASYN:
          serviceImpl.text2imgAsyn((Sd.SdText2ImgRequest) request,
                  (io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse>) responseObserver);
          break;
        case METHODID_IMG2IMG_ASYN:
          serviceImpl.img2imgAsyn((Sd.SdImg2ImgRequest) request,
                  (io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse>) responseObserver);
          break;
        case METHODID_UPSCALE_ASYN:
          serviceImpl.upscaleAsyn((Sd.SdUpscaleRequest) request,
                  (io.grpc.stub.StreamObserver<Sd.SdAsynTaskResponse>) responseObserver);
          break;
        case METHODID_QUERY:
          serviceImpl.query((Sd.SdQueryRequest) request,
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
            .addMethod(
                    getText2imgAsynMethod(),
                    io.grpc.stub.ServerCalls.asyncUnaryCall(
                            new MethodHandlers<
                                    Sd.SdText2ImgRequest,
                                    Sd.SdAsynTaskResponse>(
                                    service, METHODID_TEXT2IMG_ASYN)))
            .addMethod(
                    getImg2imgAsynMethod(),
                    io.grpc.stub.ServerCalls.asyncUnaryCall(
                            new MethodHandlers<
                                    Sd.SdImg2ImgRequest,
                                    Sd.SdAsynTaskResponse>(
                                    service, METHODID_IMG2IMG_ASYN)))
            .addMethod(
                    getUpscaleAsynMethod(),
                    io.grpc.stub.ServerCalls.asyncUnaryCall(
                            new MethodHandlers<
                                    Sd.SdUpscaleRequest,
                                    Sd.SdAsynTaskResponse>(
                                    service, METHODID_UPSCALE_ASYN)))
            .addMethod(
                    getQueryMethod(),
                    io.grpc.stub.ServerCalls.asyncUnaryCall(
                            new MethodHandlers<
                                    Sd.SdQueryRequest,
                                    Sd.SdResponse>(
                                    service, METHODID_QUERY)))
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
                  .addMethod(getUpscaleMethod())
                  .addMethod(getText2imgAsynMethod())
                  .addMethod(getImg2imgAsynMethod())
                  .addMethod(getUpscaleAsynMethod())
                  .addMethod(getQueryMethod())
                  .build();
        }
      }
    }
    return result;
  }
}
