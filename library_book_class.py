from database_manager import DatabaseManager


class LibraryBook:
    def __init__(self):
        self.database = DatabaseManager()
        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS library_books (
                book_id INT PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                author VARCHAR(100) NOT NULL,
                available BOOLEAN NOT NULL DEFAULT TRUE,
                issued_to INT NULL
            )
            """
        )
        self.database.commit()

    def add(self, book_id, title, author):
        self.database.execute(
            "INSERT INTO library_books (book_id, title, author, available) VALUES (%s, %s, %s, %s)",
            (book_id, title, author, True),
        )
        self.database.commit()
        print("Library book added successfully.")

    def get_all(self):
        return self.database.fetch_all(
            "SELECT book_id, title, author, available FROM library_books ORDER BY book_id"
        )

    def search(self, title):
        return self.database.fetch_all(
            "SELECT book_id, title, author, available FROM library_books WHERE title LIKE %s",
            (f"%{title}%",),
        )

    def close(self):
        self.database.close()


if __name__ == "__main__":
    book = LibraryBook()
    print(book.search("Python"))
    book.close()
