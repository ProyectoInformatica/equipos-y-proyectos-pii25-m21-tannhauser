import serial
import time
# Importamos el FileManager en lugar de los modelos directamente
from file_manager import FileManager

class SensoresController:
    def __init__(self, puerto='COM3', baudrate=115200):
        self.puerto = puerto
        self.baudrate = baudrate
        self.esp32 = None
        self.pines_asignados = []
        
        # Instanciamos tu gestor central de archivos y BBDD
        self.fm = FileManager()

    def inicializarSensor(self, pines):
        """Recibe los pines lógicos e inicia la conexión con ESP32."""
        self.pines_asignados = pines
        try:
            self.esp32 = serial.Serial(self.puerto, self.baudrate, timeout=1)
            time.sleep(2)
            print(f"Sensor inicializado en pines: {self.pines_asignados}")
        except Exception as e:
            print(f"Error al inicializar el ESP32: {e}")

    def comprobarDatosDisponibles(self):
        """Devuelve True si hay datos en el puerto serie."""
        if self.esp32 and self.esp32.is_open:
            return self.esp32.in_waiting > 0
        return False

    def leerDatosOrdinarios(self):
        """Devuelve [int, char] leyendo del ESP32."""
        try:
            dato_crudo = self.esp32.readline().decode('utf-8').strip()
            if dato_crudo:
                partes = dato_crudo.split(',')
                if len(partes) == 2:
                    return [int(partes[0]), partes[1][0]]
        except Exception as e:
            print(f"Error de lectura: {e}")
        return []

    def ejecutar_ciclo_lectura(self):
        """Función que unifica el proceso para que lo llame tu Vista."""
        if self.comprobarDatosDisponibles():
            datos_sensor = self.leerDatosOrdinarios()
            
            if datos_sensor and len(datos_sensor) == 2:
                # Usamos el FileManager para cumplir con "DatabaseInsert()"
                self.fm.DatabaseInsert("Sensor_Especial_ESP32", datos_sensor[0], datos_sensor[1])
                print(f"Guardado: {datos_sensor}")
                return datos_sensor
        return None