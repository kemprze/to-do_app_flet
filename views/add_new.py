import flet as ft
from flet_route import Params, Basket
from globals import list_view
from globals import todo_list
from globals import SaveListItems
import csv
import os

def AddNewTask(page: ft.Page, params: Params, basket: Basket):
    content = ft.Container()
    page.add(content) 


    def AddTask():
        new_tile = ft.ListTile(
            title = ft.Text(task_name.value),
            subtitle = ft.Text(description.value),
            trailing = ft.CupertinoCheckbox(value = False)
            )
        
        list_view.controls.append(new_tile)
        todo_list[len(todo_list)+1] = [task_name, description]
        
        print(f"Appended item: {task_name.value}")
        SaveListItems()
        page.go("/")

    task_name = ft.TextField(label = "Task name")
    description = ft.TextField(label = "Description")
    task_icon = ft.IconButton(icon = ft.icons.EDIT) # TODO -- to implement

    app_bar = ft.AppBar(
                title = ft.Text("Add a new task", size = 15),
                center_title = True,
                bgcolor = ft.colors.BLUE
                )

    column = ft.Column(
        controls = [
            ft.Row(
                controls = [
                    task_icon, task_name
                    ]
                ),

            description
            ]    
        )   
    
    bottom_app_bar = ft.BottomAppBar(
            bgcolor = ft.colors.BLUE,
            shape = ft.NotchShape.CIRCULAR,
            content = ft.Row(
                controls = [ft.Container(expand = True),
                    ft.FloatingActionButton(
                    icon = ft.icons.EDIT_OUTLINED,
                    opacity = 0.5,
                    on_click  = lambda _: AddTask()
                    )
                ]
            )
        )
    
    controls = [
        app_bar,
        column,
        bottom_app_bar
    ]

    page.update()
    
    return ft.View(
        "/add_new",
        controls)