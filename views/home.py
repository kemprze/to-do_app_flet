import flet as ft
from flet_route import Params, Basket
from globals import todo_list
from globals import initialized
from globals import list_view
from globals import SaveListItems

def Home(page: ft.Page, params: Params, basket: Basket):
    global todo_list
    global initialized
    
    content = ft.Container()
    page.add(content) 

    app_bar = ft.AppBar(
        ft.IconButton(
            icon = ft.icons.MENU_ROUNDED,
                opacity = 0.5,
                on_click = lambda x: page.go("/settings/")
                ),
        title = ft.Text("Let's plan the day!", size = 15),
        center_title = False,
        bgcolor = ft.colors.BLUE
        )

    bottom_app_bar = ft.BottomAppBar(
        bgcolor = ft.colors.BLUE,
        shape = ft.NotchShape.CIRCULAR,
        content = ft.Row(
            controls = [ft.Container(expand = True),
                ft.FloatingActionButton(
                    icon = ft.icons.EDIT_OUTLINED,
                    opacity = 0.5,
                    on_click  = lambda _: page.go("/add_new/")
                )
            ]
        )
    )
    
    list_view_titles = [control.title.value for control in list_view.controls if isinstance(control, ft.ListTile)]
    
    controls = [
        app_bar,
        list_view,
        bottom_app_bar
        ]
    
    def RemoveItemFromListView(key, todo_list, list_view):
        for control in list_view.controls:
            if isinstance(control, ft.ListTile):
                if control.title.value == todo_list[key][0]:
                    list_view.controls.remove(control)
                    page.update()
                    SaveListItems()
                    break

    def CreateListTile(key, value, list_view):
        new_tile = ft.ListTile(
            title = ft.Text(value[0]),
            subtitle = ft.Text(value[1]),
            trailing = ft.Container(content = ft.Row(
            controls = [
                ft.IconButton(
                    icon = ft.icons.DELETE_FOREVER_OUTLINED,
                    on_click = lambda _: RemoveItemFromListView(key, todo_list, list_view)),
                ft.CupertinoCheckbox(
                    value = False,
                    on_change = lambda _: print('Crossed out'))],
                    spacing = 8
                ), 
            width = 100,
            alignment = ft.alignment.center_right
            ))

        return new_tile
        
    def AppendListItemsIntoListView(todo_list, list_view, list_view_titles):
        for key in todo_list:
            value = todo_list[key]
            if value[0] in list_view_titles:
                print(f'Item {value[0]} already in the list. Skipping.')
                pass
            
            else:
                list_view.controls.append(CreateListTile(key, value, list_view))
    
    AppendListItemsIntoListView(todo_list, list_view, list_view_titles)

    page.update()

    return ft.View("/", controls)
