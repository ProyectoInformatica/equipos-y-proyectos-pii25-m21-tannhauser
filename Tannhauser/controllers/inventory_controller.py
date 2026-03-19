from models.inventory_manager import InventoryManager


class InventoryController:
    def __init__(self):
        self.manager = InventoryManager()

    def listar_stock(self):
        return self.manager.listar()

    def obtener_item(self, item_id: int):
        return self.manager.obtener_por_id(item_id)

    def actualizar_cantidad(self, item_id: int, cantidad: int):
        return self.manager.actualizar_cantidad(item_id, cantidad)

    def agregar_item(self, nombre: str, cantidad: int, precio: float):
        return self.manager.agregar_item(nombre, cantidad, precio)

    def eliminar_item(self, item_id: int):
        return self.manager.eliminar_item(item_id)
