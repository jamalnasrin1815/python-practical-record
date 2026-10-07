# Contact Management using List and Dictionary

contacts = []

while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Exit")

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
        search = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "3":
        print("\n--- All Contacts ---")

        for contact in contacts:
            print(contact["name"],
                  "|", contact["phone"],
                  "|", contact["email"])

    elif choice == "4":
        print("Exiting Contact Management System.")
        break

    else:
        print("Invalid choice.")