import os

import mysql.connector


def delete_student(student_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    connection.commit()
    print(f"Student deleted successfully. Rows deleted: {cursor.rowcount}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    delete_student(10)
