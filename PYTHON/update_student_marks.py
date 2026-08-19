import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student_id = int(input("Enter student ID: "))
new_marks = float(input("Enter the new marks: "))
query = "UPDATE students SET marks = %s WHERE id = %s"

cursor = connection.cursor()
cursor.execute(query, (new_marks, student_id))
connection.commit()
print(f"Student marks updated successfully. Rows changed: {cursor.rowcount}")

cursor.close()
connection.close()
