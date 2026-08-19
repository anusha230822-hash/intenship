import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student_id = int(input("Enter student ID: "))
query = "SELECT id, name, age, course, marks FROM students WHERE id = %s"

cursor = connection.cursor()
cursor.execute(query, (student_id,))
student = cursor.fetchone()

if student:
    print("Student details:")
    print("ID | Name | Age | Course | Marks")
    print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]} | {student[4]}")
else:
    print("Student not found.")

cursor.close()
connection.close()
