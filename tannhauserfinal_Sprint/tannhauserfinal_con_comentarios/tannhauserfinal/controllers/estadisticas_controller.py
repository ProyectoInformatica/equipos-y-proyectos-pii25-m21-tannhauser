"""
Controlador para gestionar estadísticas de sensores.
Proporciona métodos para obtener, formatear y analizar datos de sensores.
Todos los datos provienen de los archivos JSON en data/sensores/
"""

from models.file_manager import FileManager
import logging
from datetime import datetime, timedelta

DEFAULT_POTENCIAS = {
    "sensor_temperatura": 0.5,  # W
    "sensor_humedad": 0.3,      # W
    "sensor_luz": 2.0,          # W
    "sensor_nevera": 100.0,     # W (ejemplo)
    "sensor_puerta": 0.1,       # W
}

logger = logging.getLogger(__name__)


class EstadisticasController:
    """Controlador centralizado para estadísticas de sensores"""
    
    def __init__(self):
        self.fm = FileManager()
    
    def obtener_todas_estadisticas(self):
        """
        Obtiene estadísticas de todos los sensores disponibles.
        
        Returns:
            dict: Diccionario con estadísticas de todos los sensores
        """
        return self.fm.obtener_estadisticas_sensores()
    
    def obtener_estadisticas(self, nombre_sensor):
        """
        Obtiene estadísticas detalladas de un sensor específico.
        
        Args:
            nombre_sensor: Nombre del sensor
            
        Returns:
            dict: Estadísticas del sensor
        """
        return self.fm.obtener_estadisticas_sensor_individual(nombre_sensor)
    
    def obtener_resumen_rapido(self):
        """
        Obtiene un resumen rápido del estado de todos los sensores.
        
        Returns:
            dict: Resumen con estado, última lectura y promedio de cada sensor
        """
        todas_stats = self.fm.obtener_estadisticas_sensores()
        resumen = {}
        
        for nombre_sensor, stats in todas_stats.items():
            if stats.get("estado") == "sin_datos":
                resumen[nombre_sensor] = {
                    "estado": "sin_datos",
                    "mensaje": "Sin datos disponibles"
                }
            else:
                resumen[nombre_sensor] = {
                    "estado": "operativo",
                    "total_lecturas": stats.get("total_lecturas"),
                    "ultima_lectura": stats.get("ultima_lectura", {}).get("valor"),
                    "timestamp_ultima": stats.get("ultima_lectura", {}).get("timestamp"),
                    "promedio": stats.get("promedio", stats.get("valores", [])),
                }
        
        return resumen
    
    def obtener_alertas(self):
        """
        Analiza los datos y retorna alertas de sensores anómalos.
        
        Returns:
            list: Lista de alertas detectadas
        """
        alertas = []
        todas_stats = self.fm.obtener_estadisticas_sensores()
        
        for nombre_sensor, stats in todas_stats.items():
            if stats.get("estado") == "sin_datos":
                alertas.append({
                    "sensor": nombre_sensor,
                    "tipo": "advertencia",
                    "mensaje": f"El sensor {nombre_sensor} no tiene datos registrados"
                })
            elif nombre_sensor == "sensor_temperatura":
                promedio = stats.get("promedio")
                if promedio and (promedio < 15 or promedio > 30):
                    alertas.append({
                        "sensor": nombre_sensor,
                        "tipo": "alerta",
                        "mensaje": f"Temperatura fuera de rango (promedio: {promedio}°C)"
                    })
            elif nombre_sensor == "sensor_humedad":
                promedio = stats.get("promedio")
                if promedio and (promedio < 30 or promedio > 90):
                    alertas.append({
                        "sensor": nombre_sensor,
                        "tipo": "alerta",
                        "mensaje": f"Humedad fuera de rango (promedio: {promedio}%)"
                    })
            elif nombre_sensor == "sensor_nevera":
                promedio = stats.get("promedio")
                if promedio and promedio > 5:
                    alertas.append({
                        "sensor": nombre_sensor,
                        "tipo": "alerta",
                        "mensaje": f"Temperatura de nevera alta (promedio: {promedio}°C)"
                    })
        
        return alertas
    
    def exportar_estadisticas_json(self, nombre_sensor=None):
        """
        Exporta estadísticas en formato JSON.
        
        Args:
            nombre_sensor: Si se especifica, exporta solo ese sensor
            
        Returns:
            dict o str: Datos en formato JSON
        """
        if nombre_sensor:
            return self.fm.obtener_estadisticas_sensor_individual(nombre_sensor)
        else:
            return self.fm.obtener_estadisticas_sensores()
    
    def obtener_comparativa_sensores(self):
        """
        Obtiene una comparativa entre sensores similares.
        
        Returns:
            dict: Comparativa agrupada por tipo
        """
        todas_stats = self.fm.obtener_estadisticas_sensores()
        comparativa = {}
        
        # Agrupar por tipo de sensor
        tipos = {
            "temperatura": ["sensor_temperatura", "sensor_nevera"],
            "humedad": ["sensor_humedad"],
            "luz": ["sensor_luz"],
            "puerta": ["sensor_puerta"]
        }
        
        for tipo, sensores in tipos.items():
            comparativa[tipo] = {}
            for sensor in sensores:
                if sensor in todas_stats:
                    comparativa[tipo][sensor] = todas_stats[sensor]
        
        return comparativa
    
    def verificar_conexion_archivos(self):
        """
        Verifica que todos los archivos JSON de sensores existan y tengan datos.
        
        Returns:
            dict: Estado de conexión de cada sensor
        """
        sensores_esperados = [
            "sensor_temperatura",
            "sensor_humedad",
            "sensor_luz",
            "sensor_nevera",
            "sensor_puerta"
        ]
        
        estado = {}
        
        for nombre_sensor in sensores_esperados:
            try:
                lecturas = self.fm.leer_lecturas_sensor(nombre_sensor)
                estado[nombre_sensor] = {
                    "conectado": True,
                    "archivo": f"data/sensores/{nombre_sensor}.json",
                    "total_registros": len(lecturas),
                    "ultimo_registro": lecturas[-1] if lecturas else None
                }
                logger.info(f"✓ {nombre_sensor}: {len(lecturas)} registros")
            except Exception as e:
                estado[nombre_sensor] = {
                    "conectado": False,
                    "archivo": f"data/sensores/{nombre_sensor}.json",
                    "error": str(e)
                }
                logger.error(f"✗ {nombre_sensor}: {str(e)}")
        
        return estado
    
    def obtener_ruta_archivos_sensores(self):
        """
        Retorna la ruta de los archivos JSON de sensores.
        
        Returns:
            dict: Rutas de cada archivo sensor
        """
        return {
            "directorio_base": self.fm.SENSORES_DIR,
            "sensores": {
                "temperatura": f"{self.fm.SENSORES_DIR}/sensor_temperatura.json",
                "humedad": f"{self.fm.SENSORES_DIR}/sensor_humedad.json",
                "luz": f"{self.fm.SENSORES_DIR}/sensor_luz.json",
                "nevera": f"{self.fm.SENSORES_DIR}/sensor_nevera.json",
                "puerta": f"{self.fm.SENSORES_DIR}/sensor_puerta.json",
            }
        }

    def obtener_consumo_ultimas_24h(self, potencia_por_sensor=None):
        """
        Calcula el consumo energético aproximado (Wh) de cada sensor en las últimas 24 horas.

        Args:
            potencia_por_sensor: dict opcional con potencias en W por nombre de sensor.

        Returns:
            dict: {sensor_nombre: consumo_wh}
        """
        potencia = DEFAULT_POTENCIAS.copy()
        if potencia_por_sensor:
            potencia.update(potencia_por_sensor)

        ahora = datetime.now()
        corte = ahora - timedelta(days=1)

        consumo = {}

        # Obtener archivos/lecturas
        todas_stats = self.fm.obtener_estadisticas_sensores()

        for nombre_sensor in todas_stats.keys():
            lecturas = self.fm.leer_lecturas_sensor(nombre_sensor)
            if not lecturas:
                consumo[nombre_sensor] = 0.0
                continue

            # Parsear timestamps y ordenar
            tiempos = []
            for l in lecturas:
                ts = l.get("timestamp")
                try:
                    tiempos.append(datetime.fromisoformat(ts))
                except Exception:
                    continue
            tiempos.sort()

            if not tiempos:
                consumo[nombre_sensor] = 0.0
                continue

            total_wh = 0.0
            # Si solo hay un timestamp dentro del periodo, asumimos un intervalo mínimo de 60s
            MIN_INTERVAL_SECONDS = 60

            # Recorremos intervalos entre tiempos consecutivos
            for i in range(len(tiempos)):
                t_start = tiempos[i]
                if i + 1 < len(tiempos):
                    t_end = tiempos[i + 1]
                else:
                    # Para la última lectura asumimos que mantiene hasta 'ahora'
                    t_end = ahora

                # Calcular solapamiento con ventana de últimas 24h
                inicio = max(t_start, corte)
                fin = min(t_end, ahora)
                segundos = (fin - inicio).total_seconds()
                if segundos <= 0:
                    continue

                # Evitar intervalos extremadamente cortos
                if segundos < MIN_INTERVAL_SECONDS:
                    segundos = MIN_INTERVAL_SECONDS

                potencia_w = potencia.get(nombre_sensor, 1.0)
                wh = potencia_w * (segundos / 3600.0)
                total_wh += wh

            consumo[nombre_sensor] = round(total_wh, 2)

            # Persistir en el JSON del sensor como campo meta.consumo_24h
            try:
                self.fm.guardar_consumo_sensor(nombre_sensor, consumo[nombre_sensor])
            except Exception:
                # No bloquear en caso de fallo de I/O
                logger.exception(f"No se pudo guardar consumo para {nombre_sensor}")

        return consumo
