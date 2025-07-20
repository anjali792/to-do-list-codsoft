todo_list = []

def show_menu():
    print("\n To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print(" No tasks in the list.")
    else:
        print("\n Your Tasks:")
        for idx, task in enumerate(todo_list, start=1):
            status = " Done" if task['done'] else "❌ Not Done"
            print(f"{idx}. {task['task']} [{status}]")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({'task': task, 'done': False})
    print(" Task added.")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]['done'] = True
            print(" Task marked as done.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f" Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print(" Exiting. Have a productive day!")
        break
    else:
        print("Invalid choice. Please try again.")
