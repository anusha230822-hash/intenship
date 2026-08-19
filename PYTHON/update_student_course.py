import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student_id = int(input("Enter student ID: "))
new_course = input("Enter the new course: ")
query = "UPDATE students SET course = %s WHERE id = %s"

cursor = connection.cursor()
cursor.execute(query, (new_course, student_id))
connection.commit()
print(f"Student course updated successfully. Rows changed: {cursor.rowcount}")

cursor.close()
connection.close()
