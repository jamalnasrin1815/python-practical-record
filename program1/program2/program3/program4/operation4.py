# Contact Management System
# Add, Search, Delete

contacts = []

while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        print("Contact added successfully.")

    elif choice == "2":

        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():

                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "3":

        name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():

                contacts.remove(contact)
                print("Contact deleted successfully.")

                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "4":

        print("\n--- Contact List ---")

        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for contact in contacts:
                print(
                    "Name:", contact["name"],
                    "| Phone:", contact["phone"],
                    "| Email:", contact["email"]
                )

    elif choice == "5":
        print("Thank you for using Contact Management System.")
        break

    else:
        print("Invalid choice.")