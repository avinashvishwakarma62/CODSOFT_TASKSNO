import tkinter as tk
import random


user_score = 0
computer_score = 0

options = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(options)

    user_label.config(
        text="Your Choice: " + user_choice
    )

    computer_label.config(
        text="Computer Choice: " + computer_choice
    )

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You Win!")
        user_score += 1

    else:
        result_label.config(text="Computer Wins!")
        computer_score += 1

    score_label.config(
        text=f"Score  You: {user_score}    Computer: {computer_score}"
    )


def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer Choice: ")
    result_label.config(text="Choose your move!")
    score_label.config(text="Score  You: 0    Computer: 0")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("550x550")
root.resizable(False, False)

title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 22, "bold")
)
title.pack(pady=30)

result_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=20)

user_label = tk.Label(
    root,
    text="Your Choice: ",
    font=("Arial", 13)
)
user_label.pack(pady=5)

computer_label = tk.Label(
    root,
    text="Computer Choice: ",
    font=("Arial", 13)
)
computer_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

tk.Button(
    button_frame,
    text="Rock",
    width=12,
    height=2,
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="Paper",
    width=12,
    height=2,
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=8)

tk.Button(
    button_frame,
    text="Scissors",
    width=12,
    height=2,
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=8)

score_label = tk.Label(
    root,
    text="Score  You: 0    Computer: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=20)

tk.Button(
    root,
    text="Reset Game",
    width=18,
    command=reset_game
).pack(pady=10)

root.mainloop()