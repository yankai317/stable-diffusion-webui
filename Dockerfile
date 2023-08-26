FROM sd-auto:63

RUN sed -i s/archive.ubuntu.com/mirrors.163.com/g /etc/apt/sources.list && \
    sed -i s/security.ubuntu.com/mirrors.163.com/g /etc/apt/sources.list

ENV NVIDIA_DRIVER_CAPABILITIES=video,compute,utility
ENV TERM=xterm \
    TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN git config --global url."https://hub.fgit.cf/".insteadOf "https://github.com/"
RUN pip install grpcio grpcio-tools -i https://mirrors.aliyun.com/pypi/simple
ENV REPO_ROOT=/root/stable-diffusion-webui
ADD . $REPO_ROOT
RUN cp -r /stable-diffusion-webui/repositories /root/stable-diffusion-webui
