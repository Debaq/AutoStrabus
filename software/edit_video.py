import sys
import json
import os
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSlider, QFileDialog
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap, QMouseEvent

class VideoEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.video_label = QLabel(self)
        self.video_label.setFixedSize(1280, 720)
        self.video_label.mousePressEvent = self.mouse_event
        self.video_label.wheelEvent = self.wheel_event

        self.save_button = QPushButton("Save Marks", self)
        self.save_button.clicked.connect(self.save_marks)

        self.timeline_slider = QSlider(Qt.Horizontal, self)
        self.timeline_slider.setMinimum(0)
        self.timeline_slider.valueChanged.connect(self.slider_changed)

        self.right_pupil_button = QPushButton("Right Pupil", self)
        #self.right_pupil_button.setCheckable(True)
        self.right_pupil_button.clicked.connect(lambda: self.set_tool("right_pupil"))

        self.left_pupil_button = QPushButton("Left Pupil", self)
        #self.left_pupil_button.setCheckable(True)
        self.left_pupil_button.clicked.connect(lambda: self.set_tool("left_pupil"))

        self.epicantos_button = QPushButton("Epicantos", self)
        #self.epicantos_button.setCheckable(True)
        self.epicantos_button.clicked.connect(lambda: self.set_tool("epicantos"))

        self.midline_button = QPushButton("Midline", self)
        #self.midline_button.setCheckable(True)
        self.midline_button.clicked.connect(lambda: self.set_tool("midline"))
        
        tools_layout = QVBoxLayout()
        tools_layout.addWidget(self.right_pupil_button)
        tools_layout.addWidget(self.left_pupil_button)
        tools_layout.addWidget(self.epicantos_button)
        tools_layout.addWidget(self.midline_button)
        tools_layout.addWidget(self.save_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.timeline_slider)

        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(tools_layout)
        
        self.setLayout(main_layout)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)
        
        self.video_capture = None
        self.video_writer = None
        self.total_frames = 0
        self.current_frame = 0
        self.marks = {}
        self.points = []
        self.current_frame_frame = None
        self.tool = None
        self.right_pupil_circle = None
        self.left_pupil_circle = None
        self.right_pupil_radius = 20
        self.left_pupil_radius = 20
        self.midline = None
        self.video_file_path = None
        self.json_file_path = None


    def next_frame(self):
        if self.video_capture and self.video_capture.isOpened():
            print(self.current_frame)
            ret, frame = self.video_capture.read()
            if ret:
                self.current_frame += 1
                self.timeline_slider.setValue(self.current_frame)
                self.display_frame(frame)
            else:
                print("stop")
                self.timer.stop()
    
    def load_video(self, file_name=None):
        if not file_name:
            file_name, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if file_name:
            self.video_capture = cv2.VideoCapture(file_name)
            self.video_file_path = file_name
            self.total_frames = int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
            self.timeline_slider.setMaximum(self.total_frames - 1)
            #self.timer.start(30)
            self.slider_changed(0)
            self.load_marks(file_name)

    
    def load_marks(self, video_file_name):
        json_file_name = os.path.splitext(video_file_name)[0] + '.json'
        if os.path.exists(json_file_name):
            with open(json_file_name, 'r') as f:
                data = json.load(f)
                self.marks = data.get('marks', {})
                self.midline = data.get('midline', None)
                self.json_file_path = json_file_name

    def slider_changed(self, value):
        if self.video_capture and self.video_capture.isOpened():
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, value)
            self.current_frame = value
            ret, frame = self.video_capture.read()
            if ret:
                self.display_frame(frame)
    
    def display_frame(self, frame):
        self.current_frame_frame = frame.copy()

        frame_marks = self.marks.get(self.current_frame)
        if frame_marks is None:
            # Si no se encuentra, intentar obtener la clave como cadena
            frame_marks = self.marks.get(str(self.current_frame), {})
        if 'right_pupil' in frame_marks:
            center, radius = frame_marks['right_pupil']
            if center and radius:
                cv2.circle(frame, center, radius, (0, 0, 255), 2)
                cv2.circle(frame, center, 2, (0, 0, 255), -1)
                if self.midline:
                    cv2.line(frame, center, (self.midline, center[1]), (0, 0, 255), 1)
        
        if 'left_pupil' in frame_marks:
            center, radius = frame_marks['left_pupil']
            if center and radius:
                cv2.circle(frame, center, radius, (255, 0, 0), 2)
                cv2.circle(frame, center, 2, (255, 0, 0), -1)
                if self.midline:
                    cv2.line(frame, center, (self.midline, center[1]), (255, 0, 0), 1)
        
        if 'epicantos' in frame_marks:
            point1, point2 = frame_marks['epicantos']
            if point1 and point2:
                cv2.circle(frame, point1, 5, (0, 255, 0), -1)
                cv2.circle(frame, point2, 5, (0, 255, 0), -1)
                cv2.line(frame, point1, point2, (0, 255, 0), 2)
                midpoint = ((point1[0] + point2[0]) // 2, (point1[1] + point2[1]) // 2)
                distance = np.linalg.norm(np.array(point1) - np.array(point2))
                cv2.putText(frame, f"{distance:.2f}px", midpoint, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        if self.midline:
            cv2.line(frame, (self.midline, 0), (self.midline, frame.shape[0]), (255, 255, 255), 1)

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(1280, 720, Qt.KeepAspectRatio)
        self.video_label.setPixmap(QPixmap.fromImage(p))

    def set_tool(self, tool_name):
        self.tool = tool_name
        #self.right_pupil_button.setChecked(tool_name == "right_pupil")
        #self.left_pupil_button.setChecked(tool_name == "left_pupil")
        #self.epicantos_button.setChecked(tool_name == "epicantos")
        #self.midline_button.setChecked(tool_name == "midline")
    
    def mouse_event(self, event: QMouseEvent):
        x = event.pos().x()
        y = event.pos().y()
        if self.current_frame_frame is not None:
            if self.tool == "right_pupil":
                self.right_pupil_circle = (x, y)
                self.marks.setdefault(self.current_frame, {})['right_pupil'] = ((x, y), self.right_pupil_radius)
            elif self.tool == "left_pupil":
                self.left_pupil_circle = (x, y)
                self.marks.setdefault(self.current_frame, {})['left_pupil'] = ((x, y), self.left_pupil_radius)
            elif self.tool == "epicantos":
                if len(self.points) < 2:
                    self.points.append((x, y))
                    if len(self.points) == 2:
                        self.marks.setdefault(self.current_frame, {})['epicantos'] = (self.points[0], self.points[1])
                        self.points = []
            elif self.tool == "midline":
                self.midline = x
            self.display_frame(self.current_frame_frame) #acá dibuja las marcas


    def wheel_event(self, event):
        if self.tool == "right_pupil" and self.right_pupil_circle:
            self.right_pupil_radius += (1 if event.angleDelta().y() > 0 else -1)
            self.right_pupil_radius = max(1, self.right_pupil_radius)
            self.marks.setdefault(self.current_frame, {})['right_pupil'] = (self.right_pupil_circle, self.right_pupil_radius)
        elif self.tool == "left_pupil" and self.left_pupil_circle:
            self.left_pupil_radius += (1 if event.angleDelta().y() > 0 else -1)
            self.left_pupil_radius = max(1, self.left_pupil_radius)
            self.marks.setdefault(self.current_frame, {})['left_pupil'] = (self.left_pupil_circle, self.left_pupil_radius)
        self.display_frame(self.current_frame_frame)

    def save_marks(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Marks", "", "JSON Files (*.json)")
        if file_name:
            video_file_name = os.path.splitext(file_name)[0] + '.avi'
            os.rename(self.video_file_path, video_file_name)
            self.video_file_path = video_file_name
            data = {
                'video_file': os.path.basename(video_file_name),
                'json_file': os.path.basename(file_name),
                'marks': self.marks,
                'midline': self.midline
            }
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.timeline_slider.setValue(self.timeline_slider.value() + 1)
        elif event.key() == Qt.Key_Left:
            self.timeline_slider.setValue(self.timeline_slider.value() - 1)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QWidget()
    video_editor = VideoEditor()
    main_layout = QVBoxLayout(main_window)
    main_layout.addWidget(video_editor)
    main_window.show()
    sys.exit(app.exec())
