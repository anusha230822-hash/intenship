import os

import mysql.connector


def search_student(student_id=None, name=None):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )
    cursor = connection.cursor()
    if student_id is not None:
        cursor.execute(
            "SELECT id, name, age, course, marks FROM students WHERE id = %s",
            (student_id,),
        )
    elif name is not None:
        cursor.execute(
            "SELECT id, name, age, course, marks FROM students WHERE name LIKE %s",
            (f"%{name}%",),
        )
    else:
        raise ValueError("Provide a student ID or name.")
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students


if __name__ == "__main__":
    print("Search results:")
    for student in search_student(name="Anu"):
        print(student)
