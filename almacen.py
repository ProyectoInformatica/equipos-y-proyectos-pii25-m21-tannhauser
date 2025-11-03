import json
from typing import List, Optional
from models.sensor import Sensor


class Almacen:
    """Clase para representar un almacén que contiene sensores.
    Proporciona operaciones básicas: añadir, eliminar, buscar y listar sensores.
    """

    def __init__(self, nombre: str, ubicacion: Optional[str] = None, sensores: Optional[List[Sensor]] = None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        # almacenará instancias de Sensor
        self.sensores: List[Sensor] = sensores[:] if sensores else []

    def agregar_sensor(self, sensor: Sensor) -> bool:
        """Agrega un sensor al almacén. Devuelve True si se añadió, False si ya existía el ID."""
        if self.get_sensor_por_id(sensor.id) is not None:
            return False
        self.sensores.append(sensor)
        return True

    def eliminar_sensor_por_id(self, id_sensor: str) -> bool:
        """Elimina un sensor por su ID. Devuelve True si se eliminó, False si no se encontró."""
        for i, s in enumerate(self.sensores):
            if s.id == id_sensor:
                del self.sensores[i]
                return True
        return False

    def get_sensor_por_id(self, id_sensor: str) -> Optional[Sensor]:
        """Busca y devuelve la instancia Sensor con el ID dado, o None si no existe."""
        for s in self.sensores:
            if s.id == id_sensor:
                return s
        return None

    def listar_sensores(self) -> List[Sensor]:
        """Devuelve la lista de sensores (referencias)."""
        return list(self.sensores)

    def __str__(self) -> str:
        return f"Almacén '{self.nombre}' ({len(self.sensores)} sensores)"

    def to_dict(self) -> dict:
        """Serializa el almacén a un dict (incluye metadata y sensores)."""
        return {
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "sensores": [
                {
                    "id": s.id,
                    "tipo": s.tipo,
                    "ubicacion": s.ubicacion,
                    "valor": s.valor,
                    "unidad": s.unidad,
                }
                for s in self.sensores
            ],
        }

    def guardar_en_archivo(self, archivo: str) -> bool:
        """Guarda el estado del almacén en un archivo JSON. Devuelve True si tuvo éxito."""
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"[Almacen] Error al guardar en {archivo}:", e)
            return False

    @classmethod
    def cargar_desde_archivo(cls, archivo: str) -> Optional["Almacen"]:
        """Carga un almacén desde un archivo JSON y devuelve una instancia de Almacen.
        El archivo puede contener keys: nombre, ubicacion, sensores (lista de dicts).
        """
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)

            nombre = data.get("nombre", "Almacén desde archivo")
            ubicacion = data.get("ubicacion")
            sensores_data = data.get("sensores", [])
            sensores: List[Sensor] = []
            for sd in sensores_data:
                # Maneja ausencia de campos con valores por defecto
                sid = sd.get("id")
                tipo = sd.get("tipo", "")
                ubic = sd.get("ubicacion", "")
                valor = sd.get("valor")
                unidad = sd.get("unidad", "")
                if sid is None:
                    # Ignorar sensores sin id
                    continue
                sensores.append(Sensor(sid, tipo, ubic, valor, unidad))

            return cls(nombre, ubicacion, sensores)
        except Exception as e:
            print(f"[Almacen] Error al cargar desde {archivo}:", e)
            return None
