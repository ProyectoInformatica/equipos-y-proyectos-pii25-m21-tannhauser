import asyncio

import flet as ft

from models.chat_manager import ChatManager
from models.session_manager import get_current_user
from utils.navigation import ruta_dashboard_por_rol
from utils.ui_premium import (
    ACCENT_STRONG,
    CHAMPAGNE,
    TEXT_MUTED,
    glass_panel,
    premium_empty_state,
    premium_snackbar,
    premium_text_field,
    premium_dropdown,
    primary_button,
    secondary_button,
    status_badge,
)


class ChatInternoView(ft.View):
    REFRESH_SECONDS = 8
    ALLOWED_ROLES = {"cliente", "empleado", "administrador", "superusuario"}

    def __init__(self, page: ft.Page, go):
        super().__init__(route="/chat_interno", padding=0, spacing=0)
        self.page = page
        self.go = go
        self.groups = []
        self.current_members = []
        self.current_can_manage = False
        self.selected_group_id = None
        self.emoji_panel_visible = False
        self._group_image_target = None
        self._running = False
        self.user = {}
        self.manager = None

        try:
            self.user = get_current_user() or {}
            rol = (self.user.get("rol") or "").strip().lower()
            if rol not in self.ALLOWED_ROLES:
                self.controls = [self.error_page("Acceso restringido", "No tienes conversaciones asignadas en el chat.")]
                return

            self.manager = ChatManager()
            if not self.manager.ensure_tables():
                detail = self.manager.last_error or "No se pudieron preparar las tablas del chat."
                self.controls = [self.error_page("Chat no disponible", detail)]
                return

            self.groups_slot = ft.Container(width=320, expand=True)
            self.messages_slot = ft.Container(expand=True)
            self.detail_slot = ft.Container(width=300, expand=True)
            self.message_input = premium_text_field(
                ft.TextField(
                    hint_text="Escribe un mensaje...",
                    multiline=True,
                    min_lines=1,
                    max_lines=3,
                    expand=True,
                )
            )
            self.file_picker = ft.FilePicker(on_result=self.on_file_picked)
            self.group_image_picker = ft.FilePicker(on_result=self.on_group_image_picked)
            if hasattr(page, "overlay") and self.file_picker not in page.overlay:
                page.overlay.append(self.file_picker)
            if hasattr(page, "overlay") and self.group_image_picker not in page.overlay:
                page.overlay.append(self.group_image_picker)

            self.controls = [self.build()]
            self.refresh_all()
        except Exception as e:
            self.controls = [self.error_page("No se pudo abrir la mensajeria", f"{type(e).__name__}: {e}")]

    def did_mount(self):
        if not self.manager or not hasattr(self, "messages_slot"):
            return
        self._running = True
        self.page.run_task(self.auto_refresh)

    def will_unmount(self):
        self._running = False

    async def auto_refresh(self):
        while self._running:
            await asyncio.sleep(self.REFRESH_SECONDS)
            if self._running:
                try:
                    self.refresh_messages()
                except Exception as e:
                    self.render_controlled_error("No se pudo refrescar el chat.", e)

    def show_message(self, text, ok=True):
        self.page.snack_bar = premium_snackbar(text, ok=ok)
        self.page.snack_bar.open = True
        self.page.update()

    def build(self):
        can_create_group = self.manager.can_create_group(self.user.get("rol"))
        can_create_direct = self.manager.can_create_direct(self.user.get("rol"))
        header = ft.Container(
            height=104,
            padding=ft.Padding(22, 18, 22, 18),
            border_radius=26,
            bgcolor=ft.Colors.with_opacity(0.075, ft.Colors.WHITE),
            border=ft.border.all(1.1, ft.Colors.with_opacity(0.20, CHAMPAGNE)),
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Comunicacion interna", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(
                                "Mensajeria de equipo para conversaciones, grupos y soporte.",
                                size=15,
                                color=TEXT_MUTED,
                            ),
                        ],
                        spacing=6,
                    ),
                    ft.Row(
                        [
                            primary_button("Nuevo grupo", ft.Icons.ADD_ROUNDED, on_click=self.open_group_dialog, visible=can_create_group),
                            secondary_button("Nuevo chat", ft.Icons.PERSON_ADD_ALT_1_ROUNDED, on_click=self.open_direct_dialog, visible=can_create_direct),
                            self.icon_action(ft.Icons.REFRESH_ROUNDED, "Refrescar", lambda e: self.refresh_all()),
                        ],
                        spacing=12,
                        wrap=True,
                    ),
                    self.icon_action(ft.Icons.ARROW_BACK_ROUNDED, "Volver al panel", lambda e: self.go(ruta_dashboard_por_rol())),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        return ft.Container(
            expand=True,
            padding=18,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
            ),
            content=ft.Column(
                [
                    header,
                    ft.Row(
                        [
                            self.groups_slot,
                            self.messages_slot,
                            self.detail_slot,
                        ],
                        spacing=18,
                        expand=True,
                        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    ),
                ],
                spacing=14,
                expand=True,
            ),
        )

    def refresh_all(self):
        try:
            self.groups = self.manager.get_groups_for_user(self.user.get("id"), self.user.get("rol"))
            if self.groups and not self.selected_group_id:
                self.selected_group_id = self.groups[0]["id"]
            if self.selected_group_id and not any(g["id"] == self.selected_group_id for g in self.groups):
                self.selected_group_id = self.groups[0]["id"] if self.groups else None
            self.render_groups()
            self.refresh_messages()
        except Exception as e:
            self.render_controlled_error("No se pudo cargar el chat.", e)

    def render_groups(self):
        cards = []
        for group in self.groups:
            selected = group["id"] == self.selected_group_id
            cards.append(
                ft.Container(
                    padding=16,
                    border_radius=22,
                    bgcolor=ft.Colors.with_opacity(0.12 if selected else 0.06, CHAMPAGNE if selected else ft.Colors.WHITE),
                    border=ft.border.all(1.2, ft.Colors.with_opacity(0.26 if selected else 0.10, CHAMPAGNE if selected else ft.Colors.WHITE)),
                    on_click=lambda e, gid=group["id"]: self.select_group(gid),
                    content=ft.Row(
                        [
                            self.group_avatar(group, CHAMPAGNE if selected else ACCENT_STRONG, size=44),
                            ft.Column(
                                [
                                    ft.Text(group.get("name", "Grupo"), size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(self.group_subtitle(group), size=12, color=TEXT_MUTED),
                                ],
                                spacing=3,
                                expand=True,
                            ),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
            )

        self.groups_slot.content = glass_panel(
            expand=True,
            padding=16,
            border_radius=24,
            accent=CHAMPAGNE,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Conversaciones", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            self.icon_action(ft.Icons.REFRESH_ROUNDED, "Refrescar", lambda e: self.refresh_all(), size=40),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.ListView(
                            controls=cards or [premium_empty_state("No hay conversaciones disponibles.", ft.Icons.FORUM_ROUNDED)],
                            spacing=10,
                            padding=ft.Padding(0, 4, 0, 4),
                            auto_scroll=False,
                        ),
                    ),
                ],
                spacing=12,
                expand=True,
            ),
        )
        self.safe_update()

    def select_group(self, group_id):
        self.selected_group_id = group_id
        self.render_groups()
        self.refresh_messages()

    def refresh_messages(self):
        try:
            if not self.selected_group_id:
                self.messages_slot.content = self.empty_chat()
                self.detail_slot.content = self.group_detail(None)
                self.safe_update()
                return
            messages = self.manager.get_messages(self.selected_group_id, self.user)
            self.current_members = self.manager.get_group_members(self.selected_group_id, self.user)
            self.current_can_manage = self.manager.can_manage_group(self.selected_group_id, self.user)
            self.messages_slot.content = self.messages_panel(messages)
            group = next((g for g in self.groups if g["id"] == self.selected_group_id), None)
            self.detail_slot.content = self.group_detail(group)
            self.safe_update()
        except Exception as e:
            self.render_controlled_error("No se pudieron cargar los mensajes.", e)

    def messages_panel(self, messages):
        bubbles = [self.message_bubble(m) for m in messages]
        group = next((g for g in self.groups if g["id"] == self.selected_group_id), None)
        return glass_panel(
            padding=16,
            border_radius=24,
            accent=ACCENT_STRONG,
            expand=True,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Mensajes", size=21, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Row(
                                [
                                    status_badge(f"{len(messages)} mensajes", "cyan"),
                                    self.icon_action(ft.Icons.CLEANING_SERVICES_ROUNDED, "Vaciar chat", self.confirm_clear_chat, size=40),
                                    status_badge("Modo supervision", "gold")
                                    if self.is_supervision_mode(group)
                                    else ft.Container(width=0, height=0),
                                ],
                                spacing=8,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(
                        expand=True,
                        border_radius=24,
                        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
                        padding=14,
                        content=ft.ListView(
                            controls=bubbles or [premium_empty_state("Aun no hay mensajes en esta conversacion.", ft.Icons.CHAT_BUBBLE_OUTLINE_ROUNDED)],
                            spacing=12,
                            auto_scroll=True,
                        ),
                    ),
                    ft.Container(
                        padding=ft.Padding(10, 8, 10, 8),
                        border_radius=22,
                        bgcolor=ft.Colors.with_opacity(0.055, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                        content=ft.Row(
                                [
                                    self.message_input,
                                    self.icon_action(ft.Icons.ATTACH_FILE_ROUNDED, "Adjuntar archivo", self.pick_file, size=46),
                                    self.icon_action(ft.Icons.ADD_REACTION_ROUNDED, "Emoji", self.toggle_emoji_panel, size=46),
                                    self.icon_action(ft.Icons.POLL_ROUNDED, "Encuesta", self.open_poll_dialog, size=46),
                                    self.icon_action(ft.Icons.SEND_ROUNDED, "Enviar mensaje", self.send_text, size=46, filled=True),
                                ],
                            spacing=8,
                            vertical_alignment=ft.CrossAxisAlignment.END,
                        ),
                    ),
                    self.emoji_panel(),
                ],
                spacing=12,
                expand=True,
            ),
        )

    def empty_chat(self):
        return glass_panel(
            padding=24,
            border_radius=28,
            accent=ACCENT_STRONG,
            content=premium_empty_state("Selecciona o crea un grupo para empezar.", ft.Icons.FORUM_ROUNDED),
        )

    def group_detail(self, group):
        if not group:
            return glass_panel(
                width=260,
                padding=22,
                border_radius=28,
                accent=CHAMPAGNE,
                content=ft.Text("Sin grupo seleccionado.", color=TEXT_MUTED),
            )
        return glass_panel(
            expand=True,
            padding=20,
            border_radius=24,
            accent=CHAMPAGNE,
            content=ft.Column(
                [
                    self.group_avatar(group, CHAMPAGNE, size=70),
                    ft.Text(group.get("name", "Grupo"), size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                    ft.Text(group.get("description") or "Grupo interno de empresa.", size=13, color=TEXT_MUTED),
                    ft.Divider(color=ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                    ft.Text("Estado de conversacion", size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.with_opacity(0.70, ft.Colors.WHITE)),
                    self.detail_line("Miembros", group.get("member_count", 0)),
                    self.detail_line("Tipo", "Chat directo" if group.get("is_direct") else "Grupo"),
                    self.detail_line("Creador", group.get("creator_name", "Sistema")),
                    self.detail_line("Actividad", group.get("last_message_at") or "Sin mensajes"),
                    ft.Divider(color=ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                    ft.Row(
                        [
                            ft.Text("Participantes", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Row(
                                [
                                    status_badge(str(len(self.current_members)), "cyan"),
                                    self.icon_action(ft.Icons.GROUP_ROUNDED, "Ver participantes", self.open_participants_dialog, size=36),
                                ],
                                spacing=8,
                                tight=True,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.ListView(
                            controls=[self.member_row(member) for member in self.current_members],
                            spacing=8,
                            padding=ft.Padding(0, 2, 0, 2),
                        ),
                    ),
                    ft.Container(
                        visible=self.current_can_manage,
                        content=ft.Column(
                            [
                                ft.Divider(color=ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                                ft.Text("Gestionar grupo", size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.with_opacity(0.70, ft.Colors.WHITE)),
                                secondary_button("Editar grupo", ft.Icons.EDIT_ROUNDED, on_click=self.open_edit_group_dialog),
                                secondary_button("Eliminar grupo", ft.Icons.DELETE_OUTLINE_ROUNDED, on_click=self.confirm_delete_group),
                            ],
                            spacing=8,
                        ),
                    ),
                ],
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def message_bubble(self, msg):
        if msg.get("message_type") == "poll":
            return self.poll_bubble(msg)
        mine = msg.get("sender_id") == self.user.get("id")
        color = CHAMPAGNE if mine else ACCENT_STRONG
        align = ft.MainAxisAlignment.END if mine else ft.MainAxisAlignment.START
        created = msg.get("created_at")
        time_text = created.strftime("%H:%M") if hasattr(created, "strftime") else str(created)[11:16]
        attachment = self.attachment_control(msg)
        can_delete = self.manager.can_delete_message(msg, self.user, self.selected_group_id)
        body = []
        if msg.get("message_text"):
            body.append(ft.Text(msg["message_text"], size=14, color=ft.Colors.WHITE))
        if attachment:
            body.append(attachment)
        return ft.Row(
            [
                ft.Container(
                    width=420,
                    padding=14,
                    border_radius=ft.border_radius.only(
                        top_left=20,
                        top_right=20,
                        bottom_left=20 if mine else 6,
                        bottom_right=6 if mine else 20,
                    ),
                    bgcolor=ft.Colors.with_opacity(0.13 if mine else 0.08, color),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.22, color)),
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(self.message_sender_name(msg), size=12, weight=ft.FontWeight.BOLD, color=color),
                                            ft.Text(msg.get("sender_name") or "", size=10, color=TEXT_MUTED, visible=bool(msg.get("sender_nickname"))),
                                        ],
                                        spacing=0,
                                        expand=True,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Text(time_text, size=11, color=ft.Colors.with_opacity(0.45, ft.Colors.WHITE)),
                                            self.icon_action(
                                                ft.Icons.DELETE_OUTLINE_ROUNDED,
                                                "Eliminar mensaje",
                                                lambda e, mid=msg.get("id"): self.confirm_delete_message(mid),
                                                size=30,
                                                visible=can_delete,
                                            ),
                                        ],
                                        spacing=4,
                                        tight=True,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            *body,
                        ],
                        spacing=6,
                    ),
                )
            ],
            alignment=align,
        )

    def attachment_control(self, msg):
        if not msg.get("file_path"):
            return None
        filename = msg.get("original_filename") or "archivo"
        mime = msg.get("mime_type") or ""
        if mime.startswith("image/"):
            return ft.Container(
                border_radius=16,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                border=ft.border.all(1, ft.Colors.with_opacity(0.16, ft.Colors.WHITE)),
                content=ft.Image(src=msg["file_path"], width=250, height=150, fit=ft.ImageFit.COVER),
            )
        return ft.Container(
            padding=12,
            border_radius=16,
            bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.INSERT_DRIVE_FILE_ROUNDED, color=CHAMPAGNE, size=22),
                    ft.Text(filename, size=12, color=ft.Colors.WHITE, expand=True),
                ],
                spacing=8,
            ),
        )

    def send_text(self, e=None):
        try:
            if not self.selected_group_id:
                self.show_message("Selecciona un grupo.", False)
                return
            ok, msg = self.manager.send_message(
                self.selected_group_id,
                self.user.get("id"),
                self.message_input.value,
                self.user,
            )
            self.show_message(msg, ok)
            if ok:
                self.message_input.value = ""
                self.refresh_all()
        except Exception as e:
            self.render_controlled_error("No se pudo enviar el mensaje.", e)

    def pick_file(self, e=None):
        if not self.selected_group_id:
            self.show_message("Selecciona un grupo antes de adjuntar.", False)
            return
        try:
            self.file_picker.pick_files(allow_multiple=False)
        except Exception as e:
            self.render_controlled_error("No se pudo abrir el selector de archivos.", e)

    def on_file_picked(self, e):
        try:
            if not e.files:
                return
            source = e.files[0].path
            ok, msg = self.manager.send_file_message(
                self.selected_group_id,
                self.user.get("id"),
                source,
                self.message_input.value,
                self.user,
            )
            self.show_message(msg, ok)
            if ok:
                self.message_input.value = ""
                self.refresh_all()
        except Exception as ex:
            self.render_controlled_error("No se pudo adjuntar el archivo.", ex)

    def open_group_dialog(self, e=None):
        try:
            users = self.manager.list_chat_users(self.user, mode="group")
        except Exception as e:
            self.render_controlled_error("No se pudieron cargar los participantes.", e)
            return
        name_input = premium_text_field(ft.TextField(label="Nombre del grupo", width=440))
        desc_input = premium_text_field(ft.TextField(label="Descripcion", width=440))
        checks = [
            ft.Checkbox(
                label=f"{u['nombre']} ({u['rol']})",
                value=u["id"] == self.user.get("id"),
                disabled=u["id"] == self.user.get("id"),
                data=u["id"],
            )
            for u in users
        ]
        checks_by_role = {}
        for c, u in zip(checks, users):
            checks_by_role.setdefault(u["rol"], []).append(c)

        def set_checks(predicate, value=True):
            for c, u in zip(checks, users):
                if c.disabled:
                    continue
                if predicate(u):
                    c.value = value
            try:
                self.page.update()
            except Exception:
                self.safe_update()

        quick_actions = ft.Row(
            [
                secondary_button("Empleados", ft.Icons.BADGE_ROUNDED, on_click=lambda ev: set_checks(lambda u: u["rol"] == "empleado")),
                secondary_button("Admins", ft.Icons.ADMIN_PANEL_SETTINGS_ROUNDED, on_click=lambda ev: set_checks(lambda u: u["rol"] == "administrador")),
                secondary_button("Clientes", ft.Icons.GROUP_ROUNDED, on_click=lambda ev: set_checks(lambda u: u["rol"] == "cliente")),
                secondary_button("Internos", ft.Icons.HUB_ROUNDED, on_click=lambda ev: set_checks(lambda u: u["rol"] in ["empleado", "administrador", "superusuario"])),
                secondary_button("Limpiar", ft.Icons.CLEAR_ROUNDED, on_click=lambda ev: set_checks(lambda u: True, False)),
            ],
            spacing=8,
            wrap=True,
        )

        def save_group(ev):
            try:
                members = [c.data for c in checks if c.value]
                avatar_path = (self._group_image_target or {}).get("path")
                ok, msg, group_id = self.manager.create_group(name_input.value, desc_input.value, self.user.get("id"), members, self.user, avatar_path)
                self.page.close(dialog)
                self.show_message(msg, ok)
                if ok:
                    self.selected_group_id = group_id
                    self.refresh_all()
            except Exception as e:
                self.page.close(dialog)
                self.render_controlled_error("No se pudo crear el grupo.", e)

        dialog = ft.AlertDialog(
            modal=True,
            bgcolor="#071421",
            title=ft.Text("Nuevo grupo interno", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=620,
                content=ft.Column(
                    [
                        name_input,
                        desc_input,
                        self.group_image_selector(),
                        ft.Text("Seleccion rapida", color=ft.Colors.with_opacity(0.70, ft.Colors.WHITE), size=13),
                        quick_actions,
                        ft.Text("Participantes", color=ft.Colors.with_opacity(0.70, ft.Colors.WHITE), size=13),
                        ft.Container(
                            height=260,
                            content=ft.Column(checks, spacing=4, scroll=ft.ScrollMode.AUTO),
                        ),
                    ],
                    spacing=12,
                    tight=True,
                ),
            ),
            actions=[
                secondary_button("Cancelar", ft.Icons.CLOSE_ROUNDED, on_click=lambda ev: self.page.close(dialog)),
                primary_button("Crear grupo", ft.Icons.CHECK_ROUNDED, on_click=save_group),
            ],
        )
        self.page.open(dialog)

    def open_edit_group_dialog(self, e=None):
        group = next((g for g in self.groups if g["id"] == self.selected_group_id), None)
        if not group:
            return
        name_input = premium_text_field(ft.TextField(label="Nombre del grupo", value=group.get("name") or "", width=460))
        desc_input = premium_text_field(ft.TextField(label="Descripcion", value=group.get("description") or "", width=460))
        image_selector = self.group_image_selector("Mantener foto actual" if group.get("avatar_path") else "Sin imagen seleccionada")

        def save(ev):
            avatar_path = (self._group_image_target or {}).get("path")
            ok, msg = self.manager.update_group(self.selected_group_id, name_input.value, desc_input.value, self.user, avatar_path)
            self.page.close(dialog)
            self.show_message(msg, ok)
            if ok:
                self.refresh_all()

        dialog = ft.AlertDialog(
            modal=True,
            bgcolor="#071421",
            title=ft.Text("Editar grupo", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=520,
                content=ft.Column([name_input, desc_input, image_selector], spacing=12, tight=True),
            ),
            actions=[
                secondary_button("Cancelar", ft.Icons.CLOSE_ROUNDED, on_click=lambda ev: self.page.close(dialog)),
                primary_button("Guardar", ft.Icons.CHECK_ROUNDED, on_click=save),
            ],
        )
        self.page.open(dialog)

    def toggle_emoji_panel(self, e=None):
        self.emoji_panel_visible = not self.emoji_panel_visible
        self.refresh_messages()

    def emoji_panel(self):
        emojis = ["😊", "👍", "❤️", "✅", "⚠️", "🙏"]
        return ft.Container(
            visible=self.emoji_panel_visible,
            padding=ft.Padding(12, 8, 12, 8),
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.075, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Container(
                        width=38,
                        height=38,
                        border_radius=14,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
                        on_click=lambda e, emoji=emoji: self.add_emoji(emoji),
                        ink=True,
                        content=ft.Text(emoji, size=18),
                    )
                    for emoji in emojis
                ],
                spacing=8,
                wrap=True,
            ),
        )

    def add_emoji(self, emoji):
        self.message_input.value = f"{self.message_input.value or ''}{emoji}"
        self.safe_update()

    def open_poll_dialog(self, e=None):
        if not self.selected_group_id:
            self.show_message("Selecciona una conversacion.", False)
            return
        question = premium_text_field(ft.TextField(label="Pregunta", width=520))
        option_fields = [premium_text_field(ft.TextField(label=f"Opcion {i}", width=520)) for i in range(1, 5)]

        def publish(ev):
            ok, msg = self.manager.create_poll(self.selected_group_id, self.user, question.value, [field.value for field in option_fields])
            self.page.close(dialog)
            self.show_message(msg, ok)
            if ok:
                self.refresh_all()

        dialog = ft.AlertDialog(
            modal=True,
            bgcolor="#071421",
            title=ft.Text("Nueva encuesta", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            content=ft.Container(width=560, content=ft.Column([question, *option_fields], spacing=10, tight=True)),
            actions=[
                secondary_button("Cancelar", ft.Icons.CLOSE_ROUNDED, on_click=lambda ev: self.page.close(dialog)),
                primary_button("Publicar", ft.Icons.CHECK_ROUNDED, on_click=publish),
            ],
        )
        self.page.open(dialog)

    def poll_bubble(self, msg):
        poll = self.manager.get_poll_summary(msg.get("poll_id"), self.user.get("id"))
        if not poll:
            return ft.Row([premium_empty_state("Encuesta no disponible.", ft.Icons.POLL_ROUNDED)])
        total = max(int(poll.get("total_votes") or 0), 1)
        voted = poll.get("my_option_id")
        option_controls = []
        for option in poll.get("options", []):
            votes = int(option.get("votes") or 0)
            pct = int((votes / total) * 100) if votes else 0
            selected = voted == option["id"]
            option_controls.append(
                ft.Container(
                    padding=ft.Padding(10, 8, 10, 8),
                    border_radius=16,
                    bgcolor=ft.Colors.with_opacity(0.10 if selected else 0.055, CHAMPAGNE if selected else ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.22 if selected else 0.10, CHAMPAGNE if selected else ft.Colors.WHITE)),
                    on_click=None if voted else lambda e, pid=poll["id"], oid=option["id"]: self.vote_poll(pid, oid),
                    ink=not bool(voted),
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(option["option_text"], size=13, color=ft.Colors.WHITE, expand=True),
                                    ft.Text(f"{votes} votos", size=11, color=TEXT_MUTED),
                                ],
                                spacing=8,
                            ),
                            ft.Container(
                                height=6,
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                                content=ft.Container(width=max(6, pct * 2.2), border_radius=999, bgcolor=CHAMPAGNE if selected else ACCENT_STRONG),
                            ),
                        ],
                        spacing=6,
                    ),
                )
            )
        return ft.Row(
            [
                ft.Container(
                    width=460,
                    padding=16,
                    border_radius=22,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.16, CHAMPAGNE)),
                    content=ft.Column(
                        [
                            ft.Row([ft.Icon(ft.Icons.POLL_ROUNDED, color=CHAMPAGNE, size=20), ft.Text("Encuesta", color=CHAMPAGNE, size=12, weight=ft.FontWeight.BOLD)], spacing=8),
                            ft.Text(poll["question"], size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            *option_controls,
                            ft.Text(f"{poll.get('total_votes', 0)} votos" + (" · ya votaste" if voted else ""), size=11, color=TEXT_MUTED),
                        ],
                        spacing=10,
                    ),
                )
            ],
            alignment=ft.MainAxisAlignment.START,
        )

    def vote_poll(self, poll_id, option_id):
        ok, msg = self.manager.vote_poll(poll_id, option_id, self.user)
        self.show_message(msg, ok)
        self.refresh_messages()

    def group_image_selector(self, label_text="Sin imagen seleccionada"):
        label = ft.Text(label_text, size=12, color=TEXT_MUTED, expand=True)
        self._group_image_target = {"path": None, "label": label}
        return ft.Container(
            padding=ft.Padding(12, 10, 12, 10),
            border_radius=16,
            bgcolor=ft.Colors.with_opacity(0.055, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.IMAGE_ROUNDED, color=CHAMPAGNE, size=20),
                    label,
                    self.icon_action(ft.Icons.UPLOAD_FILE_ROUNDED, "Elegir foto", lambda e: self.group_image_picker.pick_files(allow_multiple=False), size=38),
                ],
                spacing=10,
            ),
        )

    def on_group_image_picked(self, e):
        if not e.files or not self._group_image_target:
            return
        self._group_image_target["path"] = e.files[0].path
        label = self._group_image_target.get("label")
        if label:
            label.value = e.files[0].name
        try:
            self.page.update()
        except Exception:
            self.safe_update()

    def open_direct_dialog(self, e=None):
        try:
            users = [u for u in self.manager.list_chat_users(self.user, mode="direct") if u["id"] != self.user.get("id")]
        except Exception as e:
            self.render_controlled_error("No se pudieron cargar los usuarios.", e)
            return
        if not users:
            self.show_message("No hay usuarios disponibles para chat directo.", False)
            return

        options = [
            ft.dropdown.Option(
                key=str(u["id"]),
                text=f"{u['nombre']} - {u['email']} ({u['rol']})",
            )
            for u in users
        ]
        user_select = premium_dropdown(ft.Dropdown(label="Usuario", width=520, options=options))

        def create_direct(ev):
            try:
                if not user_select.value:
                    self.show_message("Selecciona un usuario.", False)
                    return
                ok, msg, group_id = self.manager.create_or_get_direct_chat(self.user, int(user_select.value))
                self.page.close(dialog)
                self.show_message(msg, ok)
                if ok:
                    self.selected_group_id = group_id
                    self.refresh_all()
            except Exception as e:
                self.page.close(dialog)
                self.render_controlled_error("No se pudo crear el chat directo.", e)

        dialog = ft.AlertDialog(
            modal=True,
            bgcolor="#071421",
            title=ft.Text("Nuevo chat", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=560,
                content=ft.Column(
                    [
                        ft.Text("Selecciona un usuario registrado para abrir una conversacion 1 a 1.", color=TEXT_MUTED, size=13),
                        user_select,
                    ],
                    spacing=12,
                    tight=True,
                ),
            ),
            actions=[
                secondary_button("Cancelar", ft.Icons.CLOSE_ROUNDED, on_click=lambda ev: self.page.close(dialog)),
                primary_button("Crear conversacion", ft.Icons.CHECK_ROUNDED, on_click=create_direct),
            ],
        )
        self.page.open(dialog)

    def member_row(self, member):
        is_owner = member.get("role_in_group") == "owner"
        can_remove = self.current_can_manage and member.get("user_id") != self.user.get("id")
        can_edit_nick = self.current_can_manage or member.get("user_id") == self.user.get("id")
        return ft.Container(
            padding=ft.Padding(12, 10, 12, 10),
            border_radius=16,
            bgcolor=ft.Colors.with_opacity(0.055, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    self.avatar(self.member_display_name(member), CHAMPAGNE if is_owner else ACCENT_STRONG, size=38),
                    ft.Column(
                        [
                            ft.Text(self.member_display_name(member), size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, no_wrap=True),
                            ft.Text(self.member_subtitle(member), size=11, color=TEXT_MUTED, no_wrap=True),
                        ],
                        spacing=1,
                        expand=True,
                    ),
                    self.icon_action(
                        ft.Icons.EDIT_ROUNDED,
                        "Editar mote",
                        lambda e, m=member: self.open_nickname_dialog(m),
                        size=34,
                        visible=can_edit_nick,
                    ),
                    self.icon_action(
                        ft.Icons.PERSON_REMOVE_ALT_1_ROUNDED,
                        "Eliminar participante",
                        lambda e, uid=member.get("user_id"), name=member.get("nombre"): self.confirm_remove_member(uid, name),
                        size=34,
                        visible=can_remove,
                    ),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def member_display_name(self, member):
        return (member.get("nickname") or member.get("nombre") or "Usuario").strip()

    def member_subtitle(self, member):
        role_map = {"owner": "Owner", "admin": "Admin", "member": "Miembro"}
        base = f"{role_map.get(member.get('role_in_group'), 'Miembro')} - {member.get('rol', '')}"
        if member.get("nickname"):
            return f"{base} - {member.get('nombre') or ''}"
        return base

    def message_sender_name(self, msg):
        return (msg.get("sender_nickname") or msg.get("sender_name") or "Usuario").strip()

    def open_participants_dialog(self, e=None):
        if not self.selected_group_id:
            return
        try:
            self.current_members = self.manager.get_group_members(self.selected_group_id, self.user)
            self.current_can_manage = self.manager.can_manage_group(self.selected_group_id, self.user)
            rows = [self.participant_dialog_row(member) for member in self.current_members]
            dialog = ft.AlertDialog(
                modal=True,
                bgcolor="#071421",
                title=ft.Text("Gestionar participantes", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                content=ft.Container(
                    width=680,
                    height=520,
                    content=ft.Column(
                        [
                            ft.Text("Participantes del grupo", size=13, color=TEXT_MUTED),
                            ft.Container(
                                expand=True,
                                content=ft.ListView(
                                    controls=rows or [premium_empty_state("No hay participantes.", ft.Icons.GROUP_ROUNDED)],
                                    spacing=10,
                                    padding=ft.Padding(0, 4, 0, 4),
                                ),
                            ),
                        ],
                        spacing=12,
                        expand=True,
                    ),
                ),
                actions=[secondary_button("Cerrar", ft.Icons.CLOSE_ROUNDED, on_click=lambda ev: self.page.close(dialog))],
            )
            self.page.open(dialog)
        except Exception as ex:
            self.render_controlled_error("No se pudieron abrir los participantes.", ex)

    def participant_dialog_row(self, member):
        is_owner = member.get("role_in_group") == "owner"
        can_remove = self.current_can_manage and member.get("user_id") != self.user.get("id")
        can_edit_nick = self.current_can_manage or member.get("user_id") == self.user.get("id")
        return ft.Container(
            padding=14,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    self.avatar(self.member_display_name(member), CHAMPAGNE if is_owner else ACCENT_STRONG, size=44),
                    ft.Column(
                        [
                            ft.Text(self.member_display_name(member), size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(member.get("nombre") or "", size=12, color=TEXT_MUTED, visible=bool(member.get("nickname"))),
                            ft.Text(member.get("email") or "", size=12, color=TEXT_MUTED),
                            ft.Row(
                                [
                                    status_badge(member.get("rol") or "usuario", "cyan"),
                                    status_badge(member.get("role_in_group") or "member", "gold" if is_owner else "cyan"),
                                ],
                                spacing=8,
                                wrap=True,
                            ),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                    self.icon_action(
                        ft.Icons.EDIT_ROUNDED,
                        "Editar mote",
                        lambda e, m=member: self.open_nickname_dialog(m),
                        size=38,
                        visible=can_edit_nick,
                    ),
                    self.icon_action(
                        ft.Icons.PERSON_REMOVE_ALT_1_ROUNDED,
                        "Eliminar participante",
                        lambda e, uid=member.get("user_id"), name=self.member_display_name(member): self.confirm_remove_member(uid, name),
                        size=38,
                        visible=can_remove,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def open_nickname_dialog(self, member):
        name = member.get("nombre") or "Usuario"
        nick_input = premium_text_field(
            ft.TextField(
                label="Mote en este grupo",
                value=member.get("nickname") or "",
                width=440,
            )
        )

        def save(ev):
            ok, msg = self.manager.update_member_nickname(self.selected_group_id, member.get("user_id"), nick_input.value, self.user)
            self.page.close(dialog)
            self.show_message(msg, ok)
            if ok:
                self.refresh_messages()

        dialog = ft.AlertDialog(
            modal=True,
            bgcolor="#071421",
            title=ft.Text("Editar mote", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=480,
                content=ft.Column(
                    [
                        ft.Text(name, color=TEXT_MUTED, size=13),
                        nick_input,
                    ],
                    spacing=12,
                    tight=True,
                ),
            ),
            actions=[
                secondary_button("Cancelar", ft.Icons.CLOSE_ROUNDED, on_click=lambda ev: self.page.close(dialog)),
                primary_button("Guardar", ft.Icons.CHECK_ROUNDED, on_click=save),
            ],
        )
        self.page.open(dialog)

    def is_supervision_mode(self, group):
        return bool(group and self.user.get("rol") == "superusuario" and not group.get("my_role"))

    def confirm_dialog(self, title, text, confirm_text, on_confirm, danger=False):
        accent = "#FFB4B8" if danger else CHAMPAGNE
        dialog = ft.AlertDialog(
            modal=True,
            bgcolor="#071421",
            title=ft.Text(title, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=430,
                padding=ft.Padding(0, 8, 0, 0),
                content=ft.Text(text, size=13, color=TEXT_MUTED),
            ),
            actions=[
                secondary_button("Cancelar", ft.Icons.CLOSE_ROUNDED, on_click=lambda e: self.page.close(dialog)),
                ft.Container(
                    height=46,
                    padding=ft.Padding(18, 0, 18, 0),
                    border_radius=16,
                    bgcolor=ft.Colors.with_opacity(0.12, accent),
                    border=ft.border.all(1.1, ft.Colors.with_opacity(0.26, accent)),
                    alignment=ft.alignment.center,
                    on_click=lambda e: on_confirm(dialog),
                    ink=True,
                    content=ft.Row(
                        [
                            ft.Icon(ft.Icons.CHECK_ROUNDED, color=accent, size=18),
                            ft.Text(confirm_text, color=accent, weight=ft.FontWeight.BOLD, size=13),
                        ],
                        spacing=8,
                        tight=True,
                    ),
                ),
            ],
        )
        self.page.open(dialog)

    def confirm_remove_member(self, user_id, name):
        self.confirm_dialog(
            "Eliminar participante",
            f"{name or 'Este usuario'} dejara de ver esta conversacion y no podra acceder a sus mensajes nuevos.",
            "Eliminar",
            lambda dialog: self.remove_member(dialog, user_id),
            danger=True,
        )

    def remove_member(self, dialog, user_id):
        self.page.close(dialog)
        ok, msg = self.manager.remove_member(self.selected_group_id, user_id, self.user)
        self.show_message(msg, ok)
        self.refresh_all()

    def confirm_delete_group(self, e=None):
        self.confirm_dialog(
            "Eliminar grupo",
            "Esta conversacion dejara de estar disponible para sus miembros. Los mensajes se conservan para auditoria.",
            "Eliminar grupo",
            self.delete_group,
            danger=True,
        )

    def delete_group(self, dialog):
        self.page.close(dialog)
        ok, msg = self.manager.delete_group(self.selected_group_id, self.user)
        self.show_message(msg, ok)
        if ok:
            self.selected_group_id = None
        self.refresh_all()

    def confirm_clear_chat(self, e=None):
        if not self.selected_group_id:
            return
        self.confirm_dialog(
            "Vaciar chat",
            "Solo se ocultaran los mensajes anteriores para tu usuario. Los mensajes nuevos volveran a aparecer.",
            "Vaciar chat",
            self.clear_chat,
        )

    def clear_chat(self, dialog):
        self.page.close(dialog)
        ok, msg = self.manager.clear_chat_for_user(self.selected_group_id, self.user)
        self.show_message(msg, ok)
        self.refresh_messages()

    def confirm_delete_message(self, message_id):
        self.confirm_dialog(
            "Eliminar mensaje",
            "El mensaje dejara de mostrarse en la conversacion. Los adjuntos no se eliminaran fisicamente.",
            "Eliminar",
            lambda dialog: self.delete_message(dialog, message_id),
            danger=True,
        )

    def delete_message(self, dialog, message_id):
        self.page.close(dialog)
        ok, msg = self.manager.delete_message(message_id, self.user)
        self.show_message(msg, ok)
        self.refresh_messages()

    def error_page(self, title, detail):
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
                    glass_panel(
                        width=760,
                        padding=28,
                        border_radius=30,
                        accent="#FFB4B8",
                        content=ft.Column(
                            [
                                status_badge("Mensajeria", "gold"),
                                ft.Icon(ft.Icons.ERROR_OUTLINE_ROUNDED, color="#FFB4B8", size=48),
                                ft.Text(title, size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                                ft.Text(str(detail), size=14, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
                                secondary_button("Volver al panel", ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda e: self.go(ruta_dashboard_por_rol())),
                            ],
                            spacing=14,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def render_controlled_error(self, title, error):
        detail = f"{type(error).__name__}: {error}"
        card = glass_panel(
            padding=24,
            border_radius=28,
            accent="#FFB4B8",
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.ERROR_OUTLINE_ROUNDED, color="#FFB4B8", size=34),
                    ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(detail, size=13, color=TEXT_MUTED),
                    secondary_button("Reintentar", ft.Icons.REFRESH_ROUNDED, on_click=lambda e: self.refresh_all()),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        if hasattr(self, "messages_slot"):
            self.messages_slot.content = card
            self.safe_update()
        else:
            self.controls = [self.error_page(title, detail)]
            self.safe_update()

    def avatar(self, text, color, size=44):
        initial = (text or "?").strip()[:1].upper()
        return ft.Container(
            width=size,
            height=size,
            border_radius=size / 2,
            bgcolor=ft.Colors.with_opacity(0.14, color),
            border=ft.border.all(1, ft.Colors.with_opacity(0.24, color)),
            alignment=ft.alignment.center,
            content=ft.Text(initial, size=max(14, int(size * 0.34)), weight=ft.FontWeight.BOLD, color=color),
        )

    def group_avatar(self, group, color, size=44):
        avatar_path = (group or {}).get("avatar_path")
        if avatar_path:
            return ft.Container(
                width=size,
                height=size,
                border_radius=size / 2,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                bgcolor=ft.Colors.with_opacity(0.12, color),
                border=ft.border.all(1, ft.Colors.with_opacity(0.24, color)),
                content=ft.Image(src=avatar_path, width=size, height=size, fit=ft.ImageFit.COVER),
            )
        return self.avatar((group or {}).get("name"), color, size=size)

    def icon_action(self, icon, tooltip, on_click, size=44, filled=False, visible=True):
        color = "#07111F" if filled else ft.Colors.WHITE
        bg = CHAMPAGNE if filled else ft.Colors.with_opacity(0.065, ft.Colors.WHITE)
        border_color = CHAMPAGNE if filled else ft.Colors.with_opacity(0.16, ft.Colors.WHITE)
        return ft.Container(
            width=size,
            height=size,
            visible=visible,
            border_radius=16,
            bgcolor=bg,
            border=ft.border.all(1.1, border_color),
            alignment=ft.alignment.center,
            tooltip=tooltip,
            on_click=on_click,
            ink=True,
            content=ft.Icon(icon, color=color, size=22),
        )

    def group_subtitle(self, group):
        kind = "Directo" if group.get("is_direct") else "Grupo"
        return f"{kind} - {group.get('member_count', 0)} miembros"

    def detail_line(self, label, value):
        return ft.Row(
            [
                ft.Text(label, size=12, color=ft.Colors.with_opacity(0.54, ft.Colors.WHITE), width=86),
                ft.Text(str(value), size=12, color=ft.Colors.WHITE, expand=True),
            ],
            spacing=8,
        )

    def safe_update(self):
        try:
            self.update()
        except Exception:
            try:
                self.page.update()
            except Exception:
                pass
