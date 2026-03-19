import flet as ft
from controllers.user_controller import UserController
from controllers.auth_controller import AuthController
from models.session_manager import get_current_user, get_panel_route_for_current_user


class AdminEliminarUsuarioView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_eliminar_usuario")
        self._page = page
        self.go = go
        self.uc = UserController()
        self.auth = AuthController()

        self.input_nombre = ft.TextField(label="Nombre o Email del usuario", width=350)
        self.btn_buscar = ft.ElevatedButton("Buscar", icon=ft.Icons.SEARCH, on_click=self.buscar_usuario)
        self.btn_eliminar = ft.ElevatedButton("Eliminar Usuario", icon=ft.Icons.DELETE, bgcolor=ft.Colors.RED_700, on_click=self.confirmar_eliminar)
        self.btn_eliminar.disabled = True

        self.detalle = ft.Column()

        self.construir_ui()

    def construir_ui(self):
        titulo = ft.Text("Eliminar Usuario", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200)
        subtitulo = ft.Text("Introduce el nombre o email del usuario que deseas eliminar.", size=14, color=ft.Colors.WHITE70)

        boton_volver = ft.TextButton("Volver al Panel", icon=ft.Icons.ARROW_BACK, on_click=lambda e: self._volver_al_panel())

        formulario = ft.Container(
            padding=20,
            border_radius=12,
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.BLUE_GREY_900),
            content=ft.Column([self.input_nombre, ft.Row([self.btn_buscar, self.btn_eliminar], spacing=10), self.detalle]),
        )

        self.controls = [
            ft.Column(controls=[titulo, subtitulo, ft.Divider(), formulario, ft.Divider(), boton_volver], spacing=12)
        ]

    def buscar_usuario(self, e):
        q = (self.input_nombre.value or "").strip()
        if not q:
            self.page.snack_bar = ft.SnackBar(ft.Text("Introduce un nombre o email para buscar."), bgcolor=ft.Colors.RED_600)
            self.page.snack_bar.open = True
            self.page.update()
            return

        # buscar por email exacto
        user = None
        if "@" in q:
            user = self.uc.buscar_por_email(q)
            if not user:
                self.page.snack_bar = ft.SnackBar(ft.Text("Usuario no encontrado por email."), bgcolor=ft.Colors.RED_600)
                self.page.snack_bar.open = True
                self.page.update()
                return
        else:
            encontrados = self.uc.buscar_por_nombre(q)
            if not encontrados:
                self.page.snack_bar = ft.SnackBar(ft.Text("Usuario no encontrado por nombre."), bgcolor=ft.Colors.RED_600)
                self.page.snack_bar.open = True
                self.page.update()
                return
            if len(encontrados) > 1:
                # mostrar lista de coincidencias y pedir al admin especificar email
                self.detalle.controls.clear()
                self.detalle.controls.append(ft.Text("Se encontraron varias coincidencias:", color=ft.Colors.AMBER_200))
                for u in encontrados:
                    self.detalle.controls.append(ft.Text(f"ID: {u['id']} - {u['nombre']} - {u['email']} - rol: {u['rol']}", color=ft.Colors.WHITE))
                self.detalle.controls.append(ft.Text("Especifica el email para eliminar el usuario exacto.", color=ft.Colors.GREY_400))
                self.btn_eliminar.disabled = True
                self.page.update()
                return
            user = encontrados[0]

        # Un único usuario encontrado
        self.detalle.controls.clear()
        self.detalle.controls.append(ft.Text(f"ID: {user['id']}", color=ft.Colors.CYAN_100))
        self.detalle.controls.append(ft.Text(f"Nombre: {user['nombre']}", color=ft.Colors.WHITE))
        self.detalle.controls.append(ft.Text(f"Email: {user['email']}", color=ft.Colors.WHITE70))
        self.detalle.controls.append(ft.Text(f"Rol: {user['rol']}", color=ft.Colors.AMBER_200))
        # guardamos el email en el botón (closure)
        self.btn_eliminar.data = user['email']
        self.btn_eliminar.disabled = False
        self.page.update()

    def confirmar_eliminar(self, e):
        # Valida que haya un usuario seleccionado para eliminar
        email = getattr(self.btn_eliminar, 'data', None)
        if not email:
            self.page.snack_bar = ft.SnackBar(ft.Text("No hay usuario seleccionado para eliminar."), bgcolor=ft.Colors.RED_600)
            self.page.snack_bar.open = True
            self.page.update()
            return
        # Pedimos la contraseña del admin para confirmar la eliminación
        password_field = ft.TextField(label="Confirma contraseña del administrador", password=True, width=300)

        def on_confirm_password(e):
            admin = get_current_user()
            if not admin:
                self.page.snack_bar = ft.SnackBar(ft.Text("No hay sesión de administrador activa."), bgcolor=ft.Colors.RED_700)
                self.page.snack_bar.open = True
                self.page.update()
                dlg.dismiss()
                return
            # Confirmar que el usuario en sesión es admin o superusuario
            if admin.get("rol") not in ["administrador", "superusuario"]:
                self.page.snack_bar = ft.SnackBar(ft.Text("Solo administradores o superusuarios pueden eliminar usuarios."), bgcolor=ft.Colors.RED_700)
                self.page.snack_bar.open = True
                self.page.update()
                dlg.dismiss()
                return

            # Evitar que el admin se elimine a sí mismo
            if admin and admin.get('email') == email:
                self.page.snack_bar = ft.SnackBar(ft.Text("No puedes eliminar la cuenta con la que estás autenticado."), bgcolor=ft.Colors.RED_700)
                self.page.snack_bar.open = True
                self.page.update()
                dlg.dismiss()
                return

            # Validamos contraseña
            pwd = password_field.value or ""
            usuario_aut = self.auth.login(admin.get("email"), pwd)
            if not usuario_aut:
                self.page.snack_bar = ft.SnackBar(ft.Text("Contraseña incorrecta."), bgcolor=ft.Colors.RED_600)
                self.page.snack_bar.open = True
                self.page.update()
                return

            # Si todo OK, procedemos a eliminar
            actor_email = admin.get('email') if admin else None
            ok, msg = self.uc.eliminar(email, actor=actor_email)
            # Verificamos que la eliminación haya persistido
            if ok:
                # buscar por email; si todavía existe, señalamos fallo
                exists = self.uc.buscar_por_email(email)
                if exists:
                    ok = False
                    msg = "La eliminación no persistió; inténtalo de nuevo."
            color = ft.Colors.GREEN_700 if ok else ft.Colors.RED_700
            self.page.snack_bar = ft.SnackBar(ft.Text(msg), bgcolor=color)
            self.page.snack_bar.open = True
            self.page.update()
            dlg.dismiss()
            if ok:
                # If deletion succeeded, reload the user list (if open) and go back
                self.page.update()
                # Ir al panel correspondiente según rol
                current = get_current_user()
                if current and current.get('rol') == 'superusuario':
                    self.go('/panel_super')
                else:
                    self.go('/panel_admin')

        dlg = ft.AlertDialog(
            title=ft.Text("Confirmar eliminación"),
            content=ft.Column([ft.Text(f"Introduce la contraseña del administrador para confirmar la eliminación del usuario con email {email}."), password_field]),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: dlg.dismiss()),
                ft.ElevatedButton("Confirmar y Eliminar", bgcolor=ft.Colors.RED_700, on_click=on_confirm_password),
            ],
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def _volver_al_panel(self):
        """Navigate back to the panel corresponding to current user's role."""
        self.go(get_panel_route_for_current_user())
