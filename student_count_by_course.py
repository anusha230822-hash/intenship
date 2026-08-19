import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute(
    """
    SELECT course, COUNT(*) AS student_count
    FROM students
    GROUP BY course
    ORDER BY course
    """
)

print("Number of students in each course:")
for course, student_count in cursor.fetchall():
    print(f"{course}: {student_count}")

cursor.close()
connection.close()
