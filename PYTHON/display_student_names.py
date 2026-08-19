import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT name FROM students")

names = cursor.fetchall()
print("Student names:")
if names:
    for (name,) in names:
        print(f"- {name}")
else:
    print("No student names found.")

cursor.close()
connection.close()
