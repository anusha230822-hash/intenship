import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

student_id = int(input("Enter student ID: "))
new_name = input("Enter the new name: ")
query = "UPDATE students SET name = %s WHERE id = %s"

cursor = connection.cursor()
cursor.execute(query, (new_name, student_id))
connection.commit()
print(f"Student name updated successfully. Rows changed: {cursor.rowcount}")

cursor.close()
connection.close()
