import threading
import time
from datetime import datetime
import logging

from models.file_manager import FileManager
from .sensores_concretos import (
    SensorTemperatura,
    SensorHumedad,
    SensorLuz,
    SensorNevera,
    SensorPuerta,
)

# Configurar logging para el simulador
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SimuladorSensores:
    def __init__(self, intervalo=5, intervalo_almacenamiento=30):
        """
        Inicializa el simulador de sensores.
        
        Args:
            intervalo: Tiempo entre lecturas de sensores (segundos)
            intervalo_almacenamiento: Tiempo entre almacenamientos periódicos (segundos)
        """
        self.intervalo = intervalo
        self.intervalo_almacenamiento = intervalo_almacenamiento
        self.fm = FileManager()
        self.sensores = [
            SensorTemperatura(),
            SensorHumedad(),
            SensorLuz(),
            SensorNevera(),
            SensorPuerta(),
        ]
        self.running = False
        self.thread = None
        self.buffer_lecturas = []  # Buffer para almacenar lecturas antes de guardarlas
        self.ultimo_almacenamiento = time.time()

    def iniciar(self):
        """Inicia el simulador en un thread independiente"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._loop, daemon=True)
            self.thread.start()
            logger.info(f"Simulador de sensores iniciado. Intervalo: {self.intervalo}s, "
                       f"Almacenamiento: {self.intervalo_almacenamiento}s")

    def _ensure_buffer_is_list(self):
        """
        Asegura que `self.buffer_lecturas` sea una lista. Si no lo es, lo registra y lo restablece.
        Esto previene errores cuando algún otro código accidentalmente reasigna el buffer.
        """
        if not isinstance(self.buffer_lecturas, list):
            try:
                logger.warning(f"buffer_lecturas no es lista (tipo={type(self.buffer_lecturas)}). Restableciendo.")
                # intentar conservar lecturas si es un dict con clave 'lecturas'
                if isinstance(self.buffer_lecturas, dict) and 'lecturas' in self.buffer_lecturas:
                    posibles = self.buffer_lecturas.get('lecturas')
                    if isinstance(posibles, list):
                        self.buffer_lecturas = posibles
                        return
                # en caso contrario, banalmente resetear a lista vacía
                self.buffer_lecturas = []
            except Exception:
                self.buffer_lecturas = []

    def detener(self):
        """Detiene el simulador y guarda los datos pendientes"""
        if self.running:
            self.running = False
            # Guardar datos pendientes
            self._almacenar_datos_periodicamente(forzar=True)
            # intentar unir el hilo para un apagado ordenado
            try:
                if self.thread and self.thread.is_alive():
                    self.thread.join(timeout=2)
            except Exception:
                pass
            logger.info("Simulador de sensores detenido")

    def _loop(self):
        """Loop principal del simulador"""
        while self.running:
            try:
                # Generar valores de todos los sensores
                for sensor in self.sensores:
                    valor = sensor.generar_valor()
                    # Agregar al buffer junto con el timestamp
                    lectura = {
                        "sensor": sensor.nombre,
                        "valor": valor,
                        "timestamp": datetime.now().isoformat()
                    }
                    # proteger contra buffer malformado
                    self._ensure_buffer_is_list()
                    self.buffer_lecturas.append(lectura)
                    # Guardar inmediatamente para que esté disponible
                    self.fm.guardar_lectura_sensor(sensor.nombre, valor)
                
                # Verificar si es necesario almacenar los datos
                tiempo_actual = time.time()
                if (tiempo_actual - self.ultimo_almacenamiento) >= self.intervalo_almacenamiento:
                    self._almacenar_datos_periodicamente()
                
                time.sleep(self.intervalo)
            except Exception as e:
                logger.error(f"Error en el loop del simulador: {e}")

    def _almacenar_datos_periodicamente(self, forzar=False):
        """
        Almacena los datos del buffer de forma periódica.
        
        Args:
            forzar: Si True, almacena incluso si el buffer está vacío
        """
        if not self.buffer_lecturas and not forzar:
            return
        
        try:
            # Asegurar que buffer sea una lista antes de iterar
            self._ensure_buffer_is_list()
            for lectura in list(self.buffer_lecturas):
                self.fm.guardar_lectura_sensor(lectura["sensor"], lectura["valor"])
            
            if self.buffer_lecturas:
                logger.info(f"Almacenadas {len(self.buffer_lecturas)} lecturas de sensores")
                # limpiar de forma segura
                self.buffer_lecturas = []
            
            self.ultimo_almacenamiento = time.time()
        except Exception as e:
            logger.error(f"Error al almacenar datos de sensores: {e}")

    def obtener_valores_actuales(self):
        """Retorna los valores actuales de todos los sensores"""
        return {sensor.nombre: sensor.valor_actual for sensor in self.sensores}
    
    def obtener_estadisticas(self):
        """
        Retorna estadísticas sobre los datos almacenados de cada sensor.
        
        Returns:
            dict: Diccionario con estadísticas por sensor
        """
        estadisticas = {}
        for sensor in self.sensores:
            lecturas = self.fm.leer_lecturas_sensor(sensor.nombre)
            if lecturas:
                valores = [l["valor"] for l in lecturas if isinstance(l.get("valor"), (int, float))]
                if valores:
                    estadisticas[sensor.nombre] = {
                        "total_lecturas": len(lecturas),
                        "valor_minimo": min(valores),
                        "valor_maximo": max(valores),
                        "valor_promedio": sum(valores) / len(valores),
                        "ultima_lectura": lecturas[-1].get("valor"),
                        "timestamp_ultima": lecturas[-1].get("timestamp")
                    }
            else:
                estadisticas[sensor.nombre] = {
                    "total_lecturas": 0,
                    "mensaje": "Sin datos disponibles"
                }
        return estadisticas
