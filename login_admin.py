# admin_demo_json.py
# Demo de clase Administrador con persistencia en JSON (sin interfaz).
# Ejecutar: python admin_demo_json.py --db db.json

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
from datetime import datetime
import json, os, copy, argparse

# =========================
# Excepciones de dominio
# =========================
class PermisoError(Exception): ...
class ReglasNegocioError(Exception): ...

# =========================
# Utilidades
# =========================
def ahora_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

# =========================
# Modelos (usuarios)
# =========================
@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    rol: str  # "usuario" | "cliente" | "personal" | "administrador" | "superusuario"
    activo: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Usuario":
        return Usuario(**d)

# =========================
# Modelos (sensores) - para sembrado/validación
# =========================
@dataclass
class SensorBase:
    id: str
    encendido: bool = True
    def to_dict(self): 
        d = asdict(self)
        d["type"] = type(self).__name__
        return d

@dataclass
class DHT(SensorBase):
    modelo: str = "DHT11"
    temperatura_c: float = 22.0
    humedad_pct: float = 50.0

@dataclass
class CamaraFrigorifica(SensorBase):
    setpoint_c: float = 4.0
    temperatura_c: float = 6.0

@dataclass
class Congelador(SensorBase):
    setpoint_c: float = -18.0
    temperatura_c: float = -15.0

@dataclass
class LDR(SensorBase):
    lux: float = 100.0

@dataclass
class MQ2(SensorBase):
    humo_ppm: float = 0.0

@dataclass
class Caudalimetro(SensorBase):
    l_min: float = 0.0

@dataclass
class Ultrasonico(SensorBase):
    distancia_cm: float = 100.0

SENSOR_TYPES = {
    "DHT": DHT,
    "CamaraFrigorifica": CamaraFrigorifica,
    "Congelador": Congelador,
    "LDR": LDR,
    "MQ2": MQ2,
    "Caudalimetro": Caudalimetro,
    "Ultrasonico": Ultrasonico,
}

# =========================
# Capa de persistencia JSON
# =========================
class JSONDB:
    def __init__(self, path: str):
        self.path = path
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = self.default_data()
            self.save()

        self._merge_defaults()   # completa secciones que falten
        self._ensure_admin()     # si no hay admin, crea uno
        self.save()

    def default_data(self) -> Dict[str, Any]:
        return {
            "meta": {"next_user_id": 1},
            "usuarios": {},
            "luces": {
                "estado": {"entrada": False, "cajas": False, "pasillo-1": False, "pasillo-2": False, "almacen": False},
                "auto": False,
                "umbral_lux": 50.0
            },
            "sensores": {},  # mapa: sensor_id -> dict con "type" y campos del sensor
            "stock": {"estantes": {}, "camaras": {}, "almacen": {}},
            "snapshots": [],
            "actividad": []
        }

    def _merge_defaults(self):
        defaults = self.default_data()
        # Asegurar claves de primer nivel
        for k, v in defaults.items():
            if k not in self.data:
                self.data[k] = copy.deepcopy(v)
        # Luces
        luces = self.data["luces"]
        for k, v in defaults["luces"].items():
            if k not in luces:
                luces[k] = copy.deepcopy(v)
        for zona in defaults["luces"]["estado"]:
            luces["estado"].setdefault(zona, False)
        # Stock
        for k in ("estantes", "camaras", "almacen"):
            self.data["stock"].setdefault(k, {})
        # Meta.next_user_id
        if "next_user_id" not in self.data["meta"]:
            max_id = 0
            for uid in self.data["usuarios"].keys():
                try:
                    max_id = max(max_id, int(uid))
                except:
                    pass
            self.data["meta"]["next_user_id"] = max_id + 1
        # Sembrado mínimo de sensores si no hay
        if not self.data["sensores"]:
            seed = {
                "dht-a1"   : DHT(id="dht-a1", modelo="DHT11", temperatura_c=23.5, humedad_pct=45.0).to_dict(),
                "dht-b2"   : DHT(id="dht-b2", modelo="DHT22", temperatura_c=21.0, humedad_pct=55.0).to_dict(),
                "camara-01": CamaraFrigorifica(id="camara-01", setpoint_c=3.0, temperatura_c=5.5).to_dict(),
                "cong-01"  : Congelador(id="cong-01", setpoint_c=-20.0, temperatura_c=-17.0).to_dict(),
                "ldr-entr" : LDR(id="ldr-entr", lux=35.0).to_dict(),
                "ldr-pas1" : LDR(id="ldr-pas1", lux=60.0).to_dict(),
                "mq2-01"   : MQ2(id="mq2-01", humo_ppm=5.0).to_dict(),
                "flow-01"  : Caudalimetro(id="flow-01", l_min=2.3).to_dict(),
                "ultra-01" : Ultrasonico(id="ultra-01", distancia_cm=120.0).to_dict(),
            }
            self.data["sensores"] = seed
        # Sembrado mínimo de stock si estuviera vacío
        if (not self.data["stock"]["estantes"] and
            not self.data["stock"]["camaras"] and
            not self.data["stock"]["almacen"]):
            self.data["stock"] = {
                "estantes": {"pasillo-1": {"agua-1L": 45, "pasta-500g": 80},
                             "pasillo-2": {"leche-1L": 30, "galletas-200g": 60}},
                "camaras": {"camara-01": {"yogur": 120, "queso": 50}},
                "almacen": {"palets-agua": 10, "palets-leche": 8, "cajas-galletas": 25}
            }

    def _ensure_admin(self):
        if not self.data["usuarios"]:
            uid = self.allocate_user_id()
            admin = Usuario(id=uid, nombre="Admin Inicial", email="admin@tienda.com", rol="administrador").to_dict()
            self.data["usuarios"][str(uid)] = admin

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def allocate_user_id(self) -> int:
        nid = self.data["meta"].get("next_user_id", 1)
        self.data["meta"]["next_user_id"] = nid + 1
        return nid

