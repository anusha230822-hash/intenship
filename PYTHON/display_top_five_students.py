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
    """
    SELECT id, name, age, course, marks
    FROM students
    ORDER BY marks DESC
    LIMIT 5
    """
)
students = cursor.fetchall()

print("Top 5 students based on marks:")
if students:
    print("ID | Name | Age | Course | Marks")
    for student_id, name, age, course, marks in students:
        print(f"{student_id} | {name} | {age} | {course} | {marks}")
else:
    print("No student records found.")

cursor.close()
connection.close()
