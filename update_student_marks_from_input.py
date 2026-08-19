import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student_id = int(input("Enter student ID: "))
new_marks = float(input("Enter new marks: "))
query = "UPDATE students SET marks = %s WHERE id = %s"

cursor = connection.cursor()
cursor.execute(query, (new_marks, student_id))
connection.commit()

if cursor.rowcount:
    print("Student marks updated successfully.")
else:
    print("Student not found. No marks were updated.")

cursor.close()
connection.close()
