import cv2
import numpy as np

class PupilDetector:
    def __init__(self):
        pass

    def detect_pupils(self, left_half, right_half, blur_size, threshold_value, min_contour_area):
        # Detecta la pupila en cada mitad
        left_pupil, left_steps = self._detect_pupil(left_half, blur_size, threshold_value, min_contour_area)
        right_pupil, right_steps = self._detect_pupil(right_half, blur_size, threshold_value, min_contour_area)

        return left_pupil, right_pupil, left_steps + right_steps

    def _detect_pupil(self, half_frame, blur_size, threshold_value, min_contour_area):
        steps = []
        
        # Convertir a escala de grises
        gray = cv2.cvtColor(half_frame, cv2.COLOR_BGR2GRAY)
        steps.append(('Gray', gray))

        # Aplicar desenfoque gaussiano para reducir el ruido
        blurred = cv2.GaussianBlur(gray, (blur_size, blur_size), 2)
        steps.append(('Blurred', blurred))

        # Aplicar umbral adaptativo
        _, thresh = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY_INV)
        steps.append(('Threshold', thresh))

        # Encontrar contornos
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour_img = np.zeros_like(gray)
        cv2.drawContours(contour_img, contours, -1, (255, 255, 255), 1)
        steps.append(('Contours', contour_img))

        # Buscar el contorno con mayor área
        largest_contour = None
        max_area = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_contour_area and area > max_area:  # Filtrar áreas pequeñas
                max_area = area
                largest_contour = contour

        if largest_contour is not None and len(largest_contour) >= 5:
            # Ajustar una elipse al contorno
            ellipse = cv2.fitEllipse(largest_contour)
            (x, y), (major_axis, minor_axis), angle = ellipse
            center = (int(x), int(y))
            axes = (int(major_axis / 2), int(minor_axis / 2))

            return (center, axes, angle), steps

        return None, steps
