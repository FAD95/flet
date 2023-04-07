import flet as ft
import time

def main(page: ft.Page):
    # t = ft.Text(value="Hello, world!", color="red")
    # page.controls.append(t)
    # page.update()
    t = ft.Text(color="red")
    # page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )
ft.app(target=main)