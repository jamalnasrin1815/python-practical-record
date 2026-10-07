# Library Management System - Example 3
# Using Inheritance

class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False


class User:
    def __init__(self, name):
        self.name = name

    def issue_book(self, book):
        if not book.issued:
            book.issued = True
            print(self.name, "issued", book.title)
        else:
            print(book.title, "is already issued.")

    def return_book(self, book):
        if book.issued:
            book.issued = False
            print(self.name, "returned", book.title)
        else:
            print(book.title, "is not issued.")


class Student(User):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        print("Student:", self.name)
        print("Roll No:", self.roll_no)


class Teacher(User):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display(self):
        print("Teacher:", self.name)
        print("Employee ID:", self.employee_id)


# Objects
book = Book("Data Structures")

student = Student("Nasrin", 101)
teacher = Teacher("Dr. Jamal" , "T205")

print("===== LIBRARY SYSTEM =====")

student.display()
student.issue_book(book)

print()

teacher.display()
teacher.issue_book(book)

print()

student.return_book(book)

print()

teacher.issue_book(book)