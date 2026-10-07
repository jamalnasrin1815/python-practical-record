# Library Management System - Example 1

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def issue_book(self):
        if not self.issued:
            self.issued = True
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")


class User:
    def __init__(self, name):
        self.name = name

    def display_user(self):
        print("User Name:", self.name)


# Creating objects
book1 = Book("Python Programming", "John Smith")
user1 = User("Jamal")

print("===== LIBRARY SYSTEM =====")

user1.display_user()

book1.issue_book()
book1.issue_book()
book1.return_book()
book1.return_book()