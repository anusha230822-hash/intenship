from database_manager import DatabaseManager


class Library:
    def __init__(self):
        self.database = DatabaseManager()

    def issue_book(self, book_id, student_id):
        self.database.execute(
            "UPDATE library_books SET available = FALSE, issued_to = %s "
            "WHERE book_id = %s AND available = TRUE",
            (student_id, book_id),
        )
        self.database.commit()
        print(f"Book issued. Rows changed: {self.database.row_count}")

    def return_book(self, book_id):
        self.database.execute(
            "UPDATE library_books SET available = TRUE, issued_to = NULL WHERE book_id = %s",
            (book_id,),
        )
        self.database.commit()
        print(f"Book returned. Rows changed: {self.database.row_count}")

    def available_books(self):
        return self.database.fetch_all(
            "SELECT book_id, title, author FROM library_books WHERE available = TRUE"
        )

    def close(self):
        self.database.close()


if __name__ == "__main__":
    library = Library()
    print(library.available_books())
    library.close()
