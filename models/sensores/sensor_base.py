from abc import ABC, abstractmethod


class Sensor(ABC):
    """Clase abstracta para cualquier tipo de sensor"""

    def __init__(self, nombre_sensor):
        self.nombre = nombre_sensor
        self.valor_actual = None

    @abstractmethod
    def generar_valor(self):
        """Genera un valor simulado para el sensor"""
        pass

    def leer(self):
        """Devuelve el valor actual del sensor"""
        return self.valor_actual
