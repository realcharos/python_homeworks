from library import Library, BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException

library = Library()

library.add_book("Harry Potter", "J.K. Rowling")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

library.add_member("Alice")
library.add_member("Bob")

try:
    library.borrow_book("Alice", "Harry Potter")
    library.borrow_book("Bob", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "1984")  # Should raise BookAlreadyBorrowedException
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print("Error:", e)


library.display_books()
library.display_members()

library.return_book("Alice", "Harry Potter")
library.display_books()
