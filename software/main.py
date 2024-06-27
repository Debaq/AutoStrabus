import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer

from mainUi import Ui_AutoStrabus
from OpenList import FileTableWidget
from edit_video import VideoEditor
from camera_config import CameraConfig
from opencv_logic import OpenCVLogic

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
        self.min_contour_area = self.slider_size.value()
        self.focus_value = 385
        self.brightness_value = 0
        self.contrast_value = 0
        self.hue_value = 0
        self.saturation = 64
        self.gamma = 100
        self.autofocus_value = 0
        self.white_balance_automatic_value = 1

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

        self.camera_config = CameraConfig()
        self.opencv_logic = OpenCVLogic()

        self.btn_record.clicked.connect(self.toggle_recording)
        self.is_recording = False
        self.frame_number = 0

    def open_file_actions(self, values):
        if values[0] == "new":
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setTabEnabled(2, False)
            self.activate_camera()
            self.setWindowTitle("* AutoStrabus - Nueva grabación")
            self.tabWidget.setCurrentIndex(1)
            self.showMaximized()

        elif values[0] == "open":
            self.tabWidget.setTabEnabled(2, True)
            self.tabWidget.setCurrentIndex(2)
            file = values[1]
            _, name_file = file.split("/")
            name_file, _ = name_file.split(".")
            self.setWindowTitle(f"AutoStrabus - {name_file}")
            self.video_editor.load_video(file)

    def activate_camera(self):
        self.camera_open = True
        device_path = self.camera_config.get_connected_camera()
        self.cap = self.camera_config.setup_camera()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.update_focus(self.focus_value)
        self.update_brightness(self.brightness_value)
        self.update_contrast(self.contrast_value)
        self.update_autofocus(self.autofocus_value)
        self.update_white_balance_automatic(self.white_balance_automatic_value)

    def update_params(self):
        self.blur_size = self.slider_blur.value()
        self.threshold_value = self.slider_threshold.value()
        self.min_contour_area = self.slider_size.value()
        self.opencv_logic.set_params(self.blur_size, self.threshold_value, self.min_contour_area)

        self.lbl_blur.setText(f"{self.blur_size}")
        self.lbl_threshold.setText(f"{self.threshold_value}")
        self.lbl_size.setText(f"{self.min_contour_area}")

    def update_focus(self, value):
        self.focus_value = value
        self.camera_config.set_focus(self.focus_value)
        self.lbl_focus.setText(f"{self.focus_value}")

    def update_brightness(self, value):
        self.brightness_value = value
        self.camera_config.set_brightness(self.brightness_value)
        self.lbl_brig.setText(f"{self.brightness_value}")

    def update_contrast(self, value):
        self.contrast_value = value
        self.camera_config.set_contrast(self.contrast_value)
        self.lbl_contrast.setText(f"{self.contrast_value}")

    def update_autofocus(self, value):
        self.autofocus_value = int(value)
        self.camera_config.set_autofocus(self.autofocus_value)

    def update_white_balance_automatic(self, value):
        self.white_balance_automatic_value = int(value)
        self.camera_config.set_white_balance_automatic(self.white_balance_automatic_value)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            original_frame, marked_frame = self.opencv_logic.process_frame(frame, self.frame_number)
            image = QImage(marked_frame.data, marked_frame.shape[1], marked_frame.shape[0], QImage.Format_RGB888)
            self.CameraFrame.setPixmap(QPixmap.fromImage(image))
            if self.is_recording:
                self.camera_config.write_frame(original_frame)
            self.frame_number += 1

    def toggle_recording(self):
        if self.is_recording:
            self.camera_config.stop_recording()
            self.opencv_logic.save_marks_to_json()
            self.is_recording = False
            self.btn_record.setText("Grabar")
        else:
            self.camera_config.start_recording()
            self.is_recording = True
            self.frame_number = 0
            self.opencv_logic.frame_data.clear()  # Limpiar los datos de los frames anteriores
            self.btn_record.setText("Parar")

    def closeEvent(self, event):
        if self.camera_open:
            self.cap.release()
        if self.is_recording:
            self.camera_config.stop_recording()
            self.opencv_logic.save_marks_to_json()
        super(AutoStrabus, self).closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoStrabus()
    window.show()
    sys.exit(app.exec())
