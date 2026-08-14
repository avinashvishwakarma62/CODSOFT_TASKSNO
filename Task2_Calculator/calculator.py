import tkinter as tk


expression = ""


def press(value):
    global expression

    expression += str(value)
    display.set(expression)


def clear():
    global expression

    expression = ""
    display.set("")


def backspace():
    global expression

    expression = expression[:-1]
    display.set(expression)


def calculate():
    global expression

    try:
        result = eval(expression)
        display.set(str(result))
        expression = str(result)

    except:
        display.set("Error")
        expression = ""


def percent():
    global expression

    try:
        result = eval(expression) / 100
        display.set(str(result))
        expression = str(result)

    except:
        display.set("Error")
        expression = ""


def keyboard_input(event):
    key = event.keysym
    char = event.char

    if char in "0123456789.+-*/":
        press(char)

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()

    elif char == "%":
        percent()


root = tk.Tk()
root.title("Calculator")
root.geometry("400x580")
root.resizable(False, False)

root.configure(bg="#202124")

display = tk.StringVar()

display_box = tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 28),
    justify="right",
    bg="#303134",
    fg="white",
    insertbackground="white",
    relief="flat"
)

display_box.pack(
    padx=20,
    pady=25,
    ipady=18,
    fill="x"
)

button_frame = tk.Frame(
    root,
    bg="#202124"
)

button_frame.pack(
    padx=15,
    pady=5
)


def create_button(text, row, column, command, width=6):
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16, "bold"),
        width=width,
        height=2,
        command=command,
        bg="#303134",
        fg="white",
        activebackground="#5f6368",
        activeforeground="white",
        relief="flat",
        bd=0
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


create_button("C", 0, 0, clear)
create_button("⌫", 0, 1, backspace)
create_button("%", 0, 2, percent)
create_button("÷", 0, 3, lambda: press("/"))

create_button("7", 1, 0, lambda: press("7"))
create_button("8", 1, 1, lambda: press("8"))
create_button("9", 1, 2, lambda: press("9"))
create_button("×", 1, 3, lambda: press("*"))

create_button("4", 2, 0, lambda: press("4"))
create_button("5", 2, 1, lambda: press("5"))
create_button("6", 2, 2, lambda: press("6"))
create_button("−", 2, 3, lambda: press("-"))

create_button("1", 3, 0, lambda: press("1"))
create_button("2", 3, 1, lambda: press("2"))
create_button("3", 3, 2, lambda: press("3"))
create_button("+", 3, 3, lambda: press("+"))

create_button("0", 4, 0, lambda: press("0"))
create_button(".", 4, 1, lambda: press("."))
create_button("=", 4, 2, calculate)
create_button("÷", 4, 3, lambda: press("/"))


root.bind("<Key>", keyboard_input)

display_box.focus_set()

root.mainloop()