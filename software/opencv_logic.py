import cv2
import json
from TrackbarHandler import process_frame
from FrameDivider import FrameDivider
from DetectPupil import PupilDetector

class OpenCVLogic:
    def __init__(self):
        self.divider = FrameDivider()
        self.detector = PupilDetector()
        self.blur_size = 0
        self.threshold_value = 0
        self.min_contour_area = 0
        self.frame_data = {}

    def set_params(self, blur_size, threshold_value, min_contour_area):
        self.blur_size = blur_size
        self.threshold_value = threshold_value
        self.min_contour_area = min_contour_area

    def process_frame(self, frame, frame_number):
        # Guardar el frame original antes de procesar
        original_frame = frame.copy()
        
        # Procesar el frame y obtener las marcas de las pupilas
        marked_frame, left_pupil, right_pupil = process_frame(frame, self.divider, self.detector, self.blur_size, self.threshold_value, self.min_contour_area)
        
        # Guardar las marcas en el diccionario
        self.frame_data[frame_number] = {
            "right_pupil": [[right_pupil[0][0] + self.divider.width, right_pupil[0][1]], 10] if right_pupil else [[], 0],
            "left_pupil": [[left_pupil[0][0], left_pupil[0][1]], 10] if left_pupil else [[], 0],
            "epicantos": [[], []]  # Vacío por ahora
        }

        return original_frame, marked_frame

    def save_marks_to_json(self, video_file = "output.avi", json_file = "output.json"):
        data = {
            "video_file": video_file,
            "json_file": json_file,
            "marks": self.frame_data,
            "midline": 640  # Valor constante por ahora
        }

        folder = "record"
        json_file = f"{folder}/{json_file}"
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
