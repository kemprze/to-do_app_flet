import flet as ft
from flet_route import Routing, path
from views.home import Home
from views.settings import Settings
from views.add_new import AddNewTask
from flet_route import Params, Basket
from globals import todo_list
from globals import initialized
from globals import SaveListItems
import csv
import os

def GetSaveFilePath():
        script_dir = os.path.dirname(__file__)
        return os.path.join(script_dir, 'Save.csv')
    
def initialize_app():
    def AccessSaveFile():
    # Checking for the save file
    # TODO -- consider different file formats
        file_path = GetSaveFilePath()

        if not os.path.exists(file_path):
            print("Save file not found, initializing a new one...")
            with open(file_path, 'w', newline='') as save:
                fieldnames = ['task_name', 'description']
                writer = csv.DictWriter(save, fieldnames=fieldnames)
                writer.writeheader()
            return open(file_path, 'r')
            
        else:
            save = open(file_path, 'r')
            print("Save file accessed successfully")
            return save
            
            # If not found, creating a new file

    def LoadListItems():
        save = AccessSaveFile()
        global todo_list
        reader = csv.DictReader(save)
        headers = reader.fieldnames
        if headers and 'task_name' in headers:
            print('Headers found!')
            for row in reader:
                task_name = row['task_name']
                description = row['description']
                if task_name not in todo_list:
                    todo_list[len(todo_list)+1] = [task_name, description]
                    
        else:
            print("No valid headers found in the file...")
            
        save.close()
        print(f"Loaded dictionary items: {todo_list}")
        return todo_list
        
    return LoadListItems()
    
def main(page: ft.Page):
    global todo_list
    global initialized
    
    # Define app routes with todo_list passed to Home view
    app_routes = [
        # Route for Home screen
        path(url="/", view = Home, clear = True),

        # Route for AddNewTask screen
        path(url="/add_new", view = AddNewTask, clear=True),

        # Route for Settings screen
        path(url="/settings", view = Settings, clear=True)
    ]

    # Setup routing with app_routes
    Routing(page = page, app_routes = app_routes)

    # Navigate to the current route
    page.go(page.route)

if __name__ == '__main__':
    initialize_app()
    initialized = True
    ft.app(target = main)