import flet as ft
from controllers.umbral_controller import UmbralController
from utils.navigation import ruta_dashboard_por_rol


class AdminUmbralesView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_umbrales", padding=0, spacing=0)
        self._page = page
        self.go = go
        self.controller = UmbralController()
        self.lista = ft.Column(spacing=16)
        self.dialog_nueva_regla = None
        self.controls = [self._build_ui()]

    def _mostrar_mensaje(self, texto, ok=True):
        self._page.snack_bar = ft.SnackBar(
            ft.Text(texto),
            bgcolor=ft.Colors.GREEN_600 if ok else ft.Colors.RED_600,
        )
        self._page.snack_bar.open = True
        self._page.update()

    def _guardar(self, row_id, op_dd, val_tf, sev_dd, title_tf, desc_tf, active_sw):
        try:
            valor = float(str(val_tf.value).replace(",", "."))
        except Exception:
            self._mostrar_mensaje("El umbral debe ser numérico.", ok=False)
            return

        ok, msg = self.controller.actualizar_umbral(
            row_id,
            op_dd.value,
            valor,
            sev_dd.value,
            title_tf.value.strip(),
            desc_tf.value.strip(),
            active_sw.value,
        )
        self._mostrar_mensaje(msg, ok)
        if ok:
            self.refrescar()

    def _eliminar(self, row_id):
        ok, msg = self.controller.eliminar_umbral(row_id)
        self._mostrar_mensaje(msg, ok)
        if ok:
            self.refrescar()

    def _cerrar_dialogo(self, e=None):
        if self.dialog_nueva_regla:
            self.dialog_nueva_regla.open = False
            self._page.update()

    def _crear_nueva_regla(self, e=None):
        state_dd = ft.Dropdown(
            width=220,
            label="Sensor",
            value="TEMP_AIR",
            options=[
                ft.dropdown.Option("TEMP_AIR", "Temperatura ambiente"),
                ft.dropdown.Option("HUM_AIR", "Humedad ambiente"),
                ft.dropdown.Option("MQ135_AIR", "Calidad del aire"),
                ft.dropdown.Option("DISTANCE_CM", "Distancia / puerta"),
            ],
            border_radius=14,
        )

        op_dd = ft.Dropdown(
            width=170,
            label="Operador",
            value="gt",
            options=[
                ft.dropdown.Option("gt", "Mayor que"),
                ft.dropdown.Option("lt", "Menor que"),
            ],
            border_radius=14,
        )

        val_tf = ft.TextField(
            label="Umbral",
            width=170,
            value="0",
            border_radius=14,
        )

        sev_dd = ft.Dropdown(
            width=180,
            label="Severidad",
            value="warning",
            options=[
                ft.dropdown.Option("info", "Info"),
                ft.dropdown.Option("warning", "Warning"),
                ft.dropdown.Option("critical", "Critical"),
            ],
            border_radius=14,
        )

        title_tf = ft.TextField(
            label="Título de la alerta",
            value="Nueva alerta",
            width=520,
            border_radius=14,
        )

        desc_tf = ft.TextField(
            label="Descripción",
            value="Descripción de la alerta",
            multiline=True,
            min_lines=2,
            max_lines=4,
            width=520,
            border_radius=14,
        )

        active_sw = ft.Switch(
            label="Regla activa",
            value=True,
            active_color="#64D7FF",
        )

        def guardar_nueva(ev):
            try:
                valor = float(str(val_tf.value).replace(",", "."))
            except Exception:
                self._mostrar_mensaje("El umbral debe ser numérico.", ok=False)
                return

            ok, msg = self.controller.crear_umbral(
                state_dd.value,
                op_dd.value,
                valor,
                sev_dd.value,
                title_tf.value.strip(),
                desc_tf.value.strip(),
                active_sw.value,
            )

            self._mostrar_mensaje(msg, ok)

            if ok:
                self._cerrar_dialogo()
                self.refrescar()

        self.dialog_nueva_regla = ft.AlertDialog(
            modal=True,
            bgcolor="#0F172A",
            title=ft.Text(
                "Nueva regla de alerta",
                color=ft.Colors.WHITE,
                weight=ft.FontWeight.BOLD,
            ),
            content=ft.Container(
                width=560,
                content=ft.Column(
                    [
                        state_dd,
                        ft.Row(
                            [op_dd, val_tf, sev_dd],
                            wrap=True,
                            spacing=12,
                        ),
                        title_tf,
                        desc_tf,
                        active_sw,
                    ],
                    tight=True,
                    spacing=12,
                ),
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=self._cerrar_dialogo),
                ft.ElevatedButton(
                    "Crear regla",
                    icon=ft.Icons.ADD_ALERT_ROUNDED,
                    bgcolor="#64D7FF",
                    color=ft.Colors.BLACK,
                    on_click=guardar_nueva,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self._page.open(self.dialog_nueva_regla)

    def _card_regla(self, row):
        op_dd = ft.Dropdown(
            width=160,
            value=row["operator_type"],
            options=[
                ft.dropdown.Option("gt", "Mayor que"),
                ft.dropdown.Option("lt", "Menor que"),
            ],
            border_radius=14,
        )

        val_tf = ft.TextField(
            label="Umbral",
            value=str(row["threshold_value"]),
            width=170,
            border_radius=14,
        )

        sev_dd = ft.Dropdown(
            width=180,
            value=row["severity"],
            options=[
                ft.dropdown.Option("info", "Info"),
                ft.dropdown.Option("warning", "Warning"),
                ft.dropdown.Option("critical", "Critical"),
            ],
            border_radius=14,
        )

        title_tf = ft.TextField(
            label="Título",
            value=row["title"],
            expand=True,
            border_radius=14,
        )

        desc_tf = ft.TextField(
            label="Descripción",
            value=row["description_template"],
            multiline=True,
            min_lines=2,
            max_lines=4,
            expand=True,
            border_radius=14,
        )

        active_sw = ft.Switch(
            label="Activo",
            value=bool(row["is_active"]),
            active_color="#64D7FF",
        )

        severity = (row.get("severity") or "warning").lower()
        if severity == "critical":
            sev_color = "#F87171"
        elif severity == "warning":
            sev_color = "#FBBF24"
        else:
            sev_color = "#67E8F9"

        return ft.Container(
            width=1180,
            padding=22,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        padding=ft.Padding(12, 6, 12, 6),
                                        border_radius=999,
                                        bgcolor=ft.Colors.with_opacity(0.18, sev_color),
                                        content=ft.Text(
                                            row["state_code"],
                                            size=12,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                    ),
                                    ft.Text(
                                        f"Regla #{row['id']}",
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                ],
                                spacing=10,
                            ),
                            ft.Text(
                                f"Última actualización: {row['updated_at']}",
                                color=ft.Colors.WHITE60,
                                size=12,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        [op_dd, val_tf, sev_dd, active_sw],
                        wrap=True,
                        spacing=12,
                    ),
                    title_tf,
                    desc_tf,
                    ft.Row(
                        [
                            ft.OutlinedButton(
                                "Eliminar",
                                icon=ft.Icons.DELETE_OUTLINE_ROUNDED,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.RED_300,
                                    side=ft.BorderSide(1.0, ft.Colors.with_opacity(0.22, ft.Colors.RED_300)),
                                    shape=ft.RoundedRectangleBorder(radius=14),
                                ),
                                on_click=lambda e, rid=row["id"]: self._eliminar(rid),
                            ),
                            ft.ElevatedButton(
                                "Guardar cambios",
                                icon=ft.Icons.SAVE_ROUNDED,
                                bgcolor="#64D7FF",
                                color=ft.Colors.BLACK,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=14),
                                ),
                                on_click=lambda e, rid=row["id"], o=op_dd, v=val_tf, s=sev_dd, t=title_tf, d=desc_tf, a=active_sw:
                                    self._guardar(rid, o, v, s, t, d, a),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10,
                    ),
                ],
                spacing=14,
            ),
        )

    def refrescar(self, e=None):
        self.lista.controls.clear()
        rows = self.controller.obtener_umbrales()

        if not rows:
            self.lista.controls.append(
                ft.Container(
                    width=1180,
                    padding=22,
                    border_radius=22,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Text(
                        "No hay reglas configuradas.",
                        color=ft.Colors.WHITE70,
                        size=15,
                    ),
                )
            )
            self.update()
            return

        for row in rows:
            self.lista.controls.append(self._card_regla(row))

        self.update()

    def did_mount(self):
        self.refrescar()

    def _build_ui(self):
        return ft.Container(
            expand=True,
            padding=28,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
            ),
            content=ft.Column(
                [
                    ft.Container(
                        width=1180,
                        padding=24,
                        border_radius=28,
                        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Gestión de umbrales",
                                            size=34,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            "Define múltiples reglas por sensor, con distintas severidades y distintos valores de disparo.",
                                            size=15,
                                            color=ft.Colors.WHITE70,
                                        ),
                                    ],
                                    spacing=6,
                                ),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "Nueva regla",
                                            icon=ft.Icons.ADD_ALERT_ROUNDED,
                                            bgcolor="#64D7FF",
                                            color=ft.Colors.BLACK,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=self._crear_nueva_regla,
                                        ),
                                        ft.OutlinedButton(
                                            "Refrescar",
                                            icon=ft.Icons.REFRESH_ROUNDED,
                                            style=ft.ButtonStyle(
                                                color=ft.Colors.WHITE,
                                                side=ft.BorderSide(1.0, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=self.refrescar,
                                        ),
                                        ft.OutlinedButton(
                                            "Volver al panel",
                                            icon=ft.Icons.ARROW_BACK_ROUNDED,
                                            style=ft.ButtonStyle(
                                                color=ft.Colors.WHITE,
                                                side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=lambda e: self.go(ruta_dashboard_por_rol()),
                                        ),
                                    ],
                                    spacing=12,
                                    wrap=True,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                    ft.Container(height=18),
                    ft.Container(
                        width=1180,
                        padding=20,
                        border_radius=24,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Reglas configuradas",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                self.lista,
                            ],
                            spacing=16,
                        ),
                    ),
                ],
                spacing=0,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )