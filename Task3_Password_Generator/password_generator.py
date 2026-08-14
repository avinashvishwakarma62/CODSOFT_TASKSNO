import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    mode = choice.get()

    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")
        return

    if length < 8:
        messagebox.showwarning(
            "Warning",
            "Password length must be at least 8 characters."
        )
        return

    # ---------------- NAME BASED PASSWORD ----------------
    if mode == "name":

        word = name_entry.get().strip()

        if word == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a name or word."
            )
            return

        # Keep only letters and numbers
        word = "".join(ch for ch in word if ch.isalnum())

        if len(word) == 0:
            messagebox.showwarning(
                "Warning",
                "Please enter a valid name or word."
            )
            return

        # If name is longer than required length
        if len(word) > length - 4:
            word = word[:length - 4]

        # Change random letters to uppercase/lowercase
        name_part = ""

        for ch in word:
            if ch.isalpha():
                if random.choice([True, False]):
                    name_part += ch.upper()
                else:
                    name_part += ch.lower()
            else:
                name_part += ch

        # Required strong characters
        number1 = random.choice(string.digits)
        number2 = random.choice(string.digits)

        symbol1 = random.choice("@#$%&*!")
        symbol2 = random.choice("@#$%&*!")

        extra = number1 + symbol1 + number2 + symbol2

        remaining_length = length - len(name_part) - len(extra)

        random_part = ""

        all_characters = (
            string.ascii_letters +
            string.digits +
            "@#$%&*!"
        )

        for i in range(remaining_length):
            random_part += random.choice(all_characters)

        # Keep name clearly visible
        password = name_part + extra + random_part

        # Shuffle only the extra/random portion
        beginning = name_part
        ending = list(password[len(name_part):])

        random.shuffle(ending)

        password = beginning + "".join(ending)

    # ---------------- COMPLETELY RANDOM PASSWORD ----------------
    else:

        password = []

        # Make sure every type is included
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("@#$%&*!"))

        all_characters = (
            string.ascii_letters +
            string.digits +
            "@#$%&*!"
        )

        while len(password) < length:
            password.append(random.choice(all_characters))

        random.shuffle(password)

        password = "".join(password)

    password_entry.config(show="")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    show_button.config(text="Hide")


def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


def show_hide_password():

    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        show_button.config(text="Show")
    else:
        password_entry.config(show="")
        show_button.config(text="Hide")


def update_mode():

    if choice.get() == "name":
        name_entry.config(state="normal")
        name_entry.focus()

    else:
        name_entry.delete(0, tk.END)
        name_entry.config(state="disabled")


def clear_all():

    name_entry.config(state="normal")
    name_entry.delete(0, tk.END)

    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")

    password_entry.delete(0, tk.END)

    choice.set("name")
    update_mode()


# ---------------- WINDOW ----------------

root = tk.Tk()

root.title("Password Generator")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#181A1B")


# Title
tk.Label(
    root,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 24, "bold"),
    bg="#181A1B",
    fg="white"
).pack(pady=(30, 8))


tk.Label(
    root,
    text="Create a strong password your way",
    font=("Arial", 11),
    bg="#181A1B",
    fg="#B0B3B8"
).pack(pady=(0, 25))


# Main frame
main_frame = tk.Frame(
    root,
    bg="#242526"
)

main_frame.pack(
    padx=35,
    pady=5,
    fill="both",
    expand=True
)


# Password type
tk.Label(
    main_frame,
    text="Password Type",
    font=("Arial", 13, "bold"),
    bg="#242526",
    fg="white"
).pack(pady=(25, 12))


choice = tk.StringVar(value="name")


radio_frame = tk.Frame(
    main_frame,
    bg="#242526"
)

radio_frame.pack()


tk.Radiobutton(
    radio_frame,
    text="Based on Name / Word",
    variable=choice,
    value="name",
    command=update_mode,
    font=("Arial", 11),
    bg="#242526",
    fg="white",
    selectcolor="#242526",
    activebackground="#242526",
    activeforeground="white"
).pack(side="left", padx=10)


tk.Radiobutton(
    radio_frame,
    text="Completely Random",
    variable=choice,
    value="random",
    command=update_mode,
    font=("Arial", 11),
    bg="#242526",
    fg="white",
    selectcolor="#242526",
    activebackground="#242526",
    activeforeground="white"
).pack(side="left", padx=10)


# Name
tk.Label(
    main_frame,
    text="Name / Word",
    font=("Arial", 11, "bold"),
    bg="#242526",
    fg="white"
).pack(pady=(22, 5))


name_entry = tk.Entry(
    main_frame,
    width=40,
    font=("Arial", 13),
    bg="#303134",
    fg="white",
    insertbackground="white",
    relief="flat",
    justify="center"
)

name_entry.pack(ipady=9)


# Length
tk.Label(
    main_frame,
    text="Password Length",
    font=("Arial", 11, "bold"),
    bg="#242526",
    fg="white"
).pack(pady=(20, 5))


length_entry = tk.Entry(
    main_frame,
    width=10,
    font=("Arial", 13),
    bg="#303134",
    fg="white",
    insertbackground="white",
    relief="flat",
    justify="center"
)

length_entry.pack(ipady=8)
length_entry.insert(0, "12")


# Generate
tk.Button(
    main_frame,
    text="GENERATE PASSWORD",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45A049",
    activeforeground="white",
    relief="flat",
    width=25,
    height=2,
    command=generate_password
).pack(pady=24)


# Result
tk.Label(
    main_frame,
    text="Generated Password",
    font=("Arial", 11, "bold"),
    bg="#242526",
    fg="white"
).pack(pady=(0, 7))


password_frame = tk.Frame(
    main_frame,
    bg="#303134"
)

password_frame.pack(
    padx=25,
    fill="x"
)


password_entry = tk.Entry(
    password_frame,
    font=("Arial", 14),
    bg="#303134",
    fg="white",
    insertbackground="white",
    relief="flat",
    justify="center",
    show="*"
)

password_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10,
    padx=10
)


show_button = tk.Button(
    password_frame,
    text="Show",
    font=("Arial", 10, "bold"),
    bg="#303134",
    fg="white",
    relief="flat",
    command=show_hide_password
)

show_button.pack(
    side="right",
    padx=10
)


# Bottom buttons
button_frame = tk.Frame(
    main_frame,
    bg="#242526"
)

button_frame.pack(pady=20)


tk.Button(
    button_frame,
    text="📋 Copy",
    font=("Arial", 10, "bold"),
    width=14,
    height=2,
    bg="#303134",
    fg="white",
    activebackground="#5f6368",
    relief="flat",
    command=copy_password
).grid(row=0, column=0, padx=6)


tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 10, "bold"),
    width=14,
    height=2,
    bg="#303134",
    fg="white",
    activebackground="#5f6368",
    relief="flat",
    command=clear_all
).grid(row=0, column=1, padx=6)


update_mode()

root.mainloop()