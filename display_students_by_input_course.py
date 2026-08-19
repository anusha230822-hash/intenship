import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

course = input("Enter course name: ")
query = "SELECT id, name, age, course, marks FROM students WHERE course = %s"

cursor = connection.cursor()
cursor.execute(query, (course,))
students = cursor.fetchall()

print(f"Students in the {course} course:")
if students:
    print("ID | Name | Age | Course | Marks")
    for student_id, name, age, student_course, marks in students:
        print(f"{student_id} | {name} | {age} | {student_course} | {marks}")
else:
    print("No students found for this course.")

cursor.close()
connection.close()
