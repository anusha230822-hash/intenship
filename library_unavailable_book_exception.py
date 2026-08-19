class BookUnavailableError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {"Python Basics": True, "SQL Guide": False}

    def issue_book(self, title):
        if not self.books.get(title, False):
            raise BookUnavailableError(f"Book '{title}' is unavailable.")
        self.books[title] = False
        return f"Book '{title}' issued successfully."


try:
    library = Library()
    print(library.issue_book("SQL Guide"))
except BookUnavailableError as error:
    print(f"BookUnavailableError: {error}")
