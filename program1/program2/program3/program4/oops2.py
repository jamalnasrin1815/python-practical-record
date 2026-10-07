# Library Management System - Example 2

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued successfully.")
        else:
            print(self.title, "is already issued.")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned successfully.")
        else:
            print(self.title, "is not currently issued.")


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if not book.issued:
            book.issue()
            self.borrowed_books.append(book)
        else:
            print("Book is unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("This book was not borrowed by", self.name)


# Creating books
book1 = Book("Python", "Guido")
book2 = Book("Java", "James")

# Creating users
user1 = User("Rahul")
user2 = User("Priya")

print("===== LIBRARY MANAGEMENT =====")

print("\nUser:", user1.name)
user1.borrow(book1)

print("\nUser:", user2.name)
user2.borrow(book2)

print("\nTrying to borrow Python again:")
user2.borrow(book1)

print("\nReturning Python:")
user1.return_book(book1)

print("\nPriya borrows Python:")
user2.borrow(book1)