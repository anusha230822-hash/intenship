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
    SELECT student_name, COUNT(course_id) AS course_count
    FROM college_students
    JOIN enrollments USING (student_id)
    GROUP BY student_id, student_name
    HAVING COUNT(course_id) > 1
    """
)

print("Students enrolled in multiple courses:")
for student_name, course_count in cursor.fetchall():
    print(f"{student_name}: {course_count} courses")

cursor.close()
connection.close()
