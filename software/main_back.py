import sys
import platform
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer

from mainUi import Ui_AutoStrabus
from FrameDivider import FrameDivider
from DetectPupil import PupilDetector
from TrackbarHandler import process_frame
from OpenList import FileTableWidget
from  edit_video import VideoEditor

# Importar la clase adecuada según el sistema operativo
if platform.system() == "Linux":
    from V4L2Camera import V4L2Camera as Camera
elif platform.system() == "Windows":
    from WindowsCamera import WindowsCamera as Camera
else:
    raise EnvironmentError("Sistema operativo no soportado")

class AutoStrabus(QMainWindow, Ui_AutoStrabus):
    def __init__(self):
        super(AutoStrabus, self).__init__()
        self.setupUi(self)
        self.showMaximized()

        self.open_file = FileTableWidget()
        self.layout_openList.addWidget(self.open_file)
        self.open_file.btn_action.connect(self.open_file_actions)

        self.video_editor = VideoEditor()
        self.layout_edit.addWidget(self.video_editor)

        
        self.blur_size = self.slider_blur.value()
        self.threshold_value = self.slider_threshold.value()
        self.min_contour_area = self.slider_size.value()  # Default value for contour area
        self.focus_value = 385  # Default focus value
        self.brightness_value = 0  # Default brightness value
        self.contrast_value = 50  # Default contrast value
        self.autofocus_value = 0  # Default autofocus value (off)
        self.white_balance_automatic_value = 1  # Default white balance automatic value (on)
        
        self.slider_focus.setMaximum(1023)
        self.slider_focus.setMinimum(0)
        self.slider_brig.setMaximum(64)
        self.slider_brig.setMinimum(-64)
        self.slider_contrast.setMaximum(95)
        self.slider_contrast.setMinimum(0)
        self.slider_focus.setValue(self.focus_value)
        self.slider_brig.setValue(self.brightness_value)
        self.slider_contrast.setValue(self.contrast_value)
        self.chk_autofocus.setChecked(bool(self.autofocus_value))
        self.chk_white_balance_automatic.setChecked(bool(self.white_balance_automatic_value))
        self.lbl_focus.setText(f"{self.focus_value}")
        self.lbl_brig.setText(f"{self.brightness_value}")
        self.lbl_contrast.setText(f"{self.contrast_value}")

        self.slider_blur.valueChanged.connect(self.update_params)
        self.slider_threshold.valueChanged.connect(self.update_params)
        self.slider_size.valueChanged.connect(self.update_params)
        self.slider_focus.valueChanged.connect(self.update_focus)
        self.slider_brig.valueChanged.connect(self.update_brightness)
        self.slider_contrast.valueChanged.connect(self.update_contrast)
        self.chk_autofocus.toggled.connect(self.update_autofocus)
        self.chk_white_balance_automatic.toggled.connect(self.update_white_balance_automatic)

        self.frame_head.setFixedHeight(200)
        self.frame_head.setFixedWidth(200)

        self.camera_open = False
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setCurrentIndex(0)

        self.CameraFrame.setFixedSize(1280, 720)



    def open_file_actions(self, values):
        if values[0] == "new":
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setTabEnabled(2, False)
            self.activate_camera()
            self.setWindowTitle("* AutoStrabus - Nueva grabación")
            self.tabWidget.setCurrentIndex(1)
            self.showMaximized()


        elif values[0] == "open":
            self.tabWidget.setTabEnabled(2,True)
            self.tabWidget.setCurrentIndex(2)
            file = values[1]
            _,name_file = file.split("/")
            name_file,_ = name_file.split(".")
            self.setWindowTitle(f"AutoStrabus - {name_file}")
            self.video_editor.load_video(file)



    def activate_camera(self):
        self.camera_open = True
        self.camera = Camera()
        self.divider = FrameDivider()
        self.detector = PupilDetector()

         # Obtener cámaras conectadas
        cameras = self.camera.get_connected_cameras()
        camera_name = "DH Camera"
        self.device_path = None
        for cam_name, cam_path in cameras:
            if camera_name in cam_name:
                self.device_path = cam_path
                break

        if not self.device_path:
            raise ValueError(f"No se encontró la cámara {camera_name}")

        # Configurar la cámara con el tamaño de fotograma deseado
        if platform.system() == "Linux":
            self.camera.set_camera(self.device_path, 1280, 720)
        elif platform.system() == "Windows":
            self.camera.set_camera(self.device_path)
            self.camera.set_control('frame_size', (1280, 720))

        # Inicializar la captura de video desde la cámara configurada
        self.cap = cv2.VideoCapture(self.device_path if platform.system() == "Linux" else 0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        # Configurar el enfoque, brillo, contraste, enfoque automático y balance de blancos automático iniciales
        self.update_focus(self.focus_value)
        self.update_brightness(self.brightness_value)
        self.update_contrast(self.contrast_value)
        self.update_autofocus(self.autofocus_value)
        self.update_white_balance_automatic(self.white_balance_automatic_value)


    def update_params(self):
        self.blur_size = self.slider_blur.value()
        self.threshold_value = self.slider_threshold.value()
        self.min_contour_area = self.slider_size.value()

        self.lbl_blur.setText(f"{self.blur_size}")
        self.lbl_threshold.setText(f"{self.threshold_value}")
        self.lbl_size.setText(f"{self.min_contour_area}")

    def update_focus(self, value):
        self.focus_value = value
        self.camera.set_focus(self.focus_value)
        self.lbl_focus.setText(f"{self.focus_value}")

    def update_brightness(self, value):
        self.brightness_value = value
        self.camera.set_brightness(self.brightness_value)
        self.lbl_brig.setText(f"{self.brightness_value}")

    def update_contrast(self, value):
        self.contrast_value = value
        self.camera.set_contrast(self.contrast_value)
        self.lbl_contrast.setText(f"{self.contrast_value}")

    def update_autofocus(self, value):
        self.autofocus_value = int(value)
        self.camera.set_autofocus(self.autofocus_value)

    def update_white_balance_automatic(self, value):
        self.white_balance_automatic_value = int(value)
        self.camera.set_white_balance_automatic(self.white_balance_automatic_value)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = process_frame(frame, self.divider, self.detector, self.blur_size, self.threshold_value, self.min_contour_area)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.CameraFrame.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        if self.camera_open:
            self.cap.release()
        super(AutoStrabus, self).closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoStrabus()
    window.show()
    sys.exit(app.exec())
