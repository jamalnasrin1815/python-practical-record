# Contact Management System using CSV File

import csv

filename = "contacts.csv"

# Load existing contacts
contacts = []

try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
except FileNotFoundError:
    pass


while True:
    print("\n===== CONTACT MANAGEMENT =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        # Save contacts
        with open(filename, "w", newline="") as file:
            fields = ["name", "phone", "email"]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(contacts)

        print("Contact added successfully.")

    # Search Contact
    elif choice == "2":
        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("\nContact Found!")
                print("Name :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete Contact
    elif choice == "3":
        name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                found = True
                break

        if found:
            with open(filename, "w", newline="") as file:
                fields = ["name", "phone", "email"]
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(contacts)

            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Display Contacts
    elif choice == "4":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n----- CONTACT LIST -----")

            for contact in contacts:
                print("Name :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("------------------------")

    # Exit
    elif choice == "5":
        print("Thank you for using Contact Management System.")
        break

    else:
        print("Invalid choice.")