import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

old_course = input("Update students currently in course: ")
new_course = input("Enter the new course name: ")
query = "UPDATE students SET course = %s WHERE course = %s"

cursor = connection.cursor()
cursor.execute(query, (new_course, old_course))
connection.commit()
print(f"{cursor.rowcount} student records updated successfully.")

cursor.close()
connection.close()
