import flet as ft
from models.file_manager import FileManager

def SensoresPulsometroView(page: ft.Page, go):
    fm = FileManager()
    
    # Ejemplo rápido de cómo leerías los datos
    datos_pulsometro = fm.leer_lecturas_pulsometro()
    ultima_fc = datos_pulsometro["frecuencia_cardiaca"][-1]["valor"] if datos_pulsometro["frecuencia_cardiaca"] else "Sin datos"
    
    contenido = ft.Container(
        expand=True,
        padding=30,
        bgcolor="#050A12",
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(ft.Icons.ARROW_BACK, icon_color=ft.Colors.WHITE, on_click=lambda e: go("/panel_admin")),
                        ft.Text("Monitor de Pulsómetro", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Container(height=20),
                ft.Text(f"Última Frecuencia Cardíaca registrada: {ultima_fc} BPM", color=ft.Colors.WHITE70, size=18),
                # Aquí puedes expandir tu UI siguiendo el diseño de tus otras vistas
            ]
        )
    )

    return ft.View(
        route="/sensores_pulsometro",
        controls=[contenido],
        padding=0,
        bgcolor="#050A12"
    )