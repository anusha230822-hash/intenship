import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT MIN(marks) FROM students")
lowest_marks = cursor.fetchone()[0]
print(f"Lowest student marks: {lowest_marks}")

cursor.close()
connection.close()
