FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    git \
    wget \
    cmake \
    build-essential \
    libopencv-dev \
    python3 \
    python3-pip

# Instalar AWS CLI y SageMaker Inference Toolkit
RUN pip3 install awscli sagemaker-training

# Instalar darknet
RUN git clone https://github.com/AlexeyAB/darknet.git /darknet
WORKDIR /darknet
RUN sed -i 's/GPU=0/GPU=1/' Makefile && \
    sed -i 's/CUDNN=0/CUDNN=1/' Makefile && \
    sed -i 's/OPENCV=0/OPENCV=1/' Makefile && \
    make

# Instalar dependencias Python
RUN pip3 install numpy opencv-python

# Copiar scripts de entrenamiento y configuración
COPY Training/train.py /opt/ml/code/train.py
COPY Training/entrypoint.py /opt/ml/code/entrypoint.py

# Comando por defecto
ENTRYPOINT ["python3", "/opt/ml/code/entrypoint.py"]
