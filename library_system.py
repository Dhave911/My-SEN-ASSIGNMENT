class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not member:
            print(f"Member ID {member_id} not found.")
            return
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return
        if not book.is_available:
            print(f"Book '{book.title}' is already borrowed.")
            return

        book.is_available = False
        member.borrowed_books.append(book)
        print(f"Successfully borrowed: {book.title} to {member.name}")

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print(f"Member ID {member_id} not found.")
            return

        book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
        if not book:
            print(f"Book with ISBN {isbn} not found in member's borrowed list.")
            return

        book.is_available = True
        member.borrowed_books.remove(book)
        print(f"Successfully returned: {book.title} from {member.name}")

    def display_books(self):
        print("\nLibrary Inventory:")
        for book in self.books:
            print(book)


if __name__ == "__main__":
    # Demonstration
    my_library = Library()

    # Add books
    my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890"))
    my_library.add_book(Book("1984", "George Orwell", "0987654321"))

    # Register member
    member1 = Member("Alice", "M001")
    my_library.register_member(member1)

    # Transactions
    my_library.display_books()
    my_library.borrow_book("M001", "1234567890")
    my_library.display_books()
    my_library.return_book("M001", "1234567890")
    my_library.display_books()
