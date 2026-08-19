import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student_id = int(input("Enter student ID to delete: "))
query = "DELETE FROM students WHERE id = %s"

cursor = connection.cursor()
cursor.execute(query, (student_id,))
connection.commit()

if cursor.rowcount:
    print("Student record deleted successfully.")
else:
    print("Student not found. No record was deleted.")

cursor.close()
connection.close()
