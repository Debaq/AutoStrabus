# AutoStrabus

AutoStrabus es un sistema innovador diseñado para la evaluación automática del estrabismo y los movimientos oculares. Utiliza tecnología de visión por computadora junto con gafas de video oculografía para detectar desviaciones oculares de forma precisa y eficiente.

## Tabla de Contenidos
 [Introducción](#Autostrabus)
   - [Características](#Características)
   - [Instalación](#Instalación)
   - [Estructura del proyecto]
   - [Contribuir](#Contribuir)
   - [Licencia](#Licencia)
   - [Contacto](#Contacto)


## Características

- **Video Oculografía:** Incorpora gafas equipadas con una camara de alta velocidad para monitorear los movimientos oculares en tiempo real.
- **Análisis Automatizado:** Usa OpenCV para analizar los datos de video, identificando los centros ópticos y rastreando los movimientos oculares.
- **Control de Oclusión:** Implementa un ESP8266 para manejar dos válvulas de luz que actúan como oclusores automáticos durante las pruebas.
- **Detección de Movimientos Cefálicos:** Incluye un IMU para detectar cualquier desviación o torsión de la cabeza que pueda influir en los resultados de la prueba.
 ## Partes del equipo
![Sistema optoclopadores ](https://github.com/NicoAguilera7/AutoStrabus/assets/169829886/dd2d0c4c-2f4a-4908-826d-58f713a9faac)
>Optocoplador: Un optoacoplador, también conocido como optoaislador, es un dispositivo electrónico que combina un componente emisor de luz (generalmente un diodo emisor de luz o LED) y un componente detector de luz (generalmente un fotodiodo, un fototransistor o un fototriac) dentro de un único encapsulado. Su función principal es proporcionar un aislamiento eléctrico entre dos partes de un circuito eléctrico, permitiendo la transmisión de señales o el control de dispositivos sin una conexión eléctrica directa.
![Controlador ESP8266MOD](https://github.com/NicoAguilera7/AutoStrabus/assets/169829886/efb8b195-e4f2-4717-b48d-570b2e7591f9)
>Controlador ESP8266MOD: El controlador ESP8266MOD es un microcontrolador integrado que ofrece conectividad Wi-Fi incorporada en un solo chip. Diseñado por Espressif Systems, este chip compacto integra un procesador de aplicación, memoria flash y un transceptor Wi-Fi en un paquete único. El objetivo principal es dar acceso a cualquier microcontrolador a una red.
![BNO(GY-BNOO55)](https://github.com/NicoAguilera7/AutoStrabus/assets/169829886/89754a8f-7ea3-414a-85c0-359307acdc89)
>BNO(GY-BN0055):
>El GY-BNO es un módulo sensor que incluye un sensor de orientación y movimiento de tres ejes llamado BNO055. Este sensor es capaz de proporcionar información precisa sobre la orientación absoluta, la velocidad angular y la aceleración lineal en tiempo real
![Tarjeta verde ](https://github.com/NicoAguilera7/AutoStrabus/assets/169829886/4b93e539-cd3d-4fde-804f-54ba116cb3a5)
>Hub: En un circuito, un hub es un dispositivo que actúa como punto central para conectar múltiples dispositivos. Funciona como un concentrador de conexiones, permitiendo que varios dispositivos se conecten entre sí y compartan información dentro de una red local. Básicamente, un hub recibe datos de un dispositivo y los retransmite a todos los demás dispositivos conectados a é
>Circuito 
![Valvulas de cristal liquido con luz ](https://github.com/Debaq/AutoStrabus/assets/169829886/5cebd9d5-8cd1-4f49-9892-33407047423e)
>Valvulas de cristal liquido con luz 
![Cámara ](https://github.com/NicoAguilera7/AutoStrabus/assets/169829886/c6b0733c-15bf-4b93-b498-465aea8d13d1)
````
Cámara 
 ![Correa elite reemplazable para auriculares Meta Quest 3 VR ](https://github.com/NicoAguilera7/AutoStrabus/assets/169829886/af914f44-46ff-4074-a7b1-fb81df7decc0)
````
 Correa elite remplazable para auriculares Meta Quest 3 VR
 ![Soporte sistema eléctrico ](https://github.com/NicoAguilera7/AutoStrabus/assets/169829886/3a9b26a6-eefd-4fdf-a590-4098161d2744)
 Soporte sistema eléctrico 
## Funcionamiento 
> Funcionamiento valvulas de cristal liquido con luz
![Funcionamiento valvulas de cristal liquido con luz](https://github.com/Debaq/AutoStrabus/assets/169829886/c4b7896e-23f7-4772-8a42-231adaf0d559)
```
Para esto 


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
- Crea una nueva rama.
- Haz tus cambios y commit.
- Push a la rama.
- Crea una nueva Pull Request.
- Estamos ansisosos por ver tus propuestas.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE.md para detalles.


## Contacto

Para más información, puedes contactar a david.avila@uach.cl



