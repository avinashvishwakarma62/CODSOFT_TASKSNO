tasks = []

def add_task():
    task = input("Enter your task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append({"task": task, "status": "Pending"})
        print("Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]['task']} - {tasks[i]['status']}")


def update_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to update: "))

        if number >= 1 and number <= len(tasks):
            new_task = input("Enter new task: ")

            if new_task.strip() != "":
                tasks[number - 1]["task"] = new_task
                print("Task updated successfully.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number >= 1 and number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if number >= 1 and number <= len(tasks):
            tasks[number - 1]["status"] = "Completed"
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


while True:

    print("\n==============================")
    print("        TO-DO LIST")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Complete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")