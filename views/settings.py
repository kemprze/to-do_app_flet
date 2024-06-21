import flet as ft
from flet_route import Params, Basket

def Settings(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/add_new",

        controls = [
            ft.Text("This is a future Settings view"),
            ft.ElevatedButton("Cancel", on_click = lambda _: page.go("/"))
        ]
    )