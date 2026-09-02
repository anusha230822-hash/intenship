from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_library_books (id INT PRIMARY KEY, title VARCHAR(200), author VARCHAR(100), available BOOLEAN DEFAULT TRUE, issued_to INT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_library_students (id INT PRIMARY KEY, name VARCHAR(100))")
    connection.commit()
    cursor.close()


def add_book(connection, book_id, title, author):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mini_library_books (id, title, author) VALUES (%s, %s, %s)", (book_id, title, author))
    connection.commit()
    cursor.close()


def issue_book(connection, book_id, student_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE mini_library_books SET available = FALSE, issued_to = %s WHERE id = %s AND available = TRUE", (student_id, book_id))
    connection.commit()
    print(f"Book issued. Rows changed: {cursor.rowcount}")
    cursor.close()


def return_book(connection, book_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE mini_library_books SET available = TRUE, issued_to = NULL WHERE id = %s", (book_id,))
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("Library Management System ready.")
    database.close()
