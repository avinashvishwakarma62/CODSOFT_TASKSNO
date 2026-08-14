import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

contacts = []


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Warning",
            "Name and phone number are required."
        )
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    clear_fields()
    show_contacts()

    messagebox.showinfo(
        "Success",
        "Contact added successfully."
    )


def show_contacts():
    contact_list.delete(*contact_list.get_children())

    for i, contact in enumerate(contacts):
        contact_list.insert(
            "",
            tk.END,
            iid=i,
            values=(
                contact["name"],
                contact["phone"],
                contact["email"],
                contact["address"]
            )
        )


def select_contact(event):
    selected = contact_list.selection()

    if selected:
        index = int(selected[0])
        contact = contacts[index]

        clear_fields()

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])


def update_contact():
    selected = contact_list.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact first."
        )
        return

    index = int(selected[0])

    contacts[index]["name"] = name_entry.get()
    contacts[index]["phone"] = phone_entry.get()
    contacts[index]["email"] = email_entry.get()
    contacts[index]["address"] = address_entry.get()

    show_contacts()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "Contact updated successfully."
    )


def delete_contact():
    selected = contact_list.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact first."
        )
        return

    index = int(selected[0])

    contacts.pop(index)

    show_contacts()
    clear_fields()


def search_contact():
    search = search_entry.get().lower().strip()

    contact_list.delete(*contact_list.get_children())

    for i, contact in enumerate(contacts):
        if (
            search in contact["name"].lower()
            or search in contact["phone"]
        ):
            contact_list.insert(
                "",
                tk.END,
                iid=i,
                values=(
                    contact["name"],
                    contact["phone"],
                    contact["email"],
                    contact["address"]
                )
            )


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Book")
root.geometry("900x600")
root.resizable(False, False)

title = tk.Label(
    root,
    text="CONTACT BOOK",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)

form_frame = tk.Frame(root)
form_frame.pack(pady=5)

tk.Label(form_frame, text="Name").grid(
    row=0, column=0, padx=5, pady=5
)

name_entry = tk.Entry(form_frame, width=22)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(form_frame, text="Phone").grid(
    row=0, column=2, padx=5
)

phone_entry = tk.Entry(form_frame, width=22)
phone_entry.grid(row=0, column=3, padx=5)

tk.Label(form_frame, text="Email").grid(
    row=1, column=0, padx=5, pady=5
)

email_entry = tk.Entry(form_frame, width=22)
email_entry.grid(row=1, column=1, padx=5)

tk.Label(form_frame, text="Address").grid(
    row=1, column=2, padx=5
)

address_entry = tk.Entry(form_frame, width=22)
address_entry.grid(row=1, column=3, padx=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Contact",
    width=15,
    command=add_contact
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update",
    width=15,
    command=update_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    width=15,
    command=delete_contact
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_fields
).grid(row=0, column=3, padx=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(
    search_frame,
    text="Search:"
).pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(
    search_frame,
    width=30
)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_contact
).pack(side=tk.LEFT)

contact_list = ttk.Treeview(
    root,
    columns=("Name", "Phone", "Email", "Address"),
    show="headings",
    height=12
)

contact_list.heading("Name", text="Name")
contact_list.heading("Phone", text="Phone")
contact_list.heading("Email", text="Email")
contact_list.heading("Address", text="Address")

contact_list.column("Name", width=160)
contact_list.column("Phone", width=150)
contact_list.column("Email", width=220)
contact_list.column("Address", width=300)

contact_list.pack(pady=10)

contact_list.bind(
    "<<TreeviewSelect>>",
    select_contact
)

root.mainloop()