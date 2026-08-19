import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT MAX(marks) FROM students")
highest_marks = cursor.fetchone()[0]
print(f"Highest student marks: {highest_marks}")

cursor.close()
connection.close()
