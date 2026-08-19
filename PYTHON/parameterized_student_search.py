import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

name = input("Enter student name to search: ")
query = "SELECT id, name, age, course, marks FROM students WHERE name = %s"

cursor = connection.cursor()
cursor.execute(query, (name,))
students = cursor.fetchall()

print("Parameterized search results:")
if students:
    for student in students:
        print(student)
else:
    print("No student found.")

cursor.close()
connection.close()
