FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    wget \
    curl \
    cmake \
    libopencv-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Clonar el repositorio de Darknet
RUN git clone https://github.com/AlexeyAB/darknet.git
WORKDIR /darknet

# Configurar y construir Darknet con soporte para OpenCV y CUDA
RUN sed -i 's/OPENCV=0/OPENCV=1/' Makefile \
    && sed -i 's/GPU=0/GPU=1/' Makefile \
    && sed -i 's/CUDNN=0/CUDNN=1/' Makefile \
    && sed -i 's/ARCH= -gencode arch=compute_30,code=sm_30 -gencode arch=compute_35,code=sm_35 -gencode arch=compute_50,code=[sm_50,compute_50]/ARCH= -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_75,code=sm_75/' Makefile \
    && make

# Copiar los datos y el script de entrenamiento
COPY . /darknet

# Comando por defecto para ejecutar el contenedor
CMD ["darknet", "detector", "train", "/darknet/cfg/your_data.data", "/darknet/cfg/yolov4-tiny.cfg", "/darknet/yolov4-tiny.conv.29"]
