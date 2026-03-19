import flet as ft
from controllers.inventory_controller import InventoryController
from models.session_manager import get_panel_route_for_current_user


class InventarioView(ft.View):
    def __init__(self, page: ft.Page, go, editable=False):
        super().__init__(route="/inventario")
        self._page = page
        self.go = go
        self.controller = InventoryController()
        self.editable = editable
        self.lista = ft.Column(scroll=ft.ScrollMode.AUTO)
        # keep a mapping of quantity fields for editing
        self._qty_fields = {}
        self.construir_ui()

    def did_mount(self):
        self.cargar_stock()

    def construir_ui(self):
        titulo = ft.Text("Inventario - Stock del Supermercado", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200)
        subtitulo = ft.Text("Lista de productos en el almacén", size=14, color=ft.Colors.WHITE70)

        boton_volver = ft.TextButton("Volver", icon=ft.Icons.ARROW_BACK, on_click=lambda e: self.go(get_panel_route_for_current_user()))

        self.controls = [
            ft.Column(controls=[
                titulo,
                subtitulo,
                ft.Divider(),
                self.lista,
                ft.Divider(),
                boton_volver
            ], spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ]

    def cargar_stock(self):
        self.lista.controls.clear()
        items = self.controller.listar_stock()
        for it in items:
            # If editable: show a numeric TextField and Save button
            if self.editable:
                qty_field = ft.TextField(value=str(it['cantidad']), width=80, keyboard_type=ft.KeyboardType.NUMBER)
                self._qty_fields[it['id']] = qty_field

                save_btn = ft.ElevatedButton("Guardar", icon=ft.Icons.SAVE, on_click=lambda e, item_id=it['id']: self._save_cantidad(e, item_id))

                fila = ft.Row(
                    [
                        ft.Text(f"{it['id']}", width=40),
                        ft.Text(it['nombre'], width=260),
                        qty_field,
                        ft.Text(f"${it['precio']:.2f}", width=80),
                        save_btn,
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            else:
                fila = ft.Row(
                    [
                        ft.Text(f"{it['id']}", width=40),
                        ft.Text(it['nombre'], width=260),
                        ft.Text(str(it['cantidad']), width=80),
                        ft.Text(f"${it['precio']:.2f}", width=80),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )

            self.lista.controls.append(ft.Container(content=fila, padding=8, border=ft.border.all(1, ft.Colors.BLUE_GREY_700), border_radius=8))
        self.update()

    def _save_cantidad(self, e, item_id: int):
        field = self._qty_fields.get(item_id)
        if not field:
            self.page.snack_bar = ft.SnackBar(ft.Text("Campo de cantidad no encontrado"), bgcolor=ft.Colors.RED_600)
            self.page.snack_bar.open = True
            self.page.update()
            return

        try:
            new_qty = int(field.value)
        except Exception:
            self.page.snack_bar = ft.SnackBar(ft.Text("Introduce un número válido"), bgcolor=ft.Colors.RED_600)
            self.page.snack_bar.open = True
            self.page.update()
            return

        ok = self.controller.actualizar_cantidad(item_id, new_qty)
        if ok:
            self.page.snack_bar = ft.SnackBar(ft.Text("Cantidad actualizada"), bgcolor=ft.Colors.GREEN_700)
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("No se pudo actualizar la cantidad"), bgcolor=ft.Colors.RED_700)
        self.page.snack_bar.open = True
        self.cargar_stock()
