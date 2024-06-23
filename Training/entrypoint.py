import os
import subprocess
import boto3

def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    s3 = boto3.client('s3')
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

def upload_to_s3(bucket_name, local_dir, s3_folder):
    s3 = boto3.client('s3')
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_file_path, local_dir)
            s3_key = os.path.join(s3_folder, relative_path)
            print(f'Uploading {local_file_path} to s3://{bucket_name}/{s3_key}')
            s3.upload_file(local_file_path, bucket_name, s3_key)

if __name__ == '__main__':
    bucket_name = os.environ.get('S3_BUCKET_NAME', 'autostrabus')
    dataset_path = os.environ.get('S3_DATASET_PATH', 'dataset')
    output_path = os.environ.get('S3_OUTPUT_PATH', 'output')

    # Descargar datos desde S3
    download_s3_folder(bucket_name, f'{dataset_path}/images', '/darknet/data/images')
    download_s3_folder(bucket_name, f'{dataset_path}/labels', '/darknet/data/labels')

    # Ejecutar el script de entrenamiento
    subprocess.run(['python3', '/opt/ml/code/train.py'])

    # Crear archivo tar.gz del modelo entrenado
    model_dir = '/darknet/backup'
    tar_file_path = '/darknet/model.tar.gz'
    subprocess.run(['tar', '-czvf', tar_file_path, '-C', model_dir, '.'])

    # Subir el archivo tar.gz a S3
    upload_to_s3(bucket_name, '/darknet', output_path)
