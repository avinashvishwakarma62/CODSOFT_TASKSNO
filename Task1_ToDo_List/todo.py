import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

tasks = []


def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    tasks.append([task, "Pending"])
    task_entry.delete(0, tk.END)
    show_tasks()


def show_tasks():
    task_list.delete(*task_list.get_children())

    for i, task in enumerate(tasks):
        task_list.insert(
            "",
            tk.END,
            iid=i,
            values=(task[0], task[1])
        )


def update_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first.")
        return

    index = int(selected[0])
    new_task = task_entry.get().strip()

    if new_task == "":
        messagebox.showwarning("Warning", "Enter the new task.")
        return

    tasks[index][0] = new_task
    task_entry.delete(0, tk.END)
    show_tasks()


def complete_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first.")
        return

    index = int(selected[0])
    tasks[index][1] = "Completed"
    show_tasks()


def delete_task():
    selected = task_list.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first.")
        return

    index = int(selected[0])
    tasks.pop(index)
    show_tasks()


def select_task(event):
    selected = task_list.selection()

    if selected:
        index = int(selected[0])
        task_entry.delete(0, tk.END)
        task_entry.insert(0, tasks[index][0])


root = tk.Tk()
root.title("My To-Do List")
root.geometry("700x500")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

title = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

task_entry = ttk.Entry(root, width=55, font=("Arial", 12))
task_entry.pack(pady=10)

add_button = ttk.Button(
    root,
    text="+ Add Task",
    command=add_task
)
add_button.pack(pady=5)

task_list = ttk.Treeview(
    root,
    columns=("Task", "Status"),
    show="headings",
    height=12
)

task_list.heading("Task", text="Task")
task_list.heading("Status", text="Status")

task_list.column("Task", width=470)
task_list.column("Status", width=150)

task_list.pack(pady=15)

task_list.bind("<<TreeviewSelect>>", select_task)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(
    button_frame,
    text="Update",
    command=update_task
).grid(row=0, column=0, padx=5)

ttk.Button(
    button_frame,
    text="Complete",
    command=complete_task
).grid(row=0, column=1, padx=5)

ttk.Button(
    button_frame,
    text="Delete",
    command=delete_task
).grid(row=0, column=2, padx=5)

root.mainloop()