# =========================
# Servicios de dominio
# =========================
class GestorUsuarios:
    ROLES_PRIV = {"administrador", "superusuario"}

    def __init__(self, db: JSONDB):
        self.db = db
        # Sesión simulada: primer admin existente
        self._sesion_id: Optional[int] = None
        for uid, u in db.data["usuarios"].items():
            if u.get("rol") == "administrador":
                self._sesion_id = int(uid)
                break

    def listar(self) -> List[Usuario]:
        return [Usuario.from_dict({**u, "id": int(uid)}) for uid, u in self.db.data["usuarios"].items()]

    def crear(self, nombre: str, email: str, rol: str) -> Usuario:
        self._requerir_priv()
        uid = self.db.allocate_user_id()
        u = Usuario(uid, nombre, email, rol)
        self.db.data["usuarios"][str(uid)] = u.to_dict()
        self.db.save()
        return u

    # >>> NUEVO: auto-registro de clientes (no requiere privilegio)
    def registrar_cliente_autoservicio(self, nombre: str, email: str) -> Usuario:
        uid = self.db.allocate_user_id()
        u = Usuario(uid, nombre, email, "cliente")
        self.db.data["usuarios"][str(uid)] = u.to_dict()
        self.db.save()
        return u

    def borrar(self, user_id: int):
        self._requerir_priv()
        u = self.db.data["usuarios"].get(str(user_id))
        if not u:
            raise ReglasNegocioError("Usuario inexistente.")
        if u["rol"] in self.ROLES_PRIV:
            raise PermisoError("Prohibido borrar cuentas privilegiadas (administrador/superusuario).")
        del self.db.data["usuarios"][str(user_id)]
        self.db.save()

    def desactivar(self, user_id: int):
        self._requerir_priv()
        u = self.db.data["usuarios"].get(str(user_id))
        if not u:
            raise ReglasNegocioError("Usuario inexistente.")
        if u["rol"] in self.ROLES_PRIV:
            raise PermisoError("Prohibido modificar cuentas privilegiadas (administrador/superusuario).")
        u["activo"] = False
        self.db.save()

    def _requerir_priv(self):
        u = self.db.data["usuarios"].get(str(self._sesion_id))
        if not u or u["rol"] not in self.ROLES_PRIV:
            raise PermisoError("Acción permitida solo a administradores o superusuarios.")

