from pathlib import Path
import os

from models.activity_log_manager import ActivityLogManager
from models.sensor_data_manager import SensorDataManager


class FileManager:
    BASE_PATH = "data"
    SENSORES_DIR = os.path.join(BASE_PATH, "sensores")

    def __init__(self):
        possible_dirs = []
        try:
            base_here = Path(__file__).resolve().parents[2]
            possible_dirs.append(base_here / "data" / "sensores")
            possible_dirs.append(base_here / "tannhauserfinal" / "data" / "sensores")
            possible_dirs.append(Path(__file__).resolve().parents[3] / "data" / "sensores")
        except Exception:
            possible_dirs = []

        found = None
        for p in possible_dirs:
            try:
                if p.exists() and p.is_dir():
                    found = str(p)
                    break
            except Exception:
                continue

        if found:
            self.SENSORES_DIR = found
            self.BASE_PATH = str(Path(found).parents[0])
        else:
            self.SENSORES_DIR = FileManager.SENSORES_DIR
            self.BASE_PATH = FileManager.BASE_PATH

        self.log_manager = ActivityLogManager()
        self.sensor_manager = SensorDataManager()
        self._crear_directorios()

    def _crear_directorios(self):
        os.makedirs(self.BASE_PATH, exist_ok=True)
        os.makedirs(self.SENSORES_DIR, exist_ok=True)

    # --------- LOGS DE ACTIVIDAD (MYSQL) ---------
    def registrar_actividad(self, usuario, accion):
        self.log_manager.registrar(usuario, accion)

    # --------- SENSORES (MYSQL) ---------
    def guardar_lectura_sensor(self, nombre_sensor, valor):
        self.sensor_manager.guardar_lectura_sensor(nombre_sensor, valor, source="simulado")

    def guardar_lecturas_sensores_lote(self, lecturas):
        self.sensor_manager.guardar_lecturas_lote(lecturas, source="simulado")

    def leer_lecturas_sensor(self, nombre_sensor):
        return self.sensor_manager.leer_lecturas_sensor(nombre_sensor)

    def guardar_consumo_sensor(self, nombre_sensor, consumo_wh):
        self.sensor_manager.guardar_consumo_sensor(nombre_sensor, consumo_wh)

    def limpiar_lecturas_antiguas(self, nombre_sensor, max_registros=1000):
        # Ya no hace falta limpiar archivos JSON; se mantiene por compatibilidad.
        return

    def obtener_estadisticas_sensores(self):
        return self.sensor_manager.obtener_estadisticas_sensores()

    def obtener_estadisticas_sensor_individual(self, nombre_sensor):
        return self.sensor_manager.obtener_estadisticas_sensor_individual(nombre_sensor)