import sys 
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE,'r') as file:
                return json.load(file)
        else:
            return []
    except Exception as e:
        print(f'Error loading tasks due to {e}')
        return []

def save_tasks(tasks):
    try:
        with open(TASKS_FILE,'w') as file:
            json.dump(tasks,file,indent=2)
        return True
    except Exception as e:
        print(f"Saving Error {e}")
        return False

def add_task(description):
    tasks = load_tasks()
    new_task = {
        'id':len(tasks)+1,
        'description': description,
        'status':'todo',
        'createAt':datetime.now().isoformat(),
        'updatedAt':datetime.now().isoformat()
    }
    tasks.append(new_task)
    if save_tasks(tasks):
        print(f"Task added successfully (ID: {new_task['id']})")
    else:
        print("Failed to add task")

def list_tasks(search_filter = None):
    tasks = load_tasks()

    if search_filter:
        tasks = [task for task in tasks if task['status'] == search_filter]
    if not tasks:
        print("No tasks found")
        return
    
    print("\nYour tasks.")
    print("-"*50)
    for task in tasks:
        status_display = {
            'todo': 'To Do',
            'in-progress': 'In Progress',
            'done': 'Done'
        }.get(task['status'],task['status'])
        print(f"ID: {task['id']} | {task['description']} | Status: {status_display}")
    print("-"*50)

def mark_task(task_id,new_status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = datetime.now().isoformat()
            if save_tasks(tasks):
                status_name = {
                    "todo": "To Do",
                    "in-progress": "In Progress",
                    "done": "Done"         
                }.get(new_status,new_status)
                print(f"Task {task_id} marked as {status_name}")
            else:
                print('Failed to update task')
            return
    print(f"Task with ID {task_id} Not Found")
    
def mark_in_progress(task_id):
    mark_task(task_id,"in-progress")

def mark_done(task_id):
    mark_task(task_id,"done")

def update_task(task_id,new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            if save_tasks(tasks):
                print(f"Task {task_id} updated sucessfully")
            else:
                print("Failed to update task")
            return
    print(f"Task with ID {task_id} is Not Found")

def delete_task(task_id):
    tasks = load_tasks()

    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted_task = tasks.pop(i)
            if save_tasks(tasks):
                print(f"Task {task_id} deleted successfully")
            else:
                print("Failed to delete task")
            return
    print(f"Task with ID {task_id} Not Found")

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python task-cli.py [command] [arguments]")
        print("Commands: add, update, delete, mark-in-progress, mark-done, list")
        return
    command = sys.argv[1]
    try:
        if command == 'add':
            if len(sys.argv) < 3:
                print("Error: Please provide a task description")
                return
            description = sys.argv[2]
            add_task(description)
        elif command == 'update':
            if len(sys.argv) < 4:
                print("Error: Please provide task ID and new description")
                return 
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            update_task(task_id, new_description)
        elif command == 'delete':
            if len(sys.argv) < 3:
                print("Error: Please provide task ID")
                return
            task_id = int(sys.argv[2])
            delete_task(task_id)
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Please provide task Id")
                return
            task_id = int(sys.argv[2])
            mark_in_progress(task_id)
        elif command == 'mark-done':
            if len(sys.argv) < 3:
                print("Error: Please provide task ID")
                return
            task_id = int(sys.argv[2])
            mark_done(task_id)
        elif command == 'list':
            if len(sys.argv) > 2:
                status_filter = sys.argv[2]
                if status_filter not in ['todo','in-progress','done']:
                    print("Error: Status must be 'todo' , 'in-progress', or 'done'")
                    return
                list_tasks(status_filter)
            else:
                list_tasks()
        else:
            print(f"Unknown command: {command}")

    except ValueError:
        print("Error: task ID must be a number")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
