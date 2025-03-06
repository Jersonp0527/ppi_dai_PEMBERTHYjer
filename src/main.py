import flet as ft
from explore import explore_view  # Importa la vista de "Explorar"
from saved import saved_view      # Importa la vista de "Guardados"
from settings import settings_view # Importa la vista de "Configuraciones"

def main(page: ft.Page):
    """Agrupa los elementos del proyecto y configura la barra de navegación."""
    # Contenedor para el contenido dinámico (por defecto, la vista "Explorar")
    content = ft.Column([explore_view(page)])

    def on_nav_change(e):
        """Cambia el contenido de la vista según la pestaña seleccionada."""
        if page.navigation_bar.selected_index == 0:
            content.controls = [saved_view()]
        elif page.navigation_bar.selected_index == 1:
            content.controls = [explore_view(page)]
        elif page.navigation_bar.selected_index == 2:
            content.controls = [settings_view()]
        page.update()

    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        selected_index=1,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK, label="Guardados"),
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Configuraciones"),
        ]
    )

    page.add(content)

if __name__ == "__main__":
    ft.app(main)
