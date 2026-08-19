import os

import mysql.connector


def add_student(student_id, name, age, course, marks):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )
    cursor = connection.cursor()
    query = "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (student_id, name, age, course, marks))
    connection.commit()
    print("Student added successfully.")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    add_student(10, "Kavya", 21, "Python", 86.0)