class PanelLuces:
    """Control de luces + modo automático según LDR."""
    def __init__(self, db: JSONDB):
        self.db = db

    def encender(self, zona: str):
        self._validar(zona)
        self.db.data["luces"]["estado"][zona] = True
        self.db.save()

    def apagar(self, zona: str):
        self._validar(zona)
        self.db.data["luces"]["estado"][zona] = False
        self.db.save()

    def configurar_auto(self, umbral_lux: float):
        self.db.data["luces"]["auto"] = True
        self.db.data["luces"]["umbral_lux"] = float(umbral_lux)
        self.db.save()

    def desactivar_auto(self):
        self.db.data["luces"]["auto"] = False
        self.db.save()

    def aplicar_ldr(self, lux: float, zonas: Optional[List[str]] = None):
        if not self.db.data["luces"]["auto"]:
            return
        zonas = zonas or list(self.db.data["luces"]["estado"].keys())
        if lux < self.db.data["luces"]["umbral_lux"]:
            for z in zonas:
                self.db.data["luces"]["estado"][z] = True
        else:
            for z in zonas:
                self.db.data["luces"]["estado"][z] = False
        self.db.save()

    def estado(self) -> Dict[str, Any]:
        return copy.deepcopy(self.db.data["luces"])

    def _validar(self, zona: str):
        if zona not in self.db.data["luces"]["estado"]:
            raise ReglasNegocioError(f"Zona desconocida: {zona}")

class GestorSensores:
    """Sensores persistidos como: sensores[sensor_id] = dict con 'type' y campos."""
    def __init__(self, db: JSONDB):
        self.db = db

    def _get(self, sensor_id: str) -> Dict[str, Any]:
        s = self.db.data["sensores"].get(sensor_id)
        if not s:
            raise ReglasNegocioError("Sensor inexistente.")
        return s

    def leer_todo(self) -> Dict[str, Dict]:
        cats = {"dht": {}, "camaras_frio": {}, "congeladores": {}, "ldr": {}, "mq2": {}, "caudalimetros": {}, "ultrasonicos": {}}
        for sid, s in self.db.data["sensores"].items():
            t = s.get("type")
            if   t == "DHT":               cats["dht"][sid] = s
            elif t == "CamaraFrigorifica": cats["camaras_frio"][sid] = s
            elif t == "Congelador":        cats["congeladores"][sid] = s
            elif t == "LDR":               cats["ldr"][sid] = s
            elif t == "MQ2":               cats["mq2"][sid] = s
            elif t == "Caudalimetro":      cats["caudalimetros"][sid] = s
            elif t == "Ultrasonico":       cats["ultrasonicos"][sid] = s
        return cats

    def encender(self, sensor_id: str):
        s = self._get(sensor_id)
        s["encendido"] = True
        self.db.save()

    def apagar(self, sensor_id: str):
        s = self._get(sensor_id)
        s["encendido"] = False
        self.db.save()

    def ajustar_setpoint(self, sensor_id: str, nuevo_setpoint: float):
        s = self._get(sensor_id)
        if s.get("type") not in ("CamaraFrigorifica", "Congelador"):
            raise ReglasNegocioError("Solo cámaras y congeladores tienen setpoint.")
        s["setpoint_c"] = float(nuevo_setpoint)
        self.db.save()

    def simular(self, sensor_id: str, **valores):
        s = self._get(sensor_id)
        for k, v in valores.items():
            if k in s:
                s[k] = float(v) if isinstance(s[k], (int, float, float)) else v
            else:
                raise ReglasNegocioError(f"Campo '{k}' no válido para el sensor {sensor_id}.")
        self.db.save()

class GestorStock:
    def __init__(self, db: JSONDB):
        self.db = db
    def ver_stockaje(self) -> Dict[str, Dict]:
        return copy.deepcopy(self.db.data["stock"])

