import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

query = """
    SELECT id, name, age, course, marks
    FROM students
    WHERE marks BETWEEN %s AND %s
    ORDER BY marks
"""

cursor = connection.cursor()
cursor.execute(query, (50, 80))
students = cursor.fetchall()

print("Students with marks between 50 and 80:")
if students:
    print("ID | Name | Age | Course | Marks")
    for student_id, name, age, course, marks in students:
        print(f"{student_id} | {name} | {age} | {course} | {marks}")
else:
    print("No students found in this marks range.")

cursor.close()
connection.close()
