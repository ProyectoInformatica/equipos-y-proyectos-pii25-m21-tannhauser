from models.sensores.simulador_sensores import SimuladorSensores
from models.file_manager import FileManager
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
