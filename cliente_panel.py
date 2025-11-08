import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from thread_utils import ThreadedTask, file_lock

class ClientePanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Cliente - Stock Disponible")
        self.root.geometry("800x600")
        self.threaded_task = ThreadedTask()
        
        # Configurar el estilo
        style = ttk.Style()
        style.configure("Header.TLabel", font=('Helvetica', 24, 'bold'))
        style.configure("Subheader.TLabel", font=('Helvetica', 12))
        
        # Configurar el estilo
        style = ttk.Style()
        style.configure("Header.TLabel", font=('Helvetica', 24, 'bold'))
        style.configure("Subheader.TLabel", font=('Helvetica', 12))
        
        # Crear el frame principal
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título principal
        title_label = ttk.Label(self.main_frame, 
                              text="Supermercado Tannhauser", 
                              style="Header.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0,5))
        
        # Subtítulo
        subtitle_label = ttk.Label(self.main_frame, 
                                 text="Inventario Actual", 
                                 style="Subheader.TLabel")
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0,20))
        
        # Crear frame para el Treeview
        tree_frame = ttk.Frame(self.main_frame)
        tree_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear Treeview para mostrar los productos
        self.tree = ttk.Treeview(tree_frame, 
                                columns=('ID', 'Nombre', 'Cantidad', 'Estado'),
                                show='headings',
                                height=15)
        
        # Definir las columnas
        self.tree.heading('ID', text='Código')
        self.tree.heading('Nombre', text='Producto')
        self.tree.heading('Cantidad', text='Unidades Disponibles')
        self.tree.heading('Estado', text='Estado')
        
        # Ajustar el ancho de las columnas
        self.tree.column('ID', width=100, anchor='center')
        self.tree.column('Nombre', width=250, anchor='w')
        self.tree.column('Cantidad', width=150, anchor='center')
        self.tree.column('Estado', width=150, anchor='center')
        
        # Posicionar el Treeview
        self.tree.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Botón de actualizar
        ttk.Button(self.main_frame, text="Actualizar Stock", command=self.cargar_stock).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Cargar el stock inicial
        self.cargar_stock()

    def cargar_stock(self):
        # Mostrar indicador de carga
        self.tree.configure(cursor="wait")
        self.root.configure(cursor="wait")
        
        def load_data():
            with file_lock:
                with open('database/stock.json', 'r', encoding='utf-8') as file:
                    return json.load(file)
        
        def update_ui(stock):
            # Limpiar treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Insertar datos con estado de stock
            for producto in stock:
                cantidad = producto['cantidad']
                if cantidad > 100:
                    estado = "Bien Abastecido"
                    tag = "alto"
                elif 50 <= cantidad <= 100:
                    estado = "Stock Medio"
                    tag = "medio"
                elif 1 <= cantidad < 50:
                    estado = "Stock Bajo"
                    tag = "bajo"
                else:
                    estado = "Sin Stock"
                    tag = "agotado"
                
                self.tree.insert('', tk.END, values=(
                    producto['id'],
                    producto['nombre'],
                    f"{cantidad} unidades",
                    estado
                ), tags=(tag,))
            
            # Configurar colores para los diferentes estados
            self.tree.tag_configure('alto', foreground='green')
            self.tree.tag_configure('medio', foreground='orange')
            self.tree.tag_configure('bajo', foreground='red')
            self.tree.tag_configure('agotado', foreground='gray')
            
            # Restaurar cursor y mostrar mensaje
            self.tree.configure(cursor="")
            self.root.configure(cursor="")
            messagebox.showinfo("Actualización", "Stock actualizado correctamente")
        
        def error_handler(error):
            messagebox.showerror("Error", f"Error al cargar el stock: {error}")
            # Restaurar cursor
            self.tree.configure(cursor="")
            self.root.configure(cursor="")
        
        self.threaded_task.execute(load_data, update_ui, error_handler)

def main():
    root = tk.Tk()
    app = ClientePanel(root)
    root.mainloop()

if __name__ == "__main__":
    main()