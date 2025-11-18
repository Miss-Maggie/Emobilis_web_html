# Book class
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({self.isbn})"

# Member class
class Member:
    def __init__(self, name, memberid):
        self.name = name
        self.memberid = memberid
        self.borrowedbooks = []

    def borrow_book(self, book):
        if book.available:
            self.borrowedbooks.append(book)
            book.available = False
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowedbooks:
            self.borrowedbooks.remove(book)
            book.available = True
            print(f"{self.name} has returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title}.")

# Librarian Class
class Librarian(Member):
    def add_book(self, book, catalog):
        catalog.append(book)
        print(f"{book.title}  has been added to catalog.")

    def remove_book(self, book, catalog):
        if book in catalog:
            catalog.remove(book)
            print(f"{book.title} has been removed from catalog.")
        else:
            print(f"{book.title} is not found in catalog.")

# Library class
class Library:
    def __init__(self):
        self.catalog = []

    def searchbytitle(self, title):
        results = [book for book in self.catalog if title.lower() in book.title.lower()]
        return results

    def display_books(self):
        for book in self.catalog:
            status = "Available" if book.available else "Not Available"
            print(f"{book} - {status}")

# Create library
library = Library()

# Create librarian
lib = Librarian("Alice", "L001")

# Create books
b1 = Book("The Pragmatic Programmer", "Andrew Hunt & David Thomas", "9780201616224")
b2 = Book("Introduction to Algorithms", "Thomas H. Cormen", "9780262033848")

# Librarian adds books
lib.add_book(b1, library.catalog)
lib.add_book(b2, library.catalog)

# Display catalog
library.display_books()

# Create member
m1 = Member("Bob", "M001")

# Borrow and return books
m1.borrow_book(b1)
library.display_books()

m1.return_book(b1)
library.display_books()

# Search by title
results = library.searchbytitle("Python")
for r in results:
    print("Found:", r)
