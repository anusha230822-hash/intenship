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
    SELECT student_name, course_name
    FROM college_students
    JOIN enrollments USING (student_id)
    JOIN college_courses USING (course_id)
    ORDER BY student_name
    """
)

print("Students with their course names:")
for student_name, course_name in cursor.fetchall():
    print(f"{student_name} | {course_name}")

cursor.close()
connection.close()
