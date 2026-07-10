from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod
import json
import os


@dataclass
class Usuario(ABC):
    """Clase base abstracta para usuarios. No se puede instanciar directamente,
    usar Empleado o Cliente."""
    id: Optional[int]
    nombre: str
    email: str
    password: str
    rol: str = "cliente"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'rol_tipo'):
            raise TypeError(f"La clase {cls.__name__} debe definir 'rol_tipo'")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Cada subclase debe implementar su propia versión de from_dict"""
        raise NotImplementedError("Usar Empleado.from_dict() o Cliente.from_dict()")

    # --- methods to view almacen (stock) and sensores ---
    def view_almacen(self, db_path: str = 'database/stock.json'):
        """Return the almacen (stock) data. Base Usuario can view both almacen and sensores.
        If the file does not exist, returns an empty list.
        """
        try:
            if not os.path.exists(db_path):
                return []
            with open(db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    def view_sensores(self, db_path: str = 'database/sensors.json'):
        """Return the sensores data. Base Usuario can view both almacen and sensores.
        If the file does not exist, returns an empty list.
        """
        try:
            if not os.path.exists(db_path):
                return []
            with open(db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []


@dataclass
class Empleado(Usuario):
    """Un empleado del supermercado. Puede ver sensores pero no stock."""
    puesto: Optional[str] = None
    departamento: Optional[str] = None
    rol_tipo: str = "empleado"  # Requerido por Usuario

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Crea un Empleado desde un diccionario."""
        return cls(
            id=data.get("id"),
            nombre=data.get("nombre", ""),
            email=data.get("email", ""),
            password=data.get("password", ""),
            rol=data.get("rol", "empleado"),
            puesto=data.get("puesto"),
            departamento=data.get("departamento"),
        )

    # Empleado: tiene permiso para ver sensores, pero no para ver el stock completo
    def view_almacen(self, db_path: str = 'database/stock.json'):
        raise PermissionError('El empleado no tiene permiso para ver el almacen (stock) completo.')

    def view_sensores(self, db_path: str = 'database/sensors.json'):
        return super().view_sensores(db_path)


@dataclass
class Cliente(Usuario):
    """Un cliente del supermercado. Puede ver stock pero no sensores."""
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    historial: list = field(default_factory=list)
    rol_tipo: str = "cliente"  # Requerido por Usuario

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Crea un Cliente desde un diccionario."""
        return cls(
            id=data.get("id"),
            nombre=data.get("nombre", ""),
            email=data.get("email", ""),
            password=data.get("password", ""),
            rol=data.get("rol", "cliente"),
            direccion=data.get("direccion"),
            telefono=data.get("telefono"),
            historial=data.get("historial", []),
        )

    # Cliente: tiene permiso para ver el stock, pero no para ver sensores
    def view_almacen(self, db_path: str = 'database/stock.json'):
        return super().view_almacen(db_path)

    def view_sensores(self, db_path: str = 'database/sensors.json'):
        raise PermissionError('El cliente no tiene permiso para ver los sensores.')
