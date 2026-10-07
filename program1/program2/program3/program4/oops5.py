# Library Management System using OOP

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.book_id, "-", self.title, "-", status)


class User:
    def __init__(self, name):
        self.name = name

    def issue(self, book):
        if book.available:
            book.available = False
            print(self.name, "issued", book.title)
        else:
            print("Book is already issued.")

    def return_book(self, book):
        if not book.available:
            book.available = True
            print(self.name, "returned", book.title)
        else:
            print("Book is already available.")

    def show_role(self):
        print("User:", self.name)


class Student(User):
    def show_role(self):
        print("Student:", self.name)


class Librarian(User):
    def show_role(self):
        print("Librarian:", self.name)


# Creating books
book1 = Book(101, "Python Programming")
book2 = Book(102, "Java Programming")

# Creating users
student = Student("Arun")
librarian = Librarian("Meena")

books = [book1, book2]
users = [student, librarian]

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Users")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- BOOK LIST ---")
        for book in books:
            book.display()

    elif choice == "2":
        book_id = int(input("Enter book ID: "))

        for book in books:
            if book.book_id == book_id:
                student.issue(book)
                break
        else:
            print("Book not found.")

    elif choice == "3":
        book_id = int(input("Enter book ID: "))

        for book in books:
            if book.book_id == book_id:
                student.return_book(book)
                break
        else:
            print("Book not found.")

    elif choice == "4":
        print("\n--- USER LIST ---")

        # Polymorphism
        for user in users:
            user.show_role()

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice.")