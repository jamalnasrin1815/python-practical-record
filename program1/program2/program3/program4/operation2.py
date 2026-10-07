# Contact Management System using List

contacts = []

while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts.append([name, phone])
        print("Contact added successfully.")

    elif choice == "2":
        print("\n--- Contact List ---")

        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print("Name:", contact[0], "| Phone:", contact[1])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")