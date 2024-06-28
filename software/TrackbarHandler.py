import cv2

def process_frame(frame, divider, detector, blur_size, threshold_value, min_contour_area):
    blur_size = int(blur_size) if int(blur_size) % 2 != 0 else int(blur_size) + 1
    threshold_value = int(threshold_value)
    min_contour_area = int(min_contour_area)

    # Actualizar la detección de pupilas con los valores actuales de los sliders
    left_half, right_half = divider.divide_frame(frame.copy())
    left_pupil, right_pupil, _ = detector.detect_pupils(left_half, right_half, blur_size, threshold_value, min_contour_area)
    

    # Dibujar los resultados en el frame original
    height, width = frame.shape[:2]
    midline_x = width // 2
    cv2.line(frame, (midline_x, 0), (midline_x, height), (255, 255, 255), 2)  # Línea blanca en el centro

    cv2.line(frame, (0, 200), (1280, 200), (0, 255, 0), 1)  # Línea blanca en el centro
    cv2.line(frame, (0, 500), (1280, 500), (0, 255, 0), 1)  # Línea blanca en el centro

    if left_pupil and right_pupil:
        # Calcular la altura promedio
        avg_y = (left_pupil[0][1] + right_pupil[0][1]) // 2
        left = left_pupil[0][1]
        right = right_pupil[0][1]
        # Línea azul para el ojo izquierdo
        left_center = (left_pupil[0][0], avg_y)
        cv2.line(frame, (left_center[0], 0), (left_center[0], height), (255, 0, 0), 2)
        cv2.line(frame, left_center, (midline_x, left), (0, 255, 255), 2)

        # Línea roja para el ojo derecho
        right_center = (right_pupil[0][0] + divider.width, avg_y)
        cv2.line(frame, (right_center[0], 0), (right_center[0], height), (0, 0, 255), 2)
        cv2.line(frame, right_center, (midline_x, right), (0, 255, 255), 2)

        # Mostrar la distancia en píxeles
        distance_left = midline_x - left_center[0]
        distance_right = right_center[0] - midline_x
        distance_left_top = left_center[1]
        distance_right_top = right_center[1]

        cv2.putText(frame, f'{distance_left}px', (midline_x - distance_left // 2, avg_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.putText(frame, f'{distance_right}px', (midline_x + distance_right // 2, avg_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.putText(frame, f'{distance_left_top}px', (left_center[0] - 30, left_center[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, f'{distance_right_top}px', (right_center[0] - 30, right_center[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return frame, left_pupil, right_pupil
