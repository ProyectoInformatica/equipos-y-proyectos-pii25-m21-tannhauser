from models.sensores.simulador_sensores import SimuladorSensores
from models.file_manager import FileManager
from models.db import get_connection
from mysql.connector import Error
import threading
import time


class SensorController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Singleton: ensure only one controller (and simulator) exists
        if cls._instance is None:
            cls._instance = super(SensorController, cls).__new__(cls)
        return cls._instance

    def __init__(self, intervalo=5):
        # Prevent reinitialization on subsequent constructions
        if getattr(self, '_initialized', False):
            return
        self.simulador = SimuladorSensores(intervalo=intervalo)
        self.fm = FileManager()
        self._autosave_running = False
        self._autosave_thread = None
        self._autosave_interval = 60
        self._initialized = True

    def iniciar_simulacion(self, actor: str = None):
        if getattr(self.simulador, 'running', False):
            return "Simulación ya en ejecución"
        self.simulador.iniciar()
        try:
            who = actor if actor else 'SYSTEM'
            self.fm.registrar_actividad(who, 'START_SIMULACION')
        except Exception:
            pass
        return "Simulación iniciada"

    def detener_simulacion(self, actor: str = None):
        if not getattr(self.simulador, 'running', False):
            return "Simulación no está en ejecución"
        self.simulador.detener()
        try:
            who = actor if actor else 'SYSTEM'
            self.fm.registrar_actividad(who, 'STOP_SIMULACION')
        except Exception:
            pass
        return "Simulación detenida"

    def obtener_lecturas_actuales(self):
        return self.simulador.obtener_valores_actuales()

    def obtener_lecturas_historicas(self, nombre_sensor):
        return self.fm.leer_lecturas_sensor(nombre_sensor)

    def generar_lecturas_manual(self):
        datos = self.simulador.obtener_valores_actuales()
        if not any(datos.values()):
            for sensor in self.simulador.sensores:
                valor = sensor.generar_valor()
                self.fm.guardar_lectura_sensor(sensor.nombre, valor)
        return self.simulador.obtener_valores_actuales()

    def obtener_estados_actuales_db(self):
        conn = get_connection()
        if not conn:
            return {}

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    d.device_code,
                    cs.state_code,
                    cs.state_value,
                    cs.numeric_value,
                    cs.updated_at,
                    cs.source
                FROM current_state cs
                JOIN devices d ON d.id = cs.device_id
                ORDER BY cs.updated_at DESC
            """)
            rows = cursor.fetchall()

            estados = {
                "TEMP_AIR": None,
                "HUM_AIR": None,
                "MQ135_AIR": None,
                "DISTANCE_CM": None,
            }

            for row in rows:
                code = row["state_code"]
                if code in estados and estados[code] is None:
                    estados[code] = row

            return estados

        except Error as e:
            print(f"Error leyendo current_state: {e}")
            return {}

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    # -------------------------------------------------
    # Auto-save historical data periodically
    def iniciar_autoguardado(self, intervalo=60):
        """Inicia un hilo que guarda periódicamente las lecturas actuales en disco.
        """
        if self._autosave_running:
            return "Auto-guardado ya en ejecución"
        self._autosave_interval = int(intervalo)
        self._autosave_running = True
        self._autosave_thread = threading.Thread(target=self._autosave_loop, daemon=True)
        self._autosave_thread.start()
        return "Auto-guardado iniciado"

    def detener_autoguardado(self):
        if not self._autosave_running:
            return "Auto-guardado no estaba en ejecución"
        self._autosave_running = False
        if self._autosave_thread:
            self._autosave_thread.join(timeout=1)
            self._autosave_thread = None
        return "Auto-guardado detenido"

    def _autosave_loop(self):
        while self._autosave_running:
            try:
                datos = self.obtener_lecturas_actuales()
                # If no current readings exist, generate a manual set to ensure we store something
                if not datos or all(v is None for v in datos.values()):
                    datos = self.generar_lecturas_manual()
                for sensor, valor in (datos or {}).items():
                    if valor is None:
                        continue
                    # write the current value as a new historical entry
                    self.fm.guardar_lectura_sensor(sensor, valor)
            except Exception:
                # swallow errors to avoid crashing the thread and try again next cycle
                pass
            time.sleep(self._autosave_interval)

    def obtener_lista_sensores(self):
        return [sensor.nombre for sensor in self.simulador.sensores]

    def is_sim_running(self):
        return bool(getattr(self.simulador, 'running', False))