class BookNotAvailableError(Exception):
    pass


available_books = {"Python Basics": True, "SQL Guide": False}
try:
    title = input("Enter book title: ")
    if not available_books.get(title, False):
        raise BookNotAvailableError(f"The book '{title}' is not available.")
    print(f"Book '{title}' issued successfully.")
except BookNotAvailableError as error:
    print(f"BookNotAvailableError: {error}")
