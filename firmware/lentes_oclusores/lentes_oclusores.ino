#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>

// Definir los pines de los oclusores
#define lente_act_izq D5
#define lente_dct_izq D6
#define lente_act_der D7
#define lente_dct_der D8

#define BNO055_ADDRESS 0x29

// Crear el objeto BNO055
Adafruit_BNO055 bno = Adafruit_BNO055(55, BNO055_ADDRESS);

// Clase para manejar los oclusores
class Oclusor {
  private:
    unsigned long tiempoCerrado;
    unsigned long tiempoAbierto;
    bool cicloActivo;
    unsigned long tiempoAnterior;
    bool estado;
    bool oclusorIzqEncendido;
    bool oclusorDerEncendido;

  public:
    Oclusor() : tiempoCerrado(3000), tiempoAbierto(3000), cicloActivo(false), tiempoAnterior(0), estado(false), oclusorIzqEncendido(false), oclusorDerEncendido(false) {}

    void configurarTiempos(unsigned long tCerrado, unsigned long tAbierto) {
      tiempoCerrado = tCerrado;
      tiempoAbierto = tAbierto;
    }

    void iniciarCiclo() {
      cicloActivo = true;
      tiempoAnterior = millis();
      estado = true;
      actualizarEstado();
    }

    void detenerCiclo() {
      cicloActivo = false;
      actualizarEstado();
      apagarOclusor(1);
      apagarOclusor(0);

    }

    void actualizar() {
      if (cicloActivo) {
        unsigned long tiempoActual = millis();
        if (estado) {
          if (tiempoActual - tiempoAnterior >= tiempoCerrado) {
            estado = false;
            tiempoAnterior = tiempoActual;
            actualizarEstado();
          }
        } else {
          if (tiempoActual - tiempoAnterior >= tiempoAbierto) {
            estado = true;
            tiempoAnterior = tiempoActual;
            actualizarEstado();
          }
        }
      }
    }

    void actualizarEstado() {
      // Actualizar el estado del ciclo alternante de los oclusores
      if (estado) {
        encenderOclusor(1);
        apagarOclusor(0);
      } else {
        encenderOclusor(0);
        apagarOclusor(1);
      }
    }

    void encenderOclusor(int oclusor) {
      if (oclusor == 1) { // Izquierdo
        digitalWrite(lente_act_izq, HIGH);
        digitalWrite(lente_dct_izq, LOW);
        oclusorIzqEncendido = true;
      } else if (oclusor == 0) { // Derecho
        digitalWrite(lente_act_der, HIGH);
        digitalWrite(lente_dct_der, LOW);
        oclusorDerEncendido = true;
      }
    }

    void apagarOclusor(int oclusor) {
      if (oclusor == 1) { // Izquierdo
        digitalWrite(lente_act_izq, LOW);
        digitalWrite(lente_dct_izq, HIGH);
        oclusorIzqEncendido = false;
      } else if (oclusor == 0) { // Derecho
        digitalWrite(lente_act_der, LOW);
        digitalWrite(lente_dct_der, HIGH);
        oclusorDerEncendido = false;
      }
    }

    void apagarTodo(){
        digitalWrite(lente_act_der, LOW);
        digitalWrite(lente_dct_der, LOW);
        digitalWrite(lente_act_izq, LOW);
        digitalWrite(lente_dct_izq, LOW);
      }

    bool isOclusorIzqEncendido() {
      return oclusorIzqEncendido;
    }

    bool isOclusorDerEncendido() {
      return oclusorDerEncendido;
    }
};

Oclusor oclusor;

void setup() {
  pinMode(lente_act_izq, OUTPUT);
  pinMode(lente_dct_izq, OUTPUT);
  pinMode(lente_act_der, OUTPUT);
  pinMode(lente_dct_der, OUTPUT);

  Serial.begin(9600);
  
  if (!bno.begin()) {
    Serial.print("No se encontró BNO055");
    while (1);
  }
  bno.setExtCrystalUse(true);
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();
    if (comando.startsWith("T") && comando.indexOf("O") != -1) {
      int indice_O = comando.indexOf("O");
      String str_tiempo_cerrado = comando.substring(1, indice_O);
      String str_tiempo_abierto = comando.substring(indice_O + 1);

      unsigned long tiempo_cerrado = str_tiempo_cerrado.toInt() * 1000;
      unsigned long tiempo_abierto = str_tiempo_abierto.toInt() * 1000;

      oclusor.configurarTiempos(tiempo_cerrado, tiempo_abierto);

      Serial.print("OK");
      Serial.print(tiempo_cerrado / 1000);
      Serial.print("/");
      Serial.println(tiempo_abierto / 1000);
    } else if (comando.equals("OCLUON")) {
      oclusor.iniciarCiclo();
      Serial.println("OKCON");
    } else if (comando.equals("OCLUOFF")) {
      oclusor.detenerCiclo();
      Serial.println("OKCOFF");
    } else if (comando.startsWith("ON")) {
      int oclusorNum = comando.charAt(2) - '0';
      oclusor.encenderOclusor(oclusorNum);
    } else if (comando.startsWith("OFF")) {
      int oclusorNum = comando.charAt(3) - '0';
      oclusor.apagarOclusor(oclusorNum);
    }
  }

  oclusor.actualizar();

  // Leer y enviar los datos del sensor BNO055
  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  Serial.print(euler.x());
  Serial.print(";"); 
  Serial.print(euler.z());
  Serial.print(";"); 
  Serial.print(euler.y());
  Serial.print(";"); 
  Serial.print(oclusor.isOclusorDerEncendido());
  Serial.print(";"); 
  Serial.println(oclusor.isOclusorIzqEncendido());
  
  delay(100); // Actualización de datos cada 100 ms
}
