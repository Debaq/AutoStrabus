import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer

from mainUi import Ui_AutoStrabus
from OpenList import FileTableWidget
from edit_video import VideoEditor
from camera_config import CameraConfig
from opencv_logic import OpenCVLogic
from SerialHandler import SerialHandler

import threading
from PySide6.QtCore import QThread, Signal

class SerialReadThread(QThread):
    data_received = Signal(str)

    def __init__(self, serial_handler):
        super().__init__()
        self.serial_handler = serial_handler
        self._running = True

    def run(self):
        while self._running:
            data = self.serial_handler.read_data()
            if data:
                self.data_received.emit(data)
                self.msleep(10)  # Pequeña pausa para evitar sobrecargar el CPU

    def stop(self):
        self._running = False
        self.wait()
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

        self.slider_threshold.setRange(0,255)
        self.slider_focus.setRange(0,1023)
        self.slider_brig.setRange(-64,64)
        self.slider_contrast.setRange(0,95)
        self.slider_hue.setRange(-2000,2000)
        self.slider_hue.setValue(self.hue_value)
        self.slider_h.setRange(-40,40)
        self.slider_v.setRange(-20,30)

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
        self.slider_hue.valueChanged.connect(self.update_hue)
        self.slider_contrast.valueChanged.connect(self.update_contrast)
        self.chk_autofocus.toggled.connect(self.update_autofocus)
        self.chk_white_balance_automatic.toggled.connect(self.update_white_balance_automatic)

        self.frame_head.setFixedHeight(200)
        self.frame_head.setFixedWidth(200)
        self.slider_v.setFixedHeight(130)

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
        self.serial_handler = SerialHandler('/dev/ttyUSB0', 9600)  # Ajusta 'COM3' al puerto correcto
        self.btn_act_oclu.clicked.connect(self.on_btn_act_oclu_clicked)

        self.serial_thread = SerialReadThread(self.serial_handler)
        self.serial_thread.data_received.connect(self.handle_serial_data)
        self.serial_thread.start()

    def handle_serial_data(self, data):
        # Dividir el string por el punto y coma
        string_list = data.split(";")

        # Convertir cada elemento a float o bool según su posición
        result_list = [float(item) if index < len(string_list) - 2 else bool(int(item)) for index, item in enumerate(string_list)]
        self.slider_h.setValue(result_list[1])
        self.slider_v.setValue(result_list[2])
        oclus = [result_list[3],result_list[4]]
        self.opencv_logic.activate_oclusor(oclus)


    def on_btn_act_oclu_clicked(self):
        if self.sender().text() == "Activar Oclusores":
            time_alt = int(self.time_alt.value())
            time_sup = int(self.time_sup.value())
            data_string = f"T{time_alt}O{time_sup}"
            self.serial_handler.send_data(data_string)
            self.serial_handler.send_data("OCLUON")
            self.sender().setText("Apagar Oclusores")
        else:
            self.serial_handler.send_data("OCLUOFF")
            self.sender().setText("Activar Oclusores")


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
        self.timer.start(10)

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

    def update_hue(self, value):
        self.hue_value = value
        self.camera_config.set_hue(self.hue_value)
        self.lbl_hue.setText(f"{self.hue_value}")

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
        self.serial_thread.stop()  # Detener el hilo de lectura serial
        super(AutoStrabus, self).closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoStrabus()
    window.show()
    sys.exit(app.exec())
