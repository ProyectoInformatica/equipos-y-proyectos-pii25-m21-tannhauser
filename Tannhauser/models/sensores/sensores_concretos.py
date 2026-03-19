from random import uniform, randint, choice
from .sensor_base import Sensor


class SensorTemperatura(Sensor):
    def __init__(self):
        super().__init__("sensor_temperatura")

    def generar_valor(self):
        self.valor_actual = round(uniform(18.0, 28.0), 2)
        return self.valor_actual


class SensorHumedad(Sensor):
    def __init__(self):
        super().__init__("sensor_humedad")

    def generar_valor(self):
        self.valor_actual = randint(40, 90)
        return self.valor_actual


class SensorLuz(Sensor):
    def __init__(self):
        super().__init__("sensor_luz")

    def generar_valor(self):
        self.valor_actual = randint(0, 100)
        return self.valor_actual


class SensorNevera(Sensor):
    def __init__(self):
        super().__init__("sensor_nevera")

    def generar_valor(self):
        self.valor_actual = round(uniform(1.0, 8.0), 2)
        return self.valor_actual


class SensorPuerta(Sensor):
    def __init__(self):
        super().__init__("sensor_puerta")

    def generar_valor(self):
        self.valor_actual = choice(["abierta", "cerrada"])
        return self.valor_actual
