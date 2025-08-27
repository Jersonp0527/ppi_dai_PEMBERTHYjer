import flet as ft
import os

def explore_view(page):
    """Retorna el contenido de la vista "Explorar", que contiene una lista de estructuras."""
    # Se usa theme_style con el valor "headline1"
    title = ft.Text("Explorar")
    return ft.Column([title, explore_list(page)])

def explore_list(page):
    """Lee la carpeta 'src/structures' y retorna una lista con las estructuras de datos."""
    path = "src/structures"
    files = os.listdir(path)
    files = [f for f in files if f.endswith(".py")]
    items = []
    for file in files:
        item = ft.ListTile(
            title=ft.Text(file.split(".")[0]),
            on_click=lambda e, file=file: explore_structure(page, file),
        )
        items.append(item)
    return ft.ListView(controls=items)

def explore_structure(page, file):
    """Maneja la exploración de una estructura de datos, importando el módulo y actualizando la vista."""
    structure = __import__(f"structures.{file.split('.')[0]}", fromlist=[""])
    view = structure.ListView()
    back_button = ft.ElevatedButton("Regresar", on_click=lambda e: back_to_explore(page))
    new_view = ft.Column([back_button, view])
    page.controls = [new_view]
    page.update()

def back_to_explore(page):
    page.controls = [explore_view(page)]
    page.update()

def main(page: ft.Page):
    page.add(explore_view(page))

if __name__ == "__main__":
    ft.app(main)
