import os
import boto3
import subprocess

# Descargar datos desde S3
s3 = boto3.client('s3')
bucket_name = 'autostrabuss'
dataset_path = 'dataset'

def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    paginator = s3.get_paginator('list_objects_v2')
    for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_folder):
        if result.get('Contents'):
            for file in result.get('Contents'):
                file_key = file['Key']
                if not file_key.endswith('/'):
                    local_file_path = os.path.join(local_dir, os.path.relpath(file_key, s3_folder))
                    local_file_dir = os.path.dirname(local_file_path)
                    if not os.path.exists(local_file_dir):
                        os.makedirs(local_file_dir)
                    s3.download_file(bucket_name, file_key, local_file_path)

download_s3_folder(bucket_name, f'{dataset_path}/images', '/darknet/data/images')
download_s3_folder(bucket_name, f'{dataset_path}/labels', '/darknet/data/labels')

# Configurar y entrenar Tiny YOLO v4
subprocess.run(['./darknet', 'detector', 'train', 'data/obj.data', 'cfg/yolov4-tiny.cfg', 'darknet53.conv.74'])
