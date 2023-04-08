import flet as ft
import time

def main(page: ft.Page):
    # t = ft.Text(value="Hello, world!", color="red")
    # page.controls.append(t)
    # page.update()
    t = ft.Text(color="red")
    # page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 2:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)
ft.app(target=main)