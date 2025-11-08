import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
from queue import Queue


import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
from queue import Queue
import time

class ThreadedTask:
    def __init__(self):
        self.queue = Queue()
    
    def execute(self, func, callback=None, error_callback=None):
        def thread_target():
            try:
                result = func()
                self.queue.put(('success', result))
            except Exception as e:
                self.queue.put(('error', str(e)))
        
        def check_queue():
            try:
                message_type, result = self.queue.get_nowait()
                if message_type == 'success' and callback:
                    callback(result)
                elif message_type == 'error' and error_callback:
                    error_callback(result)
            except Queue.Empty:
                tk.Tk().after(100, check_queue)
        
        thread = threading.Thread(target=thread_target)
        thread.daemon = True
        thread.start()
        
        if callback or error_callback:
            tk.Tk().after(100, check_queue)

class LoginEmpleado:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Empleado - Gestor de Stock")
        self.root.geometry("400x300")
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(self.frame, text="Acceso Empleados", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0,20))
        
        # Campos de login
        ttk.Label(self.frame, text="Email:").grid(row=1, column=0, pady=5)
        self.email_entry = ttk.Entry(self.frame, width=30)
        self.email_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self.frame, text="Contraseña:").grid(row=2, column=0, pady=5)
        self.password_entry = ttk.Entry(self.frame, width=30, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)
        
        # Botón de login
        login_button = ttk.Button(self.frame, text="Iniciar Sesión", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Mensaje de error
        self.error_label = ttk.Label(self.frame, text="", foreground="red")
        self.error_label.grid(row=4, column=0, columnspan=2)
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login Empleado - Gestor de Stock")
        self.root.geometry("400x300")
        self.threaded_task = ThreadedTask()
        
        # Frame principal
        self.frame = ttk.Frame(root, padding="20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(self.frame, text="Acceso Empleados", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0,20))
        
        # Campos de login
        ttk.Label(self.frame, text="Email:").grid(row=1, column=0, pady=5)
        self.email_entry = ttk.Entry(self.frame, width=30)
        self.email_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self.frame, text="Contraseña:").grid(row=2, column=0, pady=5)
        self.password_entry = ttk.Entry(self.frame, width=30, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)
        
        # Botón de login y progreso
        self.login_button = ttk.Button(self.frame, text="Iniciar Sesión", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.progress = ttk.Progressbar(self.frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=2, pady=5)
        self.progress.grid_remove()
        
        # Mensaje de error
        self.error_label = ttk.Label(self.frame, text="", foreground="red")
        self.error_label.grid(row=5, column=0, columnspan=2)
        
    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        
        self.login_button.state(['disabled'])
        self.progress.grid()
        self.progress.start()
        self.error_label.config(text="")
        
        def validation_callback(result):
            self.progress.stop()
            self.progress.grid_remove()
            self.login_button.state(['!disabled'])
            
            if result:
                self.root.withdraw()
                self.abrir_gestor_stock()
            else:
                self.error_label.config(text="Email o contraseña incorrectos")
        
        def error_callback(error):
            self.progress.stop()
            self.progress.grid_remove()
            self.login_button.state(['!disabled'])
            self.error_label.config(text=f"Error: {error}")
        
        self.threaded_task.execute(
            lambda: self.validar_empleado(email, password),
            validation_callback,
            error_callback
        )
    
    def validar_empleado(self, email, password):
        try:
            with open('database/users.json', 'r', encoding='utf-8') as file:
                usuarios = json.load(file)
                
            for usuario in usuarios:
                if (usuario['email'] == email and 
                    usuario['password'] == password and 
                    (usuario['rol'] == 'empleado' or usuario['rol'] == 'administrador' or usuario['rol'] == 'superusuario')):
                    return True
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Error al validar usuario: {str(e)}")
            return False
    
    def abrir_gestor_stock(self):
        stock_window = tk.Toplevel()
        app = GestorStock(stock_window)
        stock_window.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_gestor(stock_window))
    
    def cerrar_gestor(self, window):
        window.destroy()
        self.root.deiconify()  # Mostrar ventana de login nuevamente

class GestorStock:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Stock - Supermercado Tannhauser")
        self.root.geometry("1000x600")
        self.threaded_task = ThreadedTask()
        
        # Lock para operaciones con archivos
        self.file_lock = threading.Lock()
        
        # Configurar el estilo
        style = ttk.Style()
        style.configure("Header.TLabel", font=('Helvetica', 20, 'bold'))
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(self.main_frame, text="Gestión de Stock", style="Header.TLabel")
        title_label.grid(row=0, column=0, columnspan=4, pady=(0,20))
        
        # Frame para entrada de datos
        input_frame = ttk.LabelFrame(self.main_frame, text="Datos del Producto", padding="10")
        input_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0,20))
        
        # Campos de entrada
        ttk.Label(input_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = ttk.Entry(input_frame, width=10)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Nombre:").grid(row=0, column=2, padx=5, pady=5)
        self.nombre_entry = ttk.Entry(input_frame, width=30)
        self.nombre_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Cantidad:").grid(row=0, column=4, padx=5, pady=5)
        self.cantidad_entry = ttk.Entry(input_frame, width=10)
        self.cantidad_entry.grid(row=0, column=5, padx=5, pady=5)
        
        # Botones de acción
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=(0,20))
        
        ttk.Button(button_frame, text="Agregar", command=self.agregar_producto).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Modificar", command=self.modificar_producto).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=3, padx=5)
        
        # Treeview para mostrar productos
        self.tree = ttk.Treeview(self.main_frame, columns=('ID', 'Nombre', 'Cantidad'), show='headings', height=15)
        self.tree.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar columnas
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre del Producto')
        self.tree.heading('Cantidad', text='Cantidad')
        
        self.tree.column('ID', width=100, anchor='center')
        self.tree.column('Nombre', width=300, anchor='w')
        self.tree.column('Cantidad', width=100, anchor='center')
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=3, column=4, sticky='ns')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Binding para selección
        self.tree.bind('<<TreeviewSelect>>', self.item_seleccionado)
        
        # Cargar datos iniciales
        self.cargar_datos()
    
    def cargar_datos(self):
        def load_data():
            with self.file_lock:
                with open('database/stock.json', 'r', encoding='utf-8') as file:
                    return json.load(file)
        
        def update_ui(stock):
            # Limpiar treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Insertar datos
            for producto in stock:
                self.tree.insert('', tk.END, values=(
                    producto['id'],
                    producto['nombre'],
                    producto['cantidad']
                ))
        
        def error_handler(error):
            messagebox.showerror("Error", f"Error al cargar los datos: {error}")
        
        self.threaded_task.execute(load_data, update_ui, error_handler)
    
    def guardar_datos(self, stock):
        try:
            with open('database/stock.json', 'w', encoding='utf-8') as file:
                json.dump(stock, file, indent=4, ensure_ascii=False)
            self.cargar_datos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar los datos: {str(e)}")
    
    def leer_stock_actual(self):
        try:
            with open('database/stock.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer el stock: {str(e)}")
            return []
    
    def agregar_producto(self):
        id = self.id_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()
        
        if not all([id, nombre, cantidad]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
        
        try:
            id = int(id)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showwarning("Advertencia", "ID y Cantidad deben ser números")
            return
            
        # Mostrar indicador de progreso
        progress = ttk.Progressbar(self.main_frame, mode='indeterminate')
        progress.grid(row=6, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        progress.start()
        
        def add_product():
            time.sleep(0.5)  # Simular tiempo de proceso
            with self.file_lock:
                stock = self.leer_stock_actual()
                
                # Verificar si el ID ya existe
                if any(prod['id'] == id for prod in stock):
                    raise ValueError("Ya existe un producto con ese ID")
                
                nuevo_producto = {
                    'id': id,
                    'nombre': nombre,
                    'cantidad': cantidad
                }
                
                stock.append(nuevo_producto)
                self.guardar_datos(stock)
                return True
        
        def on_success(result):
            progress.stop()
            progress.destroy()
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            self.limpiar_campos()
            self.cargar_datos()
        
        def on_error(error):
            progress.stop()
            progress.destroy()
            if "tiempo de espera" in str(error):
                messagebox.showerror("Error", "La operación tardó demasiado tiempo en completarse")
            elif "Ya existe un producto" in str(error):
                messagebox.showwarning("Advertencia", str(error))
            else:
                messagebox.showerror("Error", f"Error al agregar el producto: {str(error)}")
        
        self.threaded_task.execute(add_product, on_success, on_error, timeout=5)  # timeout de 5 segundos
    
    def modificar_producto(self):
        id = self.id_entry.get().strip()
        nombre = self.nombre_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()
        
        if not all([id, nombre, cantidad]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
        
        try:
            id = int(id)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showwarning("Advertencia", "ID y Cantidad deben ser números")
            return
        
        def update_product():
            with self.file_lock:
                stock = self.leer_stock_actual()
                
                # Buscar y modificar el producto
                producto_encontrado = False
                for producto in stock:
                    if producto['id'] == id:
                        producto['nombre'] = nombre
                        producto['cantidad'] = cantidad
                        producto_encontrado = True
                        break
                
                if not producto_encontrado:
                    raise ValueError("No se encontró un producto con ese ID")
                
                self.guardar_datos(stock)
                return True
        
        def on_success(result):
            messagebox.showinfo("Éxito", "Producto modificado correctamente")
            self.limpiar_campos()
            self.cargar_datos()
        
        def on_error(error):
            if "No se encontró un producto" in str(error):
                messagebox.showwarning("Advertencia", str(error))
            else:
                messagebox.showerror("Error", f"Error al modificar el producto: {str(error)}")
        
        self.threaded_task.execute(update_product, on_success, on_error)
    
    def eliminar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para eliminar")
            return
        
        if not messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este producto?"):
            return
        
        valores = self.tree.item(seleccion[0])['values']
        id_producto = valores[0]
        
        def delete_product():
            with self.file_lock:
                stock = self.leer_stock_actual()
                new_stock = [prod for prod in stock if prod['id'] != id_producto]
                
                if len(new_stock) == len(stock):
                    raise ValueError("No se encontró el producto para eliminar")
                
                self.guardar_datos(new_stock)
                return True
        
        def on_success(result):
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            self.limpiar_campos()
            self.cargar_datos()
        
        def on_error(error):
            messagebox.showerror("Error", f"Error al eliminar el producto: {str(error)}")
        
        self.threaded_task.execute(delete_product, on_success, on_error)
    
    def item_seleccionado(self, event):
        try:
            seleccion = self.tree.selection()
            if seleccion:
                valores = self.tree.item(seleccion[0])['values']
                self.id_entry.delete(0, tk.END)
                self.nombre_entry.delete(0, tk.END)
                self.cantidad_entry.delete(0, tk.END)
                
                self.id_entry.insert(0, valores[0])
                self.nombre_entry.insert(0, valores[1])
                self.cantidad_entry.insert(0, valores[2])
        except Exception as e:
            messagebox.showerror("Error", f"Error al seleccionar el producto: {str(e)}")
    
    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = LoginEmpleado(root)
    root.mainloop()

if __name__ == "__main__":
    main()