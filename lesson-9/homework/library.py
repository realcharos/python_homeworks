class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books!")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed!")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"{self.name} (Borrowed books: {[book.title for book in self.borrowed_books]})"
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library!")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found!")
            return

        book = self.find_book(book_title)
        member.borrow_book(book)
        print(f"'{book_title}' has been borrowed by {member_name}.")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found!")
            return

        book = self.find_book(book_title)
        member.return_book(book)
        print(f"'{book_title}' has been returned by {member_name}.")

    def display_books(self):
        for book in self.books:
            print(book)

    def display_members(self):
        for member in self.members:
            print(member)
