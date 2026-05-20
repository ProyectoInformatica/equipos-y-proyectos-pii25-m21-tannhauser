import flet as ft
from controllers.chat_controller import ChatController
from models.session_manager import get_current_user

def ChatView(page: ft.Page, go):
    controller = ChatController()
    usuario_actual = get_current_user()
    contacto_seleccionado = None

    # Colores basados en tu imagen
    BG_COLOR = "#1e2a32"
    SIDEBAR_BG = "#111b21"
    CHAT_BG = "#0b141a"
    SENT_MSG_BG = "#005c4b"
    RCV_MSG_BG = "#202c33"
    TEXT_COLOR = ft.Colors.WHITE70

    # Contenedores principales
    chat_list_view = ft.ListView(expand=True, spacing=10)
    messages_view = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    msg_input = ft.TextField(
        hint_text="Escribe un mensaje...", 
        expand=True, 
        border_radius=20, 
        bgcolor=RCV_MSG_BG,
        color=TEXT_COLOR,
        border_color=ft.Colors.TRANSPARENT,
        on_submit=lambda e: enviar_click(e)
    )
    lbl_chat_header = ft.Text("Selecciona un contacto", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

    def cargar_contactos():
        chat_list_view.controls.clear()
        contactos = controller.obtener_contactos()
        for c in contactos:
            chat_list_view.controls.append(
                ft.ListTile(
                    leading=ft.CircleAvatar(content=ft.Icon(ft.Icons.PERSON), bgcolor=ft.Colors.BLUE_GREY),
                    title=ft.Text(c['nombre'], color=ft.Colors.WHITE),
                    subtitle=ft.Text(c['email'], color=TEXT_COLOR, size=12),
                    on_click=lambda e, cid=c['id'], cname=c['nombre']: seleccionar_contacto(cid, cname)
                )
            )
        page.update()

    def seleccionar_contacto(cid, cname):
        nonlocal contacto_seleccionado
        contacto_seleccionado = cid
        lbl_chat_header.value = f"Chat con {cname}"
        refrescar_mensajes()

    def refrescar_mensajes():
        if not contacto_seleccionado: return
        messages_view.controls.clear()
        mensajes = controller.cargar_historial(contacto_seleccionado)
        
        for m in mensajes:
            es_mio = (m['sender_id'] == usuario_actual['id'])
            messages_view.controls.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column([
                                ft.Text(m['message'], color=ft.Colors.WHITE),
                                ft.Text(m['hora'], size=10, color=ft.Colors.WHITE54, text_align=ft.TextAlign.RIGHT)
                            ], spacing=2),
                            bgcolor=SENT_MSG_BG if es_mio else RCV_MSG_BG,
                            padding=10,
                            border_radius=10,
                            margin=ft.margin.only(left=50 if es_mio else 0, right=0 if es_mio else 50)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END if es_mio else ft.MainAxisAlignment.START
                )
            )
        page.update()

    def enviar_click(e):
        if not contacto_seleccionado or not msg_input.value: return
        if controller.enviar_mensaje(contacto_seleccionado, msg_input.value):
            msg_input.value = ""
            refrescar_mensajes()
            msg_input.focus()

    # Layout de la vista
    sidebar = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.IconButton(ft.Icons.ARROW_BACK, icon_color=TEXT_COLOR, on_click=lambda e: go(f"/panel_{usuario_actual.get('rol', 'usuario')}")),
                    ft.Text("Tannhäuserchat", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                ]),
                padding=10
            ),
            ft.Divider(color=TEXT_COLOR),
            chat_list_view
        ]),
        width=300,
        bgcolor=SIDEBAR_BG,
        padding=10
    )

    chat_area = ft.Container(
        content=ft.Column([
            # Header del chat
            ft.Container(
                content=ft.Row([
                    ft.CircleAvatar(icon=ft.Icons.PERSON, bgcolor=ft.Colors.BLUE_GREY),
                    lbl_chat_header,
                    ft.Container(expand=True),
                    ft.IconButton(ft.Icons.REFRESH, icon_color=TEXT_COLOR, on_click=lambda e: refrescar_mensajes(), tooltip="Refrescar mensajes")
                ]),
                padding=15,
                bgcolor=SIDEBAR_BG
            ),
            # Área de mensajes
            ft.Container(
                content=messages_view,
                expand=True,
                padding=20,
                image_src="https://user-images.githubusercontent.com/15075759/28719144-86dc0f70-73b1-11e7-911d-60d70fcded21.png", # Fondo estilo WhatsApp oscuro
                image_fit=ft.ImageFit.COVER,
                image_opacity=0.1
            ),
            # Input de texto
            ft.Container(
                content=ft.Row([
                    ft.IconButton(ft.Icons.ADD, icon_color=TEXT_COLOR),
                    msg_input,
                    ft.IconButton(ft.Icons.SEND, icon_color=TEXT_COLOR, on_click=enviar_click)
                ]),
                padding=10,
                bgcolor=SIDEBAR_BG
            )
        ]),
        expand=True,
        bgcolor=CHAT_BG
    )

    main_layout = ft.Row([sidebar, chat_area], expand=True, spacing=0)
    
    # Cargar contactos al iniciar la vista
    cargar_contactos()

    return ft.View(
        route="/chat",
        controls=[main_layout],
        padding=0,
        bgcolor=BG_COLOR
    )