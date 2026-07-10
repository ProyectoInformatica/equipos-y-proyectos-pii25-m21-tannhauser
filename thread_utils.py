import threading
from queue import Queue, Empty
import tkinter as tk
import time

class ThreadedTask:
    def __init__(self):
        self.queue = Queue()
        self.default_timeout = 10  # Timeout por defecto de 10 segundos
    
    def execute(self, func, callback=None, error_callback=None, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
            
        start_time = time.time()
        
        def thread_target():
            try:
                result = func()
                if time.time() - start_time < timeout:
                    self.queue.put(('success', result))
            except Exception as e:
                if time.time() - start_time < timeout:
                    self.queue.put(('error', str(e)))
        
        def check_queue():
            try:
                if time.time() - start_time > timeout:
                    if error_callback:
                        error_callback("La operación excedió el tiempo de espera")
                    return
                
                try:
                    message_type, result = self.queue.get_nowait()
                    if message_type == 'success' and callback:
                        callback(result)
                    elif message_type == 'error' and error_callback:
                        error_callback(result)
                except Empty:
                    if time.time() - start_time < timeout:
                        tk.Tk().after(100, check_queue)
                    else:
                        if error_callback:
                            error_callback("La operación excedió el tiempo de espera")
            except Exception as e:
                if error_callback:
                    error_callback(f"Error en el proceso: {str(e)}")
        
        thread = threading.Thread(target=thread_target)
        thread.daemon = True
        thread.start()
        
        if callback or error_callback:
            tk.Tk().after(100, check_queue)

# Lock global para operaciones con archivos
file_lock = threading.Lock()