import os

import mysql.connector


def get_students():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, course, marks FROM students ORDER BY id")
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students


if __name__ == "__main__":
    print("All students:")
    for student in get_students():
        print(student)
