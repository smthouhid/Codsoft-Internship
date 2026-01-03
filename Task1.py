# To-Do List Task 1

tasks = []

def menu():
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def add():
    t = input("Enter task: ")
    tasks.append(t)
    print("Task added!")

def view():
    if not tasks:
        print("No tasks found.")
    else:
        for i, t in enumerate(tasks, 1):
            print(i, ".", t)

def update():
    view()
    try:
        n = int(input("Task number to update: "))
        if 1 <= n <= len(tasks):
            t = input("New task: ")
            tasks[n - 1] = t
            print("Task updated!")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

def delete():
    view()
    try:
        n = int(input("Task number to delete: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n - 1)
            print("Task deleted!")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

while True:
    menu()
    ch = input("Choose (1-5): ")

    if ch == '1':
        add()
    elif ch == '2':
        view()
    elif ch == '3':
        update()
    elif ch == '4':
        delete()
    elif ch == '5':
        print("Thank you!")
        break
    else:
        print("Wrong choice!")
