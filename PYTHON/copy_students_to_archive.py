import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students_archive LIKE students")
cursor.execute(
    """
    INSERT INTO students_archive (id, name, age, course, marks)
    SELECT id, name, age, course, marks
    FROM students
    WHERE id NOT IN (SELECT id FROM students_archive)
    """
)
connection.commit()
print(f"{cursor.rowcount} student records copied to students_archive.")

cursor.close()
connection.close()
