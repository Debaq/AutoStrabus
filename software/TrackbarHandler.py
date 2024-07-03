import cv2

def process_frame(frame, divider, detector, blur_size, threshold_value, min_contour_area):
    blur_size = int(blur_size) if int(blur_size) % 2 != 0 else int(blur_size) + 1
    threshold_value = int(threshold_value)
    min_contour_area = int(min_contour_area)

    # Dividir el frame en mitades izquierda y derecha
    left_half, right_half = divider.divide_frame(frame.copy())
    
    # Detectar pupilas en cada mitad
    left_pupil, right_pupil, step = detector.detect_pupils(left_half, right_half, blur_size, threshold_value, min_contour_area)

    # Dibujar resultados en el frame original
    height, width = frame.shape[:2]
    midline_x = width // 2
    cv2.line(frame, (midline_x, 0), (midline_x, height), (255, 255, 255), 2)  # Línea blanca en el centro

    cv2.line(frame, (0, 200), (1280, 200), (0, 255, 0), 1)  # Línea corte superior
    cv2.line(frame, (0, 500), (1280, 500), (0, 255, 0), 1)  # Línea corte inferior

    #_, frame = cv2.threshold(frame, threshold_value, 255, cv2.THRESH_BINARY)

    frame  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Cambio el orden de los colores

    if left_pupil and right_pupil:
        # Puntos centrales para las líneas
        left_center = (left_pupil[0][0], left_pupil[0][1])
        right_center = (right_pupil[0][0] + divider.width, right_pupil[0][1])

        # Dibujar líneas para las pupilas
        cv2.line(frame, (left_center[0], 0), (left_center[0], height), (255, 0, 0), 2)  # Línea azul para el ojo izquierdo
        cv2.line(frame, left_center, (midline_x, left_pupil[0][1]), (0, 255, 255), 2)

        cv2.line(frame, (right_center[0], 0), (right_center[0], height), (0, 0, 255), 2)  # Línea roja para el ojo derecho
        cv2.line(frame, right_center, (midline_x, right_pupil[0][1]), (0, 255, 255), 2)

        # Mostrar las distancias en píxeles
        distance_left = midline_x - left_center[0]
        distance_right = right_center[0] - midline_x

        cv2.putText(frame, f'{distance_left}px', (midline_x - distance_left // 2, left_pupil[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.putText(frame, f'{distance_right}px', (midline_x + distance_right // 2, right_pupil[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.putText(frame, f'{left_center[1]}px', (left_center[0] - 30, left_center[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, f'{right_center[1]}px', (right_center[0] - 30, right_center[1] // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)



    return frame, left_pupil, right_pupil


