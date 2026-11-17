class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        print("\n--- Library Books ---")

        for book in self.books:
            status = "Available" if book.available else "Issued"

            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)
            print("-------------------")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return

        print("Book not found!")

# Creating library object
library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == 5:
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Try again.")
