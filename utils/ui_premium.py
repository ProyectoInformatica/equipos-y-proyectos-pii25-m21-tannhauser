import flet as ft


BG_GRADIENT = ["#030712", "#06111D", "#0A1C2D", "#12385C"]
SURFACE = "#081421"
SURFACE_SOFT = "#0B1828"
TEXT_MUTED = ft.Colors.with_opacity(0.70, ft.Colors.WHITE)
ACCENT = "#C8F3FF"
ACCENT_STRONG = "#67E8F9"
CHAMPAGNE = "#E8D5A3"


def logo_mark(size=72):
    return ft.Container(
        width=size,
        height=size,
        border_radius=size / 2,
        padding=max(8, int(size * 0.12)),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        bgcolor=ft.Colors.with_opacity(0.94, ft.Colors.WHITE),
        border=ft.border.all(1.2, ft.Colors.with_opacity(0.34, ft.Colors.CYAN_100)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=22,
            color=ft.Colors.with_opacity(0.20, ft.Colors.CYAN_200),
            offset=ft.Offset(0, 10),
        ),
        content=ft.Image(src="logo_tannhauser.png", fit=ft.ImageFit.CONTAIN),
    )


def primary_button(text, icon=None, on_click=None, width=None, disabled=False, visible=True, data=None):
    return ft.ElevatedButton(
        text,
        icon=icon,
        width=width,
        height=48,
        bgcolor=ACCENT,
        color="#06111D",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=16),
            elevation=6,
            padding=ft.Padding(20, 0, 20, 0),
        ),
        on_click=on_click,
        disabled=disabled,
        visible=visible,
        data=data,
    )


def secondary_button(text, icon=None, on_click=None, width=None, disabled=False, visible=True, data=None):
    return ft.OutlinedButton(
        text,
        icon=icon,
        width=width,
        height=48,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
            shape=ft.RoundedRectangleBorder(radius=16),
            padding=ft.Padding(18, 0, 18, 0),
        ),
        on_click=on_click,
        disabled=disabled,
        visible=visible,
        data=data,
    )


def danger_button(text, icon=None, on_click=None, width=None, disabled=False, visible=True, data=None):
    return ft.OutlinedButton(
        text,
        icon=icon,
        width=width,
        height=46,
        style=ft.ButtonStyle(
            color="#FFB4B4",
            side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.RED_200)),
            shape=ft.RoundedRectangleBorder(radius=16),
            padding=ft.Padding(18, 0, 18, 0),
        ),
        on_click=on_click,
        disabled=disabled,
        visible=visible,
        data=data,
    )


def premium_text_field(control):
    control.border_radius = 16
    control.border_color = ft.Colors.with_opacity(0.22, ft.Colors.CYAN_100)
    control.focused_border_color = ACCENT_STRONG
    control.bgcolor = ft.Colors.with_opacity(0.055, ft.Colors.WHITE)
    control.color = ft.Colors.WHITE
    control.label_style = ft.TextStyle(color=ft.Colors.WHITE70)
    control.hint_style = ft.TextStyle(color=ft.Colors.WHITE38)
    return control


def premium_dropdown(control):
    control.border_radius = 16
    control.border_color = ft.Colors.with_opacity(0.22, ft.Colors.CYAN_100)
    control.focused_border_color = ACCENT_STRONG
    control.bgcolor = ft.Colors.with_opacity(0.055, ft.Colors.WHITE)
    control.color = ft.Colors.WHITE
    control.label_style = ft.TextStyle(color=ft.Colors.WHITE70)
    return control


