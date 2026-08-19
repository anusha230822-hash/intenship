import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

maximum_marks = float(input("Delete students with marks below: "))
query = "DELETE FROM students WHERE marks < %s"

cursor = connection.cursor()
cursor.execute(query, (maximum_marks,))
connection.commit()
print(f"{cursor.rowcount} student records deleted successfully.")

cursor.close()
connection.close()
