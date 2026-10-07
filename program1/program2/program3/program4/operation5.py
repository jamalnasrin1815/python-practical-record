# Complete Contact Management System
# Using List, Dictionary and File Handling

import json

FILE_NAME = "contacts.txt"


# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save contacts to file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()

    print("Contact added successfully.")


# Search contact
def search_contact():
    name = input("Enter name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            print("\n--- Contact Found ---")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])

            found = True
            break

    if not found:
        print("Contact not found.")


# Delete contact
def delete_contact():
    name = input("Enter name to delete: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            contacts.remove(contact)
            save_contacts()

            print("Contact deleted successfully.")
            found = True
            break

    if not found:
        print("Contact not found.")


# Display all contacts
def display_contacts():

    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("\n===== ALL CONTACTS =====")

    for contact in contacts:
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("------------------------")


# Load existing contacts
contacts = load_contacts()


# Main menu
while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        display_contacts()

    elif choice == "5":
        print("Contacts saved successfully.")
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Please try again.")