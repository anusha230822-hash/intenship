import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS relationship_students")
cursor.execute("DROP TABLE IF EXISTS relationship_courses")
cursor.execute(
    """
    CREATE TABLE relationship_courses (
        course_id INT PRIMARY KEY,
        course_name VARCHAR(100) NOT NULL
    )
    """
)
cursor.execute(
    """
    CREATE TABLE relationship_students (
        student_id INT PRIMARY KEY,
        student_name VARCHAR(100) NOT NULL,
        course_id INT,
        CONSTRAINT fk_student_course
            FOREIGN KEY (course_id) REFERENCES relationship_courses(course_id)
    )
    """
)
connection.commit()
print("Students and courses tables created with a foreign-key relationship.")

cursor.close()
connection.close()
