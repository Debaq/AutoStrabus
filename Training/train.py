import subprocess

# Configurar y entrenar Tiny YOLO v4
subprocess.run(['./darknet', 'detector', 'train', 'data/obj.data', 'cfg/yolov4-tiny.cfg', 'darknet53.conv.74'])
