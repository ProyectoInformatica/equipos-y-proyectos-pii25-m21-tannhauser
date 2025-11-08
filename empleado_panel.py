import json
import os
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from thread_utils import ThreadedTask, file_lock
import threading

class EmpleadoPanelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel del Empleado - Supermercado Inteligente")
        self.root.geometry("1000x600")
        self.threaded_task = ThreadedTask()
        
        # Configurar el estilo
        style = ttk.Style()
        style.configure("Header.TLabel", font=('Helvetica', 20, 'bold'))
        style.configure("Subheader.TLabel", font=('Helvetica', 12))
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(self.main_frame, 
                              text="Panel del Empleado - Monitoreo de Sensores",
                              style="Header.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0,20))
        
        # Frame para el Treeview
        tree_frame = ttk.Frame(self.main_frame)
        tree_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear Treeview
        self.tree = ttk.Treeview(tree_frame, 
                                columns=('ID', 'Tipo', 'Valor', 'Estado'),
                                show='headings',
                                height=15)
        
        # Configurar columnas
        self.tree.heading('ID', text='ID Sensor')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.heading('Valor', text='Valor')
        self.tree.heading('Estado', text='Estado')
        
        self.tree.column('ID', width=100, anchor='center')
        self.tree.column('Tipo', width=150, anchor='center')
        self.tree.column('Valor', width=200, anchor='center')
        self.tree.column('Estado', width=150, anchor='center')
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Posicionar Treeview
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=2, column=0, pady=20)
        
        # Botones
        ttk.Button(button_frame, text="Actualizar", command=self.actualizar_sensores).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Ver Detalles", command=self.ver_detalles).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Cerrar Sesión", command=self.cerrar_sesion).grid(row=0, column=2, padx=5)
        
        # Iniciar monitoreo automático
        self.monitoreo_activo = True
        self.thread_monitoreo = threading.Thread(target=self.monitoreo_automatico, daemon=True)
        self.thread_monitoreo.start()
        
        # Cargar datos iniciales
        self.actualizar_sensores()
    
    def actualizar_sensores(self):
        self.tree.configure(cursor="wait")
        self.root.configure(cursor="wait")
        
        def load_data():
            with file_lock:
                return leer_json("database/sensors.json")
        
        def update_ui(sensores):
            # Limpiar tabla
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Insertar nuevos datos
            for sensor in sensores:
                valor = sensor.get("valor")
                valor_str = self.formatear_valor(valor, sensor.get("unidad", ""))
                estado = self.determinar_estado(sensor)
                
                self.tree.insert('', tk.END, values=(
                    sensor.get('id', 'N/A'),
                    sensor.get('tipo', 'Desconocido').title(),
                    valor_str,
                    estado
                ), tags=(estado.lower(),))
            
            # Configurar colores
            self.tree.tag_configure('normal', foreground='green')
            self.tree.tag_configure('advertencia', foreground='orange')
            self.tree.tag_configure('critico', foreground='red')
            
            # Restaurar cursor
            self.tree.configure(cursor="")
            self.root.configure(cursor="")
        
        def error_handler(error):
            messagebox.showerror("Error", f"Error al cargar los datos: {error}")
            self.tree.configure(cursor="")
            self.root.configure(cursor="")
        
        self.threaded_task.execute(load_data, update_ui, error_handler)
    
    def ver_detalles(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un sensor para ver sus detalles")
            return
        
        item = self.tree.item(seleccion[0])
        sensor_id = item['values'][0]
        
        def get_sensor_details():
            with file_lock:
                sensores = leer_json("database/sensors.json")
                for sensor in sensores:
                    if str(sensor.get('id')) == str(sensor_id):
                        return sensor
                return None
        
        def show_details(sensor):
            if sensor:
                detalle = f"""
Detalles del Sensor {sensor.get('id')}
===============================
Tipo: {sensor.get('tipo', 'N/A')}
Ubicación: {sensor.get('ubicacion', 'N/A')}
-------------------------------
{self.get_sensor_description(sensor.get('tipo', ''))}
-------------------------------
{self.formatear_valor(sensor.get('valor'), sensor.get('unidad', ''))}
===============================
"""
                messagebox.showinfo("Detalles del Sensor", detalle)
            else:
                messagebox.showerror("Error", "No se encontró el sensor seleccionado")
        
        self.threaded_task.execute(get_sensor_details, show_details)
    
    def monitoreo_automatico(self):
        while self.monitoreo_activo:
            time.sleep(5)  # Actualizar cada 5 segundos
            if self.monitoreo_activo:  # Verificar nuevamente por si se desactivó
                self.root.after(0, self.actualizar_sensores)
    
    def cerrar_sesion(self):
        self.monitoreo_activo = False
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea cerrar sesión?"):
            self.root.quit()
    
    @staticmethod
    def formatear_valor(valor, unidad):
        if isinstance(valor, dict):
            return " | ".join(f"{k.title()}: {v} {unidad.get(k, '') if isinstance(unidad, dict) else unidad}"
                            for k, v in valor.items())
        return f"{valor} {unidad}"
    
    @staticmethod
    def determinar_estado(sensor):
        tipo = sensor.get("tipo", "").lower()
        valor = sensor.get("valor")
        
        if isinstance(valor, dict):
            valor = next(iter(valor.values()))  # Tomar el primer valor
        
        try:
            valor = float(valor)
            if tipo == "temperatura":
                if valor < 0 or valor > 30: return "CRITICO"
                if valor < 5 or valor > 25: return "ADVERTENCIA"
            elif tipo == "humedad":
                if valor < 20 or valor > 80: return "CRITICO"
                if valor < 30 or valor > 70: return "ADVERTENCIA"
        except (ValueError, TypeError):
            pass
        
        return "NORMAL"
    
    @staticmethod
    def get_sensor_description(tipo):
        tipo = tipo.lower()
        if tipo == "temperatura":
            return "Monitorea la temperatura ambiente para conservar productos sensibles."
        elif tipo == "humedad":
            return "Mide los niveles de humedad en el ambiente para evitar deterioros."
        elif tipo == "movimiento":
            return "Detecta movimiento en zonas del supermercado para seguridad y flujo."
        elif tipo == "peso":
            return "Mide peso en estanterías para controlar inventario y reabastecimiento."
        return "Sensor de monitoreo general para el control del supermercado."

# ------------------- FUNCIONES DE UTILIDAD -------------------

def leer_json(ruta):
    """Lee el archivo JSON con los datos de los sensores."""
    try:
        if not os.path.exists(ruta):
            return []
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def mostrar_encabezado():
    print("=" * 60)
    print(" PANEL DEL EMPLEADO - SUPERMERCADO INTELIGENTE ".center(60, " "))
    print("=" * 60)
    print("Monitoreo de sensores".center(60, " "))
    print("-" * 60)


def mostrar_sensor(sensor):
    """Muestra un resumen de un sensor."""
    tipo = (sensor.get("tipo") or "").title()
    valor = sensor.get("valor")
    unidad = sensor.get("unidad", "")

    print(f"ID: {sensor.get('id', 'N/A')}")
    print(f"Tipo: {tipo}")

    if isinstance(valor, dict):
        for k, v in valor.items():
            u = unidad.get(k, "") if isinstance(unidad, dict) else unidad
            print(f"  {k.title()}: {v} {u}")
    else:
        print(f"  Valor: {valor} {unidad}")
    print("-" * 40)


def mostrar_detalle(sensor):
    """Muestra información detallada del sensor."""
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 60)
    print(f" DETALLES DEL SENSOR {sensor.get('id', 'N/A')} ".center(60))
    print("=" * 60)

    print(f"Tipo: {sensor.get('tipo', 'N/A')}")
    print(f"Ubicación: {sensor.get('ubicacion', 'N/A')}")
    print("-" * 40)

    tipo = (sensor.get("tipo") or "").lower()
    if tipo == "temperatura":
        print("Monitorea la temperatura ambiente para conservar productos sensibles.")
    elif tipo == "humedad":
        print("Mide los niveles de humedad en el ambiente para evitar deterioros.")
    elif tipo == "movimiento":
        print("Detecta movimiento en zonas del supermercado para seguridad y flujo.")
    elif tipo == "peso":
        print("Mide peso en estanterías para controlar inventario y reabastecimiento.")
    else:
        print("Sensor de monitoreo general para el control del supermercado.")

    print("-" * 40)

    valor = sensor.get("valor")
    unidad = sensor.get("unidad", "")
    if isinstance(valor, dict):
        for k, v in valor.items():
            u = unidad.get(k, "") if isinstance(unidad, dict) else unidad
            print(f"{k.title()}: {v} {u}")
    else:
        print(f"Valor: {valor} {unidad}")

    print("=" * 60)
    input("Pulsa Enter para volver al panel...")


# ------------------- MENÚ PRINCIPAL -------------------

def panel_empleado():
    root = tk.Tk()
    app = EmpleadoPanelGUI(root)
    root.mainloop()

