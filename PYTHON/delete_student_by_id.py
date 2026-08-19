import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student_id = int(input("Enter the student ID to delete: "))
query = "DELETE FROM students WHERE id = %s"

cursor = connection.cursor()
cursor.execute(query, (student_id,))
connection.commit()
print(f"Student deleted successfully. Rows deleted: {cursor.rowcount}")

cursor.close()
connection.close()
