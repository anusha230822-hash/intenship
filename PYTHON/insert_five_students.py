import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

students = [
    (2, "Rahul", 20, "Java", 76.0),
    (3, "Priya", 22, "Python", 91.0),
    (4, "Vikram", 21, "SQL", 68.5),
    (5, "Neha", 20, "Python", 82.0),
    (6, "Arjun", 23, "Java", 73.5),
]
query = "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)"

cursor = connection.cursor()
cursor.executemany(query, students)
connection.commit()
print(f"{cursor.rowcount} student records inserted successfully.")

cursor.close()
connection.close()
