import sys
import cv2
import serial
import serial.tools.list_ports
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QVBoxLayout, QWidget

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.resize(640, 480)

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(self.get_available_cameras())
        self.combo_box.currentIndexChanged.connect(self.select_camera)

        self.serial_combo_box = QComboBox(self)
        self.serial_combo_box.addItems(self.get_available_serial_ports())

        self.baudrate_combo_box = QComboBox(self)
        self.baudrate_combo_box.addItems(["9600", "19200", "38400", "57600", "115200"])

        self.test_button = QPushButton("Versión de prueba", self)
        self.test_button.clicked.connect(self.send_test_command)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.serial_combo_box)
        self.layout.addWidget(self.baudrate_combo_box)
        self.layout.addWidget(self.test_button)
        self.layout.addWidget(self.image_label)

        self.setLayout(self.layout)

        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.select_camera(0)

    def get_available_cameras(self):
        # Check for available cameras
        available_cameras = []
        for i in range(5):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available_cameras.append(f"Camera {i}")
                cap.release()
        return available_cameras

    def get_available_serial_ports(self):
        # Get a list of available serial ports
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def select_camera(self, index):
        if self.cap:
            self.cap.release()
        self.cap = cv2.VideoCapture(index)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            step = channel * width
            q_img = QImage(image.data, width, height, step, QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(q_img))

    def send_test_command(self):
        port = self.serial_combo_box.currentText()
        baudrate = self.baudrate_combo_box.currentText()
        if port and baudrate:
            try:
                ser = serial.Serial(port, baudrate, timeout=1)
                ser.write(b'TEST\n')
                ser.close()
            except serial.SerialException as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = CameraApp()
    viewer.show()
    sys.exit(app.exec())
