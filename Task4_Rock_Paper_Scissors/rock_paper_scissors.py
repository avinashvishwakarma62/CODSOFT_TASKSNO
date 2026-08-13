import random

print("===== ROCK PAPER SCISSORS =====")

user_score = 0
computer_score = 0

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice.")
        continue

    options = ["Rock", "Paper", "Scissors"]
    user_choice = options[int(choice) - 1]
    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1