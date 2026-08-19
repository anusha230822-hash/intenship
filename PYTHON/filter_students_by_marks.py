import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute(
    "SELECT id, name, age, course, marks FROM students WHERE marks > %s",
    (75,),
)

students = cursor.fetchall()
print("Students with marks greater than 75:")
if students:
    print("ID | Name | Age | Course | Marks")
    for student_id, name, age, course, marks in students:
        print(f"{student_id} | {name} | {age} | {course} | {marks}")
else:
    print("No students found with marks greater than 75.")

cursor.close()
connection.close()
