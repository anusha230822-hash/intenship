import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS enrollments")
cursor.execute("DROP TABLE IF EXISTS college_students")
cursor.execute("DROP TABLE IF EXISTS college_courses")
cursor.execute(
    """
    CREATE TABLE college_students (
        student_id INT PRIMARY KEY,
        student_name VARCHAR(100) NOT NULL
    )
    """
)
cursor.execute(
    """
    CREATE TABLE college_courses (
        course_id INT PRIMARY KEY,
        course_name VARCHAR(100) NOT NULL
    )
    """
)
cursor.execute(
    """
    CREATE TABLE enrollments (
        student_id INT,
        course_id INT,
        enrollment_date DATE NOT NULL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES college_students(student_id),
        FOREIGN KEY (course_id) REFERENCES college_courses(course_id)
    )
    """
)
cursor.executemany(
    "INSERT INTO college_students VALUES (%s, %s)",
    [(1, "Anusha"), (2, "Rahul"), (3, "Priya")],
)
cursor.executemany(
    "INSERT INTO college_courses VALUES (%s, %s)",
    [(101, "Python"), (102, "SQL"), (103, "Java")],
)
cursor.executemany(
    "INSERT INTO enrollments VALUES (%s, %s, %s)",
    [(1, 101, "2026-01-10"), (1, 102, "2026-01-11"), (2, 101, "2026-01-12"), (3, 103, "2026-01-13")],
)
connection.commit()
print("College students, courses, and enrollments tables created successfully.")

cursor.close()
connection.close()
