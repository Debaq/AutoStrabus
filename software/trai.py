import platform
import cv2
from FrameDivider import FrameDivider
from DetectPupil import PupilDetector
from TrackbarHandler import on_trackbar

# Importar la clase adecuada según el sistema operativo
if platform.system() == "Linux":
    from V4L2Camera import V4L2Camera as Camera
elif platform.system() == "Windows":
    from WindowsCamera import WindowsCamera as Camera
else:
    raise EnvironmentError("Sistema operativo no soportado")

def main():
    # Crear instancia de la clase de cámara adecuada
    camera = Camera()

    # Obtener cámaras conectadas
    cameras = camera.get_connected_cameras()
    print("Cámaras conectadas:")
    for cam in cameras:
        print(cam)
    
    # Buscar la cámara "DH Camera"
    camera_name = "DH Camera"
    device_path = None
    for cam_name, cam_path in cameras:
        if camera_name in cam_name:
            device_path = cam_path
            break

    if not device_path:
        raise ValueError(f"No se encontró la cámara {camera_name}")

    # Configurar la cámara con el tamaño de fotograma deseado
    if platform.system() == "Linux":
        camera.set_camera(device_path, 1280, 720)
    elif platform.system() == "Windows":
        camera.set_camera(device_path)
        camera.set_control('frame_size', (1280, 720))

    # Inicializar la clase de detección de pupilas y divisor de frames
    divider = FrameDivider()
    detector = PupilDetector()

    # Capturar video desde la cámara configurada
    cap = cv2.VideoCapture(device_path if platform.system() == "Linux" else 0)

    # Asegurarse de que el tamaño del fotograma esté configurado en OpenCV
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Crear la ventana principal y los sliders
    cv2.namedWindow('Pupil Detector')
    cv2.createTrackbar('Blur Size', 'Pupil Detector', 5, 50, lambda val: on_trackbar(val, frame, divider, detector, blur_size, threshold_value, min_contour_area))
    cv2.createTrackbar('Threshold', 'Pupil Detector', 30, 255, lambda val: on_trackbar(val, frame, divider, detector, blur_size, threshold_value, min_contour_area))
    cv2.createTrackbar('Min Contour Area', 'Pupil Detector', 50, 1000, lambda val: on_trackbar(val, frame, divider, detector, blur_size, threshold_value, min_contour_area))

    # Inicializar parámetros
    global blur_size, threshold_value, min_contour_area, frame
    blur_size = 5
    threshold_value = 30
    min_contour_area = 50
    frame = None

    while True:
        # Leer un frame de la cámara
        ret, frame = cap.read()
        if not ret:
            break

        # Actualizar la detección de pupilas con los valores actuales de los sliders
        on_trackbar(0, frame, divider, detector, blur_size, threshold_value, min_contour_area)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