def premium_section_title(title, subtitle=None, icon=None):
    controls = []
    if icon:
        controls.append(
            ft.Container(
                width=42,
                height=42,
                border_radius=14,
                bgcolor=ft.Colors.with_opacity(0.12, CHAMPAGNE),
                border=ft.border.all(1, ft.Colors.with_opacity(0.15, CHAMPAGNE)),
                alignment=ft.alignment.center,
                content=ft.Icon(icon, color=CHAMPAGNE, size=22),
            )
        )
    controls.append(
        ft.Column(
            [
                ft.Text(title, size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(subtitle, size=14, color=TEXT_MUTED) if subtitle else ft.Container(),
            ],
            spacing=4,
        )
    )
    return ft.Row(controls, spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER)


def premium_empty_state(text, icon=ft.Icons.INFO_OUTLINE_ROUNDED, width=None):
    return premium_card(
        width=width,
        padding=24,
        border_radius=22,
        content=ft.Column(
            [
                ft.Icon(icon, color=ft.Colors.WHITE54, size=38),
                ft.Text(text, size=15, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def status_badge(text, tone="neutral"):
    colors = {
        "gold": CHAMPAGNE,
        "cyan": ACCENT_STRONG,
        "green": "#B8FFE1",
        "neutral": ft.Colors.WHITE70,
    }
    color = colors.get(tone, colors["neutral"])
    return ft.Container(
        padding=ft.Padding(12, 7, 12, 7),
        border_radius=999,
        bgcolor=ft.Colors.with_opacity(0.10, color),
        border=ft.border.all(1, ft.Colors.with_opacity(0.18, color)),
        content=ft.Text(text, size=12, weight=ft.FontWeight.BOLD, color=color),
    )


def severity_style(severity="info"):
    sev = (severity or "info").lower()
    styles = {
        "critical": {
            "label": "Critica",
            "tone": "#FFB4B8",
            "accent": "#F87171",
            "icon": ft.Icons.PRIORITY_HIGH_ROUNDED,
        },
        "warning": {
            "label": "Atencion",
            "tone": CHAMPAGNE,
            "accent": "#F4C76B",
            "icon": ft.Icons.WARNING_AMBER_ROUNDED,
        },
        "info": {
            "label": "Informativa",
            "tone": ACCENT,
            "accent": ACCENT_STRONG,
            "icon": ft.Icons.NOTIFICATIONS_ACTIVE_ROUNDED,
        },
    }
    return styles.get(sev, styles["info"])


def glass_panel(content, width=None, padding=24, border_radius=26, expand=False, col=None, accent=None):
    accent = accent or CHAMPAGNE
    return ft.Container(
        col=col,
        width=width,
        expand=expand,
        padding=padding,
        border_radius=border_radius,
        bgcolor=ft.Colors.with_opacity(0.075, ft.Colors.WHITE),
        border=ft.border.all(1.1, ft.Colors.with_opacity(0.22, accent)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=30,
            color=ft.Colors.with_opacity(0.28, ft.Colors.BLACK),
            offset=ft.Offset(0, 16),
        ),
        animate_opacity=180,
        animate_scale=180,
        content=content,
    )


def severity_badge(severity="info", text=None):
    style = severity_style(severity)
    return ft.Container(
        padding=ft.Padding(12, 7, 12, 7),
        border_radius=999,
        bgcolor=ft.Colors.with_opacity(0.12, style["accent"]),
        border=ft.border.all(1, ft.Colors.with_opacity(0.24, style["tone"])),
        content=ft.Row(
            [
                ft.Icon(style["icon"], size=14, color=style["tone"]),
                ft.Text(text or style["label"], size=12, weight=ft.FontWeight.BOLD, color=style["tone"]),
            ],
            spacing=6,
            tight=True,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def premium_snackbar(message, ok=True, icon=None):
    color = "#B8FFE1" if ok else "#FFB4B8"
    return ft.SnackBar(
        bgcolor="#071421",
        elevation=12,
        duration=3600,
        content=ft.Container(
            padding=ft.Padding(4, 2, 4, 2),
            content=ft.Row(
                [
                    ft.Container(
                        width=34,
                        height=34,
                        border_radius=12,
                        bgcolor=ft.Colors.with_opacity(0.12, color),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.18, color)),
                        alignment=ft.alignment.center,
                        content=ft.Icon(icon or (ft.Icons.CHECK_ROUNDED if ok else ft.Icons.ERROR_OUTLINE_ROUNDED), color=color, size=18),
                    ),
                    ft.Text(message, size=13, color=ft.Colors.WHITE, expand=True),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )


def premium_card(content, width=None, padding=24, border_radius=26, expand=False, col=None):
    return ft.Container(
        col=col,
        width=width,
        expand=expand,
        padding=padding,
        border_radius=border_radius,
        bgcolor=SURFACE,
        border=ft.border.all(1.1, ft.Colors.with_opacity(0.15, ft.Colors.WHITE)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=28,
            color=ft.Colors.with_opacity(0.24, ft.Colors.BLACK),
            offset=ft.Offset(0, 14),
        ),
        animate_opacity=180,
        animate_scale=180,
        content=content,
    )


def premium_header(title, subtitle, name=None, actions=None):
    return premium_card(
        width=1180,
        padding=ft.Padding(28, 22, 28, 22),
        border_radius=28,
        content=ft.Row(
            [
                ft.Row(
                    [
                        logo_mark(76),
                        ft.Column(
                            [
                                status_badge("Tannhauser", "gold"),
                                ft.Text(title, size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Text(
                                    subtitle if name is None else f"{subtitle}, {name}",
                                    size=15,
                                    color=TEXT_MUTED,
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=18,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(actions or [], spacing=12),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def metric_card(icon, title, value, subtitle, tone="cyan", col=None):
    icon_color = CHAMPAGNE if tone == "gold" else ACCENT_STRONG
    return premium_card(
        col=col,
        padding=20,
        border_radius=24,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=48,
                            height=48,
                            border_radius=16,
                            bgcolor=ft.Colors.with_opacity(0.12, icon_color),
                            border=ft.border.all(1, ft.Colors.with_opacity(0.14, icon_color)),
                            alignment=ft.alignment.center,
                            content=ft.Icon(icon, color=icon_color, size=24),
                        ),
                        ft.Column(
                            [
                                ft.Text(title, size=13, color=ft.Colors.WHITE60),
                                ft.Text(str(value), size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ],
                            spacing=2,
                        ),
                    ],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Text(subtitle, size=13, color=TEXT_MUTED),
            ],
            spacing=13,
        ),
    )


def action_card(icon, title, text, button_text, on_click, col=None):
    return premium_card(
        col=col,
        width=320 if col is None else None,
        padding=24,
        border_radius=26,
        content=ft.Column(
            [
                ft.Container(
                    width=58,
                    height=58,
                    border_radius=18,
                    bgcolor=ft.Colors.with_opacity(0.12, ACCENT_STRONG),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.14, ACCENT_STRONG)),
                    alignment=ft.alignment.center,
                    content=ft.Icon(icon, size=29, color=ACCENT),
                ),
                ft.Text(title, size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(text, size=14, color=TEXT_MUTED),
                ft.Container(height=4),
                primary_button(button_text, ft.Icons.ARROW_FORWARD_ROUNDED, on_click=on_click),
            ],
            spacing=14,
        ),
    )


def premium_page(controls, padding=None, scroll=True):
    return ft.Container(
        expand=True,
        padding=padding or ft.Padding(34, 30, 34, 30),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=BG_GRADIENT,
        ),
        content=ft.Column(
            controls,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            scroll=ft.ScrollMode.AUTO if scroll else None,
        ),
    )
