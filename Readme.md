# AutoStrabus

AutoStrabus es un sistema innovador diseñado para la evaluación automática del estrabismo y los movimientos oculares. Utiliza tecnología de visión por computadora junto con gafas de video oculografía para detectar desviaciones oculares de forma precisa y eficiente.

## Características

- **Video Oculografía:** Incorpora gafas equipadas con una camara de alta velocidad para monitorear los movimientos oculares en tiempo real.
- **Análisis Automatizado:** Usa OpenCV para analizar los datos de video, identificando los centros ópticos y rastreando los movimientos oculares.
- **Control de Oclusión:** Implementa un ESP8266 para manejar dos válvulas de luz que actúan como oclusores automáticos durante las pruebas.
- **Detección de Movimientos Cefálicos:** Incluye un IMU para detectar cualquier desviación o torsión de la cabeza que pueda influir en los resultados de la prueba.

## Instalación

Para empezar a usar AutoStrabus, sigue estos pasos:

```
git clone https://github.com/tu_usuario/AutoStrabus.git
cd AutoStrabus
pip install PySide6
pip install opencv-python
python main.py

```



## Estructura del Proyecto

- Electrónica: Acá encontraras los esquematicos en Kicad para el diseño y construcción de la placa
- 3d model: acá encontraras los modelos 3d
- Firmware: Acá encontraras el firmware en Arduino para ESP8266
- Software: Aca encontrarás el software en para el PC
- BOM: acá encontraras los suministros que debes adquirir



## Contribuir

Este proyecto es open source y agradecemos cualquier contribución:

- Fork el repositorio.
- Crea una nueva rama (git checkout -b feature-nueva).
- Haz tus cambios y commit (git commit -am 'Añadir algo nuevo').
- Push a la rama (git push origin feature-nueva).
- Crea una nueva Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE.md para detalles.


## Contacto

Para más información, puedes contactar a
