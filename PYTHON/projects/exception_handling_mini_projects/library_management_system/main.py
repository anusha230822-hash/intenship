class UnavailableBookError(Exception):
    pass


class InvalidBookIdError(Exception):
    pass


class DuplicateBookError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {101: {"title": "Python Basics", "available": True}}

    def add_book(self, book_id, title):
        if book_id <= 0:
            raise InvalidBookIdError("Book ID must be positive.")
        if book_id in self.books:
            raise DuplicateBookError("Book ID already exists.")
        self.books[book_id] = {"title": title, "available": True}

    def issue(self, book_id):
        if book_id not in self.books:
            raise InvalidBookIdError("Book ID does not exist.")
        if not self.books[book_id]["available"]:
            raise UnavailableBookError("Book is not available.")
        self.books[book_id]["available"] = False


try:
    library = Library()
    library.issue(101)
    print("Book issued successfully.")
except (UnavailableBookError, InvalidBookIdError, DuplicateBookError) as error:
    print(f"Library error: {error}")
