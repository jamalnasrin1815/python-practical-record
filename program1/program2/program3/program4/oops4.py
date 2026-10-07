# Complete Library Management System
# Using Inheritance and Polymorphism

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        status = "Issued" if self.issued else "Available"
        print(self.title, "-", self.author, "-", status)


class User:
    def __init__(self, name):
        self.name = name

    def issue_book(self, book):
        if not book.issued:
            book.issued = True
            print(self.name, "issued", book.title)
        else:
            print(book.title, "is not available.")

    def return_book(self, book):
        if book.issued:
            book.issued = False
            print(self.name, "returned", book.title)
        else:
            print(book.title, "is already available.")

    def display(self):
        print("User:", self.name)


# Inheritance
class Student(User):
    def display(self):
        print("Student:", self.name)


class Teacher(User):
    def display(self):
        print("Teacher:", self.name)


# Creating books
book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Data Structures", "Mark Allen")
book3 = Book("Computer Networks", "Andrew Tanenbaum")

books = [book1, book2, book3]

# Creating users
student = Student("Rahul")
teacher = Teacher("Dr. Priya")

users = [student, teacher]

print("========== LIBRARY MANAGEMENT SYSTEM ==========")

# Polymorphism
print("\n--- Users ---")

for user in users:
    user.display()

print("\n--- Available Books ---")

for book in books:
    book.display()

print("\n--- Book Operations ---")

student.issue_book(book1)
teacher.issue_book(book1)

teacher.issue_book(book2)

print("\n--- After Issuing ---")

for book in books:
    book.display()

print("\n--- Returning Book ---")

student.return_book(book1)

print("\n--- Teacher Issues Returned Book ---")

teacher.issue_book(book1)

print("\n--- Final Book Status ---")

for book in books:
    book.display()

            