class RegistroActividad:
    def __init__(self, db: JSONDB):
        self.db = db
    def anotar(self, actor: str, accion: str, detalle: str = ""):
        self.db.data["actividad"].append({"ts": ahora_iso(), "actor": actor, "accion": accion, "detalle": detalle})
        self.db.save()
    def listar(self) -> List[Dict[str, Any]]:
        return list(self.db.data["actividad"])

# =========================
# Fachada Administrador
# =========================
class Administrador:
    def __init__(self, db: JSONDB):
        self.db = db
        self.usuarios = GestorUsuarios(db)
        self.luces = PanelLuces(db)
        self.sensores = GestorSensores(db)
        self.stock = GestorStock(db)
        self.actividad = RegistroActividad(db)

    # Luces
    def encender_luz(self, zona: str):
        self.luces.encender(zona)
        self.actividad.anotar("admin", "encender_luz", zona)

    def apagar_luz(self, zona: str):
        self.luces.apagar(zona)
        self.actividad.anotar("admin", "apagar_luz", zona)

    def configurar_luces_auto(self, umbral_lux: float):
        self.luces.configurar_auto(umbral_lux)
        self.actividad.anotar("admin", "configurar_luces_auto", f"umbral={umbral_lux}")

    def aplicar_luces_por_ldr(self, lux_promedio: float, zonas: Optional[List[str]] = None):
        self.luces.aplicar_ldr(lux_promedio, zonas)
        self.actividad.anotar("admin", "aplicar_luces_por_ldr", f"lux={lux_promedio}")

    def ver_luces(self) -> Dict[str, Any]:
        return self.luces.estado()

    # Usuarios
    def crear_usuario(self, nombre: str, email: str, tipo: str = "usuario") -> Usuario:
        if tipo not in ("usuario", "cliente", "personal", "administrador", "superusuario"):
            raise ReglasNegocioError("Tipo de usuario no válido.")
        u = self.usuarios.crear(nombre, email, tipo)
        self.actividad.anotar("admin", "crear_usuario", f"{u.id}:{u.rol}")
        return u

    # >>> NUEVO: wrapper de auto-registro para evidenciar la funcionalidad
    def registrar_cliente_autoservicio(self, nombre: str, email: str) -> Usuario:
        u = self.usuarios.registrar_cliente_autoservicio(nombre, email)
        # el actor es "cliente" para distinguirlo en el log
        self.actividad.anotar("cliente", "registro_autoservicio", f"{u.id}:{u.email}")
        return u

    def borrar_usuario(self, user_id: int):
        self.usuarios.borrar(user_id)
        self.actividad.anotar("admin", "borrar_usuario", str(user_id))

    def desactivar_usuario(self, user_id: int):
        self.usuarios.desactivar(user_id)
        self.actividad.anotar("admin", "desactivar_usuario", str(user_id))

    def listar_usuarios(self) -> List[Usuario]:
        return self.usuarios.listar()

    # Sensores
    def ver_sensores(self) -> Dict[str, Dict]:
        return self.sensores.leer_todo()

    def encender_sensor(self, sensor_id: str):
        self.sensores.encender(sensor_id)
        self.actividad.anotar("admin", "encender_sensor", sensor_id)

    def apagar_sensor(self, sensor_id: str):
        self.sensores.apagar(sensor_id)
        self.actividad.anotar("admin", "apagar_sensor", sensor_id)

    def ajustar_setpoint(self, sensor_id: str, setpoint: float):
        self.sensores.ajustar_setpoint(sensor_id, setpoint)
        self.actividad.anotar("admin", "ajustar_setpoint", f"{sensor_id}={setpoint}")

    def simular_lectura_sensor(self, sensor_id: str, **valores):
        self.sensores.simular(sensor_id, **valores)
        self.actividad.anotar("admin", "simular_lectura_sensor", f"{sensor_id}:{valores}")

    # Stock
    def ver_stockaje(self) -> Dict[str, Dict]:
        return self.stock.ver_stockaje()

    # Snapshots
    def snapshot_sensores(self):
        snap = {"ts": ahora_iso(), "lecturas": self.sensores.leer_todo()}
        self.db.data["snapshots"].append(snap)
        self.db.save()
        self.actividad.anotar("admin", "snapshot_sensores", f"total={len(self.db.data['snapshots'])}")

    def ver_historial_sensores(self) -> List[Dict[str, Any]]:
        return list(self.db.data["snapshots"])

    def ver_actividad(self) -> List[Dict[str, Any]]:
        return self.actividad.listar()

