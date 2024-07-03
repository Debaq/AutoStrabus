import cv2
import numpy as np

def detect_pupil(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=100,
        param2=30,
        minRadius=5,
        maxRadius=50
    )
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)
        return frame, (x, y)
    return frame, None

def main():
    cap = cv2.VideoCapture(2)  # Usar la webcam con índice 2
    
    if not cap.isOpened():
        print("No se pudo abrir la webcam.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo capturar el frame.")
            break
        
        frame, pupil_position = detect_pupil(frame)
        
        if pupil_position:
            x, y = pupil_position
            cv2.putText(frame, f"Pupila: ({x}, {y})", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow("Detección de Pupila", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()