import flet as ft

def ListView():
    # Lista para almacenar los contenedores creados
    containers = []

    # Función para crear un contenedor con el valor ingresado
    def create_container(value: str):
        return ft.Container(
            content=ft.Text(value),
            alignment=ft.alignment.center,
            width=50,
            height=50,
            border_radius=50,
            bgcolor=ft.colors.WHITE,  # Color de fondo por defecto
            border=ft.border.all(1, color=ft.Colors.BLACK),
        )

    # Función que se ejecuta al presionar "Agregar"
    def buttonAdd_click(e):
        if text_field.value:  # Se agrega solo si el campo no está vacío
            new_container = create_container(text_field.value)
            containers.append(new_container)
            list_view.controls = containers
            text_field.value = ""
            e.control.page.update()

    # Función que elimina el último contenedor agregado
    def buttonDelete_click(e):
        if containers:
            containers.pop()
            list_view.controls = containers
            e.control.page.update()

    # Función que ordena los contenedores según su valor (numérico si es posible, o alfabéticamente)
    def buttonSort_click(e):
        try:
            containers.sort(key=lambda c: int(c.content.value))
        except Exception:
            containers.sort(key=lambda c: c.content.value.lower())
        list_view.controls = containers
        e.control.page.update()

    # Función que busca y resalta (cambiando el color) los contenedores cuyo valor coincida con el buscado
    def buttonSearch_click(e):
        search_value = text_field.value.strip().lower()
        for container in containers:
            # Si coincide el valor, se resalta en amarillo, de lo contrario se restaura el color azul
            if container.content.value.lower() == search_value:
                container.bgcolor = ft.colors.GREEN
            else:
                container.bgcolor = ft.colors.WHITE
        e.control.page.update()

    # Función que limpia (elimina) todos los contenedores de la lista
    def buttonClear_click(e):
        containers.clear()
        list_view.controls = containers
        e.control.page.update()

    # Componentes de la interfaz
    title = ft.Markdown("# Lista")
    description = ft.Markdown("Aquí vamos a aprender cómo funcionan las **Listas**")
    text_field = ft.TextField(label="Número o Texto")

    # Fila que mostrará los contenedores; se utiliza wrap=True para que se acomoden en varias líneas
    list_view = ft.Row(controls=containers, wrap=True)

    # Botones con sus respectivas funciones
    buttonAdd = ft.ElevatedButton("Agregar", on_click=buttonAdd_click)
    buttonDelete = ft.ElevatedButton("Eliminar", on_click=buttonDelete_click)
    buttonSort = ft.ElevatedButton("Ordenar", on_click=buttonSort_click)
    buttonSearch = ft.ElevatedButton("Buscar", on_click=buttonSearch_click)
    buttonClear = ft.ElevatedButton("Limpiar", on_click=buttonClear_click)
    methods = ft.Row([buttonAdd, buttonDelete, buttonSort, buttonSearch, buttonClear])

    # Se retorna la estructura principal en una columna
    return ft.Column([title, description, text_field, methods, list_view])

def main(page: ft.Page):
    page.add(ListView())

if __name__ == "__main__":
    ft.app(target=main)
