import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student = (1, "Anusha", 21, "Python", 88.5)
query = "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)"

cursor = connection.cursor()
cursor.execute(query, student)
connection.commit()
print("One student record inserted successfully.")

cursor.close()
connection.close()
