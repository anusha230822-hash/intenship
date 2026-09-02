from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_students (id INT PRIMARY KEY, name VARCHAR(100), course VARCHAR(100), marks DECIMAL(5,2))")
    connection.commit()
    cursor.close()


def add_student(connection, student_id, name, course, marks):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mini_students VALUES (%s, %s, %s, %s)", (student_id, name, course, marks))
    connection.commit()
    cursor.close()


def get_students(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mini_students ORDER BY id")
    records = cursor.fetchall()
    cursor.close()
    return records


def update_student(connection, student_id, marks):
    cursor = connection.cursor()
    cursor.execute("UPDATE mini_students SET marks = %s WHERE id = %s", (marks, student_id))
    connection.commit()
    cursor.close()


def delete_student(connection, student_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM mini_students WHERE id = %s", (student_id,))
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("Student Management System ready.")
    print("Records:", get_students(database))
    database.close()
