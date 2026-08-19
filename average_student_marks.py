import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT AVG(marks) FROM students")
average_marks = cursor.fetchone()[0]
print(f"Average student marks: {average_marks:.2f}")

cursor.close()
connection.close()
