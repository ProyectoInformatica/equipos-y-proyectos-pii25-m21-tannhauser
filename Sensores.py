import json
import os
import threading
import time
import logging
from datetime import datetime
import random

# -------------------------
# Logging
# -------------------------
logging.basicConfig(
    filename="sensores.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# -------------------------
# GestorSensores
# -------------------------
class GestorSensores:
    def _init_(self, archivo_json="sensores.json"):
        self.archivo = archivo_json
        self._lock = threading.Lock()
        self._auto_threads = []
        self._auto_stop_event = threading.Event()

        if not os.path.exists(self.archivo):
            self._inicializar_json()
            logging.info("Archivo JSON inicial creado.")
        else:
            logging.info("Archivo JSON cargado existente.")

    # -------------------------
    # JSON
    # -------------------------
    def _leer_json(self):
        with self._lock:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)

    def _guardar_json(self, datos):
        with self._lock:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)

    # -------------------------
    # Inicialización
    # -------------------------
    def _inicializar_json(self):
        """
        Datos ficticios iniciales para simular luces y sensores aún no instalados.
        """
        estructura = {
            "luces": {
                "estado": {
                    "entrada": True,
                    "cajas": True,
                    "pasillo-1": True,
                    "pasillo-2": True,
                    "almacen": False
                },
                "auto": False,
                "umbral_lux": 50.0
            },
            "sensores": {
                "temp-01": {"type": "DHT", "valor": 22.5, "zona": "pasillo-1"},
                "hum-01": {"type": "DHT", "valor": 55.0, "zona": "zona lacteos"},
                "mov-01": {"type": "PIR", "activo": True, "zona": "entrada"},
                "temp-02": {"type": "DHT", "valor": 18.0, "zona": "refrigerados"},
                "mov-02": {"type": "PIR", "activo": False, "zona": "almacen"},
                "contador_personas": {"type": "CONTADOR", "valor": 0, "zona": "entrada"},
                "persiana_metalica": {"type": "PERSIANA", "valor": "cerrada", "zona": "fachada"}
            },
            "actividad": [
                {
                    "cuando": "2025-11-21T09:00:00",
                    "quien": "sistema",
                    "accion": "inicializacion",
                    "detalle": "Sistema iniciado - Datos de prueba cargados"
                }
            ]
        }
        self._guardar_json(estructura)

    # -------------------------
    # Registro de actividad
    # -------------------------
    def registrar_actividad(self, quien, accion, detalle):
        entrada = {
            "cuando": datetime.now().isoformat(),
            "quien": quien,
            "accion": accion,
            "detalle": detalle
        }
        datos = self._leer_json()
        datos.setdefault("actividad", []).append(entrada)
        self._guardar_json(datos)
        logging.info(f"{quien} | {accion} | {detalle}")

    # -------------------------
    # Sensores
    # -------------------------
    def mostrar_sensores(self):
        datos = self._leer_json()
        sensores = datos.get("sensores", {})
        print("\n--- SENSORES ---")
        for k, v in sensores.items():
            print(f"{k}: {v}")
        print("\n--- LUCES ---")
        print(datos.get("luces", {}))

    def persona_entra(self, cantidad=1, quien="sistema_auto"):
        datos = self._leer_json()
        cont = datos.get("sensores", {}).get("contador_personas")
        if cont is None:
            cont = {"type": "CONTADOR", "valor": 0, "zona": "entrada"}
            datos["sensores"]["contador_personas"] = cont
        cont["valor"] += cantidad
        self._guardar_json(datos)
        self.registrar_actividad(quien, "conteo_personas", f"Incrementado en {cantidad}. Total: {cont['valor']}")
        print(f"Personas totales: {cont['valor']}")

    def controlar_persiana(self, accion, quien="usuario"):
        accion = accion.lower()
        if accion not in ("abrir", "cerrar"):
            print("Acción inválida: usar 'abrir' o 'cerrar'.")
            return

        datos = self._leer_json()
        pers = datos.get("sensores", {}).get("persiana_metalica")
        if pers is None:
            pers = {"type": "PERSIANA", "valor": "cerrada", "zona": "fachada"}
            datos["sensores"]["persiana_metalica"] = pers

        pers["valor"] = "abierta" if accion == "abrir" else "cerrada"
        self._guardar_json(datos)
        self.registrar_actividad(quien, "persiana", f"{accion}")
        print(f"Persiana ahora: {pers['valor']}")

    # -------------------------
    # Sensores automáticos (simulación)
    # -------------------------
    def iniciar_simulacion(self):
        self._auto_stop_event.clear()
        t1 = threading.Thread(target=self._simular_personas, daemon=True)
        t2 = threading.Thread(target=self._simular_dht, daemon=True)
        t3 = threading.Thread(target=self._simular_pir, daemon=True)
        t4 = threading.Thread(target=self._reglas_persiana, daemon=True)
        self._auto_threads = [t1, t2, t3, t4]
        for t in self._auto_threads:
            t.start()
        print("Simulación automática iniciada.")

    def detener_simulacion(self):
        self._auto_stop_event.set()
        for t in self._auto_threads:
            t.join(timeout=2)
        print("Simulación automática detenida.")

    # Worker personas
    def _simular_personas(self):
        while not self._auto_stop_event.is_set():
            time.sleep(random.uniform(2, 5))
            personas = random.randint(0, 3)
            if personas > 0:
                self.persona_entra(personas, "simulacion")

    # Worker DHT
    def _simular_dht(self):
        while not self._auto_stop_event.is_set():
            time.sleep(5)
            datos = self._leer_json()
            for sname in ["temp-01", "temp-02", "hum-01"]:
                s = datos["sensores"].get(sname)
                if s:
                    s["valor"] += round(random.uniform(-0.5, 0.5), 2)
            self._guardar_json(datos)
            self.registrar_actividad("simulacion", "variacion_dht", "DHTs actualizados")

    # Worker PIR
    def _simular_pir(self):
        while not self._auto_stop_event.is_set():
            time.sleep(3)
            datos = self._leer_json()
            for sname in ["mov-01", "mov-02"]:
                s = datos["sensores"].get(sname)
                if s:
                    s["activo"] = random.choice([True, False])
            self._guardar_json(datos)
            self.registrar_actividad("simulacion", "pir", "Sensores PIR actualizados")

    # Reglas persiana
    def _reglas_persiana(self):
        while not self._auto_stop_event.is_set():
            time.sleep(2)
            datos = self._leer_json()
            contador = datos["sensores"]["contador_personas"]["valor"]
            persiana = datos["sensores"]["persiana_metalica"]["valor"]
            if contador > 10 and persiana != "cerrada":
                self.controlar_persiana("cerrar", "simulacion")
            elif contador <= 5 and persiana != "abierta":
                self.controlar_persiana("abrir", "simulacion")

    # -------------------------
    # Menú interactivo
    # -------------------------
    def menu(self):
        try:
            while True:
                print("\n===== MENÚ SENSORES =====")
                print("1) Mostrar sensores")
                print("2) Persona entra")
                print("3) Controlar persiana (abrir/cerrar)")
                print("4) Iniciar simulación automática")
                print("5) Detener simulación automática")
                print("6) Mostrar actividad")
                print("7) Exportar actividad a TXT")
                print("8) Salir")
                opc = input("Opción: ").strip()
                if opc == "1":
                    self.mostrar_sensores()
                elif opc == "2":
                    c = int(input("¿Cuántas personas entraron? "))
                    self.persona_entra(c, "usuario")
                elif opc == "3":
                    a = input("Abrir o cerrar: ").strip().lower()
                    self.controlar_persiana(a, "usuario")
                elif opc == "4":
                    self.iniciar_simulacion()
                elif opc == "5":
                    self.detener_simulacion()
                elif opc == "6":
                    self.mostrar_actividad()
                elif opc == "7":
                    self.exportar_actividad_txt()
                elif opc == "8":
                    self.detener_simulacion()
                    break
                else:
                    print("Opción inválida.")
        except KeyboardInterrupt:
            print("\nSaliendo…")
            self.detener_simulacion()

    def mostrar_actividad(self):
        datos = self._leer_json()
        for a in datos.get("actividad", []):
            print(a)

    def exportar_actividad_txt(self, archivo="actividad.txt"):
        datos = self._leer_json()
        with open(archivo, "w", encoding="utf-8") as f:
            for a in datos.get("actividad", []):
                f.write(json.dumps(a, ensure_ascii=False) + "\n")
        print("Actividad exportada a", archivo)


# -------------------------
# Ejecutar como script
# -------------------------
if _name_ == "_main_":
    gestor = GestorSensores("sensores.json")
    gestor.menu()