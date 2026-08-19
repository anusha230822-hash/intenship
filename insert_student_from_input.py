import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student = (
    int(input("Enter student ID: ")),
    input("Enter student name: "),
    int(input("Enter student age: ")),
    input("Enter student course: "),
    float(input("Enter student marks: ")),
)
query = "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)"

cursor = connection.cursor()
cursor.execute(query, student)
connection.commit()
print("Student details inserted successfully.")

cursor.close()
connection.close()
