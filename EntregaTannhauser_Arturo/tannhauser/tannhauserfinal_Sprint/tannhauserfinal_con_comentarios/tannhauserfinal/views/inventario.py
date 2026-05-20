import flet as ft
from mysql.connector import Error
from models.db import get_connection
from models.session_manager import get_current_user


def InventarioView(page: ft.Page, go, editable: bool = False):
    usuario = get_current_user() or {}
    rol = (usuario.get("rol") or "cliente").lower()

    busqueda = ft.TextField(
        hint_text="Buscar por nombre o SKU",
        prefix_icon=ft.Icons.SEARCH_ROUNDED,
        border_radius=18,
        border_color=ft.Colors.with_opacity(0.20, ft.Colors.CYAN_200),
        focused_border_color="#67E8F9",
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        width=420,
    )

    total_productos_txt = ft.Text("0", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    total_unidades_txt = ft.Text("0", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    stock_bajo_txt = ft.Text("0", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    valor_total_txt = ft.Text("0.00 €", size=26, weight=ft.FontWeight.BOLD, color="#8BE3FF")

    productos_column = ft.Column(spacing=16)

    nombre_input = ft.TextField(label="Nombre", border_radius=14)
    sku_input = ft.TextField(label="SKU", border_radius=14)
    cantidad_input = ft.TextField(label="Cantidad", border_radius=14)
    precio_input = ft.TextField(label="Precio (€)", border_radius=14)
    is_active_switch = ft.Switch(label="Producto activo", value=True)

    producto_editando = {"id": None}

    def show_message(texto: str, ok: bool = True):
        page.snack_bar = ft.SnackBar(
            ft.Text(texto),
            bgcolor=ft.Colors.GREEN_600 if ok else ft.Colors.RED_600,
        )
        page.snack_bar.open = True
        page.update()

    def ruta_volver():
        if editable:
            if rol == "superusuario":
                return "/panel_super"
            if rol == "administrador":
                return "/panel_admin"
            if rol == "empleado":
                return "/panel_empleado"
            return "/"
        return "/panel_usuario"

    def consultar_productos():
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        try:
            sql = """
                SELECT id, sku, nombre, cantidad, precio, is_active, created_at, updated_at
                FROM products
            """
            filtros = []
            params = []

            if not editable:
                filtros.append("is_active = 1")

            texto = (busqueda.value or "").strip().lower()
            if texto:
                filtros.append("(LOWER(nombre) LIKE %s OR LOWER(sku) LIKE %s)")
                params.append(f"%{texto}%")
                params.append(f"%{texto}%")

            if filtros:
                sql += " WHERE " + " AND ".join(filtros)

            sql += " ORDER BY nombre ASC"

            cursor.execute(sql, tuple(params))
            return cursor.fetchall()
        except Error as e:
            print(f"Error consultando productos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def cerrar_dialog(dialog):
        page.close(dialog)

    def cargar_en_formulario(producto=None):
        if producto:
            producto_editando["id"] = producto["id"]
            nombre_input.value = producto.get("nombre", "")
            sku_input.value = producto.get("sku", "")
            cantidad_input.value = str(producto.get("cantidad", ""))
            precio_input.value = str(producto.get("precio", ""))
            is_active_switch.value = bool(producto.get("is_active", 1))
        else:
            producto_editando["id"] = None
            nombre_input.value = ""
            sku_input.value = ""
            cantidad_input.value = ""
            precio_input.value = ""
            is_active_switch.value = True

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                "Editar producto" if producto else "Nuevo producto",
                weight=ft.FontWeight.BOLD,
            ),
            content=ft.Container(
                width=420,
                content=ft.Column(
                    [
                        nombre_input,
                        sku_input,
                        cantidad_input,
                        precio_input,
                        is_active_switch,
                    ],
                    tight=True,
                    spacing=12,
                ),
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialog(dialog)),
                ft.Button(
                    "Guardar",
                    on_click=lambda e: guardar_producto(dialog),
                    bgcolor="#67E8F9",
                    color=ft.Colors.BLACK,
                ),
            ],
        )

        page.open(dialog)

    def guardar_producto(dialog):
        nombre = (nombre_input.value or "").strip()
        sku = (sku_input.value or "").strip()
        cantidad = (cantidad_input.value or "").strip()
        precio = (precio_input.value or "").strip().replace(",", ".")

        if not nombre or not sku or not cantidad or not precio:
            show_message("Completa todos los campos del producto.", False)
            return

        try:
            cantidad_val = int(cantidad)
            precio_val = float(precio)
        except Exception:
            show_message("Cantidad o precio no válidos.", False)
            return

        conn = get_connection()
        if not conn:
            show_message("No se pudo conectar con la base de datos.", False)
            return

        cursor = conn.cursor()
        try:
            if producto_editando["id"] is None:
                cursor.execute("""
                    INSERT INTO products (sku, nombre, cantidad, precio, is_active, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
                """, (
                    sku,
                    nombre,
                    cantidad_val,
                    precio_val,
                    1 if is_active_switch.value else 0,
                ))
            else:
                cursor.execute("""
                    UPDATE products
                    SET sku = %s,
                        nombre = %s,
                        cantidad = %s,
                        precio = %s,
                        is_active = %s,
                        updated_at = NOW()
                    WHERE id = %s
                """, (
                    sku,
                    nombre,
                    cantidad_val,
                    precio_val,
                    1 if is_active_switch.value else 0,
                    producto_editando["id"],
                ))

            conn.commit()
            cerrar_dialog(dialog)
            show_message("Producto guardado correctamente.", True)
            refrescar_productos()
        except Error as e:
            conn.rollback()
            show_message(f"Error al guardar el producto: {e}", False)
        finally:
            cursor.close()
            conn.close()

    def cambiar_estado(producto_id: int, activar: bool):
        conn = get_connection()
        if not conn:
            show_message("No se pudo conectar con la base de datos.", False)
            return

        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE products
                SET is_active = %s,
                    updated_at = NOW()
                WHERE id = %s
            """, (1 if activar else 0, producto_id))
            conn.commit()
            show_message("Estado del producto actualizado correctamente.", True)
            refrescar_productos()
        except Error as e:
            conn.rollback()
            show_message(f"Error al actualizar el producto: {e}", False)
        finally:
            cursor.close()
            conn.close()

    def tarjeta_resumen(titulo: str, valor_control: ft.Control):
        return ft.Container(
            width=260,
            padding=22,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Text(titulo, size=14, color=ft.Colors.WHITE60),
                    valor_control,
                ],
                spacing=10,
            ),
        )

    def tarjeta_producto(producto: dict):
        cantidad = int(producto.get("cantidad", 0) or 0)
        precio = float(producto.get("precio", 0) or 0)
        activo = bool(producto.get("is_active", 1))

        if cantidad <= 5:
            stock_texto = "Stock crítico"
            stock_color = "#FF8A8A"
        elif cantidad <= 15:
            stock_texto = "Stock medio"
            stock_color = "#FFD166"
        else:
            stock_texto = "Disponible"
            stock_color = "#8BE3FF"

        acciones = []
        if editable:
            acciones = [
                ft.OutlinedButton(
                    "Editar",
                    icon=ft.Icons.EDIT_ROUNDED,
                    on_click=lambda e, p=producto: cargar_en_formulario(p),
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        side=ft.BorderSide(1, ft.Colors.with_opacity(0.18, ft.Colors.WHITE)),
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                ),
                ft.Button(
                    "Desactivar" if activo else "Activar",
                    icon=ft.Icons.TOGGLE_OFF_ROUNDED if activo else ft.Icons.TOGGLE_ON_ROUNDED,
                    on_click=lambda e, pid=producto["id"], a=not activo: cambiar_estado(pid, a),
                    bgcolor="#67E8F9",
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                ),
            ]

        return ft.Container(
            padding=20,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Container(
                        width=58,
                        height=58,
                        border_radius=18,
                        bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.CYAN_200),
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(
                            ft.Icons.INVENTORY_2_ROUNDED,
                            color="#8BE3FF",
                            size=30,
                        ),
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                producto.get("nombre", "Producto"),
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                f"SKU: {producto.get('sku', '—')}",
                                size=12,
                                color=ft.Colors.WHITE54,
                            ),
                            ft.Text(
                                f"Precio: {precio:.2f} €",
                                size=14,
                                color="#8BE3FF",
                                weight=ft.FontWeight.W_600,
                            ),
                        ],
                        spacing=6,
                        expand=True,
                    ),
                    ft.Column(
                        [
                            ft.Container(
                                padding=ft.Padding(10, 6, 10, 6),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(
                                    0.14,
                                    ft.Colors.GREEN_300 if activo else ft.Colors.RED_300,
                                ),
                                content=ft.Text(
                                    "Activo" if activo else "Inactivo",
                                    size=11,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                            ),
                            ft.Text(
                                f"Stock: {cantidad}",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.RIGHT,
                            ),
                            ft.Text(
                                stock_texto,
                                size=13,
                                weight=ft.FontWeight.BOLD,
                                color=stock_color,
                                text_align=ft.TextAlign.RIGHT,
                            ),
                        ],
                        spacing=8,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                    ),
                ],
                spacing=18,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ) if not editable else ft.Container(
            padding=20,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=58,
                                height=58,
                                border_radius=18,
                                bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.CYAN_200),
                                alignment=ft.Alignment.CENTER,
                                content=ft.Icon(
                                    ft.Icons.INVENTORY_2_ROUNDED,
                                    color="#8BE3FF",
                                    size=30,
                                ),
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        producto.get("nombre", "Producto"),
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        f"SKU: {producto.get('sku', '—')}",
                                        size=12,
                                        color=ft.Colors.WHITE54,
                                    ),
                                ],
                                spacing=4,
                                expand=True,
                            ),
                            ft.Container(
                                padding=ft.Padding(10, 6, 10, 6),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(
                                    0.14,
                                    ft.Colors.GREEN_300 if activo else ft.Colors.RED_300,
                                ),
                                content=ft.Text(
                                    "Activo" if activo else "Inactivo",
                                    size=11,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                            ),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Text(
                                f"Precio: {precio:.2f} €",
                                size=15,
                                color="#8BE3FF",
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Text(
                                f"Stock: {cantidad}",
                                size=15,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                stock_texto,
                                size=13,
                                color=stock_color,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(acciones, spacing=10, wrap=True),
                ],
                spacing=12,
            ),
        )

    def refrescar_productos(e=None):
        productos = consultar_productos()

        total_productos = len(productos)
        total_unidades = sum(int(p.get("cantidad", 0) or 0) for p in productos)
        stock_bajo = sum(1 for p in productos if int(p.get("cantidad", 0) or 0) <= 10)
        valor_total = sum(
            float(p.get("precio", 0) or 0) * int(p.get("cantidad", 0) or 0)
            for p in productos
        )

        total_productos_txt.value = str(total_productos)
        total_unidades_txt.value = str(total_unidades)
        stock_bajo_txt.value = str(stock_bajo)
        valor_total_txt.value = f"{valor_total:.2f} €"

        productos_column.controls.clear()

        if productos:
            for producto in productos:
                productos_column.controls.append(tarjeta_producto(producto))
        else:
            productos_column.controls.append(
                ft.Container(
                    padding=30,
                    border_radius=22,
                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                    content=ft.Column(
                        [
                            ft.Icon(
                                ft.Icons.SEARCH_OFF_ROUNDED,
                                color=ft.Colors.WHITE60,
                                size=40,
                            ),
                            ft.Text(
                                "No se han encontrado productos.",
                                size=16,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                )
            )

        page.update()

    busqueda.on_change = refrescar_productos

    acciones_superiores = ft.Row(
        [
            busqueda,
            ft.Button(
                "Nuevo producto",
                icon=ft.Icons.ADD_ROUNDED,
                on_click=lambda e: cargar_en_formulario(None),
                bgcolor="#67E8F9",
                color=ft.Colors.BLACK,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=18),
                ),
                visible=editable,
            ),
            ft.OutlinedButton(
                "Volver",
                icon=ft.Icons.ARROW_BACK_ROUNDED,
                on_click=lambda e: go(ruta_volver()),
                style=ft.ButtonStyle(
                    color=ft.Colors.WHITE,
                    side=ft.BorderSide(1, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                    shape=ft.RoundedRectangleBorder(radius=18),
                ),
            ),
        ],
        spacing=14,
        wrap=True,
    )

    resumen_row = ft.Row(
        [
            tarjeta_resumen("Productos visibles", total_productos_txt),
            tarjeta_resumen("Unidades totales", total_unidades_txt),
            tarjeta_resumen("Stock bajo", stock_bajo_txt),
            tarjeta_resumen("Valor estimado", valor_total_txt),
        ],
        spacing=16,
        wrap=True,
    )

    contenido = ft.Container(
        expand=True,
        padding=28,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
        ),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    "Inventario del supermercado",
                                    size=38,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                ft.Text(
                                    "Consulta el catálogo disponible, el stock actual y el valor total del inventario.",
                                    size=16,
                                    color=ft.Colors.WHITE70,
                                ),
                            ],
                            spacing=6,
                            expand=True,
                        ),
                    ]
                ),
                ft.Container(height=18),
                acciones_superiores,
                ft.Container(height=20),
                resumen_row,
                ft.Container(height=24),
                productos_column,
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    refrescar_productos()

    return ft.View(
        route="/inventario_edit" if editable else "/inventario",
        padding=0,
        spacing=0,
        controls=[contenido],
    )