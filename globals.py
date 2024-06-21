import flet as ft
from flet_route import Routing, path
from flet_route import Params, Basket
import os
import csv

todo_list = {}
initialized = False
list_view = ft.ListView(
        spacing = 10,
        padding = 20,
        height = 300,
        expand = True
        )

def SaveListItems():
    def GetSaveFilePath():
        script_dir = os.path.dirname(__file__)
        return os.path.join(script_dir, 'Save.csv')
    
    def WriteListItems():
        file_path = GetSaveFilePath()
        with open(file_path, 'w', newline = '') as save:
             fieldnames = ['task_name', 'description']
             writer = csv.DictWriter(save, fieldnames = fieldnames)
             writer.writeheader()
             for control in list_view.controls:
                writer.writerow({'task_name': control.title.value, 'description': control.subtitle.value})
                print(f'Task {control.title.value} with a description {control.subtitle.value} written to the file.')
    WriteListItems()