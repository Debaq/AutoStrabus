import serial
import threading
import time

class SerialHandler:
    def __init__(self, port, baud_rate=115200):
        self.port = port
        self.baud_rate = baud_rate
        self.serial = None
        self.is_connected = False
        self.imu_data = {'pitch': 0, 'roll': 0, 'yaw': 0, 'left_occluder': False, 'right_occluder': False}
        self.device_info = {'name': '', 'version': ''}
        self.read_thread = None

    # ... (otros métodos se mantienen igual)

    def _read_imu_data(self):
        while self.is_connected:
            try:
                data = self.serial.readline().decode().strip()
                pitch, roll, yaw, left_occluder, right_occluder = map(float, data.split(','))
                self.imu_data = {
                    'pitch': pitch,
                    'roll': roll,
                    'yaw': yaw,
                    'left_occluder': bool(int(left_occluder)),
                    'right_occluder': bool(int(right_occluder))
                }
            except ValueError:
                pass  # Ignorar líneas mal formateadas
            time.sleep(0.01)  # Pequeña pausa para no saturar el CPU

    # ... (resto del código se mantiene igual)