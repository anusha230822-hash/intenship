import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

name = input("Enter student name: ")
query = "SELECT id, name, age, course, marks FROM students WHERE name LIKE %s"

cursor = connection.cursor()
cursor.execute(query, (f"%{name}%",))
students = cursor.fetchall()

if students:
    print("Matching students:")
    print("ID | Name | Age | Course | Marks")
    for student_id, student_name, age, course, marks in students:
        print(f"{student_id} | {student_name} | {age} | {course} | {marks}")
else:
    print("No students found with that name.")

cursor.close()
connection.close()
