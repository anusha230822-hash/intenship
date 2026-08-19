import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

minimum_marks = float(input("Enter minimum marks: "))
maximum_marks = float(input("Enter maximum marks: "))
query = """
    SELECT id, name, age, course, marks
    FROM students
    WHERE marks BETWEEN %s AND %s
    ORDER BY marks
"""

cursor = connection.cursor()
cursor.execute(query, (minimum_marks, maximum_marks))
students = cursor.fetchall()

print(f"Students with marks between {minimum_marks:g} and {maximum_marks:g}:")
if students:
    print("ID | Name | Age | Course | Marks")
    for student_id, name, age, course, marks in students:
        print(f"{student_id} | {name} | {age} | {course} | {marks}")
else:
    print("No students found in this marks range.")

cursor.close()
connection.close()
