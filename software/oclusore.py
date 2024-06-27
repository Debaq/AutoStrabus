import cv2
import numpy as np

class Dibujante:
    def __init__(self, width, height):
        self.image = np.ones((height, width), dtype="uint8") * 255

    def dibujar_imagenes(self, centers, radius, line_length):
        for center in centers:
            cv2.circle(self.image, center, radius, (0, 0, 0), 2)
            cv2.line(self.image, (center[0], center[1] + radius), 
                     (center[0], center[1] + radius + line_length), (0, 0, 0), 2)

    def mostrar_imagen(self):
        cv2.imshow("Imagen", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Uso de la clase
dibujante = Dibujante(400, 400)
centers = [(100, 200), (300, 200)]  # Centros de los dos círculos
radius = 50  # Radio de los círculos
line_length = 80  # Longitud de las líneas

dibujante.dibujar_imagenes(centers, radius, line_length)
dibujante.mostrar_imagen()
