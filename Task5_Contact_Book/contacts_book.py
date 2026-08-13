contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully.")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("\n===== CONTACT LIST =====")

    for i in range(len(contacts)):
        print("\nContact", i + 1)
        print("Name:", contacts[i]["name"])
        print("Phone:", contacts[i]["phone"])


def search_contact():
    search = input("Enter name or phone number to search: ").lower()

    found = False

    for contact in contacts:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nName:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    view_contacts()

    if len(contacts) == 0:
        return

    try:
        number = int(input("Enter contact number to update: "))

        if number >= 1 and number <= len(contacts):
            contact = contacts[number - 1]

            print("\nLeave blank if you don't want to change anything.")

            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            if name != "":
                contact["name"] = name

            if phone != "":
                contact["phone"] = phone

            if email != "":
                contact["email"] = email

            if address != "":
                contact["address"] = address

            print("Contact updated successfully.")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_contact():
    view_contacts()

    if len(contacts) == 0:
        return

    try:
        number = int(input("Enter contact number to delete: "))

        if number >= 1 and number <= len(contacts):
            contacts.pop(number - 1)
            print("Contact deleted successfully.")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n==============================")
    print("        CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")