# =========================
# Demo por consola (puedes quitarla si solo quieres la clase)
# =========================
def separador(titulo: str):
    print("\n" + "=" * 74)
    print(titulo.upper())
    print("=" * 74)

def imprimir_usuarios(usuarios: List[Usuario]):
    for u in usuarios:
        print(f"[{u.id}] {u.nombre:<18} | {u.email:<22} | rol={u.rol:<13} | activo={u.activo}")

def imprimir_dict(d: Dict, indent: int = 0):
    pad = "  " * indent
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, dict):
                print(f"{pad}{k}:")
                imprimir_dict(v, indent + 1)
            else:
                print(f"{pad}{k}: {v}")
    else:
        print(f"{pad}{d}")

def main():
    parser = argparse.ArgumentParser(description="Administrador con JSON DB")
    parser.add_argument("--db", default="db.json", help="Ruta al JSON de datos")
    args = parser.parse_args()

    db = JSONDB(args.db)
    admin = Administrador(db)

    separador("Luces (leer / configurar / aplicar LDR)")
    print(admin.ver_luces())
    admin.configurar_luces_auto(50)
    admin.aplicar_luces_por_ldr(30.0, zonas=["entrada", "pasillo-1"])
    print(admin.ver_luces())

    separador("Usuarios (crear / auto-registro / restricciones)")
    u1 = admin.crear_usuario("Usuario Demo", "u@demo.com", "usuario")
    c1 = admin.crear_usuario("Ana Cliente", "ana@cliente.com", "cliente")
    p1 = admin.crear_usuario("Pablo Empleado", "pablo@tienda.com", "personal")
    a2 = admin.crear_usuario("Admin Secundario", "admin2@tienda.com", "administrador")
    s1 = admin.crear_usuario("Root Super", "root@tienda.com", "superusuario")

    # >>> Demostración de auto-registro (sin privilegios)
    auto = admin.registrar_cliente_autoservicio("Carlos Auto", "carlos@cliente.com")

    imprimir_usuarios(admin.listar_usuarios())

    print("\nIntentos de restricciones (esperan error):")
    try:
        admin.borrar_usuario(a2.id)
    except Exception as e:
        print(" - Borrar admin:", e)
    try:
        admin.desactivar_usuario(s1.id)
    except Exception as e:
        print(" - Desactivar superusuario:", e)

    print("\nBorrado permitido (cliente):")
    admin.borrar_usuario(c1.id)
    imprimir_usuarios(admin.listar_usuarios())

    separador("Sensores (lectura y simulación)")
    imprimir_dict(admin.ver_sensores())
    print("\nAjustes:")
    admin.apagar_sensor("dht-a1")
    admin.ajustar_setpoint("camara-01", 2.5)
    admin.simular_lectura_sensor("cong-01", temperatura_c=-22.0)
    admin.simular_lectura_sensor("dht-b2", temperatura_c=20.1, humedad_pct=48.0)
    admin.simular_lectura_sensor("ldr-pas1", lux=25.0)
    imprimir_dict(admin.ver_sensores())

    separador("Stockaje")
    imprimir_dict(admin.ver_stockaje())

    separador("Snapshots y actividad")
    admin.snapshot_sensores()
    admin.snapshot_sensores()
    print("Snapshots totales:", len(admin.ver_historial_sensores()))
    print("\nÚltimos eventos:")
    for ev in admin.ver_actividad()[-10:]:
        print(ev)

    print("\nDemo finalizada. Revisa los cambios persistidos en:", args.db)

if __name__ == "__main__":
    main()
