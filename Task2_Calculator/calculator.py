print("===== SIMPLE CALCULATOR =====")

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using Calculator!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", num1 + num2)

            elif choice == "2":
                print("Result:", num1 - num2)

            elif choice == "3":
                print("Result:", num1 * num2)

            elif choice == "4":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Result:", num1 / num2)

        except ValueError:
            print("Please enter valid numbers.")

    else:
        print("Invalid choice.")