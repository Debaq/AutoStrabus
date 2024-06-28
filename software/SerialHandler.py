import serial
import threading
import time

class SerialHandler:
    def __init__(self, port, baud_rate=115200):
        self.port = port
        self.baud_rate = baud_rate
        self.serial = None
        self.is_connected = False
        self.imu_data = {'pitch': 0, 'roll': 0, 'yaw': 0, 'bool1': False, 'bool2': False}
        self.device_info = {'name': '', 'version': ''}
        self.read_thread = None

    def connect(self):
        try:
            self.serial = serial.Serial(self.port, self.baud_rate, timeout=1)
            self.is_connected = True
            self._read_device_info()
            self.read_thread = threading.Thread(target=self._read_imu_data)
            self.read_thread.start()
            return True
        except serial.SerialException as e:
            print(f"Error connecting to serial port: {e}")
            return False

    def disconnect(self):
        if self.is_connected:
            self.is_connected = False
            if self.read_thread:
                self.read_thread.join()
            self.serial.close()

    def _read_device_info(self):
        if self.is_connected:
            # Leer la información del dispositivo
            device_info = self.serial.readline().decode().strip()
            name, version = device_info.split(',')
            self.device_info['name'] = name
            self.device_info['version'] = version

    def _read_imu_data(self):
        while self.is_connected:
            try:
                data = self.serial.readline().decode().strip()
                pitch, roll, yaw, bool1, bool2 = map(float, data.split(','))
                self.imu_data = {
                    'pitch': pitch,
                    'roll': roll,
                    'yaw': yaw,
                    'bool1': bool(int(bool1)),
                    'bool2': bool(int(bool2))
                }
            except ValueError:
                pass  # Ignorar líneas mal formateadas
            time.sleep(0.01)  # Pequeña pausa para no saturar el CPU

    def get_imu_data(self):
        return self.imu_data

    def get_device_info(self):
        return self.device_info

    def send_shutter_command(self, t_time, o_time):
        if self.is_connected:
            command = f"T{t_time:04d}O{o_time:04d}"
            self.serial.write(command.encode())

    def send_occluder_command(self, action, side):
        if self.is_connected:
            command = f"{'ON' if action == 'on' else 'OFF'}{1 if side == 'right' else 0}"
            self.serial.write(command.encode())

# Ejemplo de uso
if __name__ == "__main__":
    handler = SerialHandler("COM3")  # Ajusta el puerto según tu sistema
    if handler.connect():
        print(f"Connected to device: {handler.get_device_info()}")
        
        # Ejemplo de lectura de datos IMU
        for _ in range(10):
            print(handler.get_imu_data())
            time.sleep(0.5)
        
        # Ejemplo de envío de comandos
        handler.send_shutter_command(50, 75)
        handler.send_occluder_command('on', 'left')
        time.sleep(1)
        handler.send_occluder_command('off', 'left')
        
        handler.disconnect()
    else:
        print("Failed to connect")