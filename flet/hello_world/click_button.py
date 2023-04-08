import flet as ft
import time

def main(page: ft.Page):
    # t = ft.Text(value="Hello, world!", color="red")
    # page.controls.append(t)
    # page.update()
    t = ft.Text(color="red")
    # page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    def button_clicked(e):
        page.add(ft.Text("Hi Fad! You clicked!", color="green"))

    page.add(ft.ElevatedButton(text="Hi Fad!", on_click=button_clicked))
ft.app(target=main)