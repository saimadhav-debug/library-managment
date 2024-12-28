class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_loaned = False
        self.is_reserved = False
        self.reserved_by = None

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book_id = len(self.books) + 1
        if book_id in self.books:
            print(f"Book ID {book_id} already exists.")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print(f"Book '{title}' added to library with ID: {book_id}")

    def register_member(self):
        name = input("Enter member name: ")
        member_id = len(self.members) + 1
        if member_id in self.members:
            print(f"Member ID {member_id} already registered.")
        else:
            self.members[member_id] = Member(member_id, name)
            print(f"Member '{name}' registered with ID: {member_id}")

    def loan_book(self):
        book_id = int(input("Enter book ID to loan: "))
        member_id = int(input("Enter member ID: "))

        if book_id not in self.books:
            print("Book not found.")
            return

        if member_id not in self.members:
            print("Member not found.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_loaned:
            print(f"Book '{book.title}' is already loaned.")
        else:
            book.is_loaned = True
            member.borrowed_books.append(book)
            print(f"Book '{book.title}' loaned to {member.name}.")

    def return_book(self):
        book_id = int(input("Enter book ID to return: "))
        member_id = int(input("Enter member ID: "))

        if book_id not in self.books:
            print("Book not found.")
            return

        if member_id not in self.members:
            print("Member not found.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.is_loaned = False
            print(f"Book '{book.title}' returned by {member.name}.")

            if book.is_reserved and book.reserved_by:
                print(f"Book '{book.title}' is reserved by {book.reserved_by.name}. It's now available for pickup.")
        else:
            print(f"Book '{book.title}' is not borrowed by {member.name}.")

    def search_books(self):
        query = input("Enter search query (title/author): ")
        results = [book for book in self.books.values() if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        if results:
            print("Search results:")
            for book in results:
                status = "Available" if not book.is_loaned else "Loaned"
                print(f"- {book.title} by {book.author} (ID: {book.book_id}) [{status}]")
        else:
            print("No books found.")

    def list_borrowed_books(self):
        borrowed = [book for book in self.books.values() if book.is_loaned]
        if borrowed:
            print("Borrowed books:")
            for book in borrowed:
                print(f"- {book.title} by {book.author} (ID: {book.book_id})")
        else:
            print("No books are currently borrowed.")

    def reserve_book(self):
        book_id = int(input("Enter book ID to reserve: "))
        member_id = int(input("Enter member ID: "))

        if book_id not in self.books:
            print("Book not found.")
            return

        if member_id not in self.members:
            print("Member not found.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_loaned:
            if not book.is_reserved:
                book.is_reserved = True
                book.reserved_by = member
                print(f"Book '{book.title}' reserved by {member.name}.")
            else:
                print(f"Book '{book.title}' is already reserved.")
        else:
            print(f"Book '{book.title}' is available and cannot be reserved.")

library = Library()
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Loan Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. List Borrowed Books")
    print("7. Reserve Book")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.register_member()
    elif choice == '3':
        library.loan_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        library.search_books()
    elif choice == '6':
        library.list_borrowed_books()
    elif choice == '7':
        library.reserve_book()
    elif choice == '8':
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")