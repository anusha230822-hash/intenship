"""
SQLite3 Practice - Part C Setup: Create 3 Tables with Relationships
Setup for Part C exercises
"""

import sqlite3
from sqlite3 import Error


def execute_setup(db_name='college_partC.db'):
    """Create 3 tables with relationships"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part C - Setup: Create 3 Tables with Relationships")
        print("=" * 70)
        
        # Create courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL UNIQUE,
                credits INTEGER NOT NULL
            )
        ''')
        
        # Create students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students_advanced (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                marks REAL NOT NULL,
                gpa REAL
            )
        ''')
        
        # Create enrollments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date TEXT DEFAULT CURRENT_DATE,
                FOREIGN KEY (student_id) REFERENCES students_advanced(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        ''')
        
        print("\n✓ Tables created successfully")
        
        # Insert courses
        courses = [
            ('Python', 3),
            ('Java', 3),
            ('C++', 4),
            ('Database Design', 3)
        ]
        cursor.executemany('INSERT INTO courses (course_name, credits) VALUES (?, ?)', courses)
        
        # Insert students
        students = [
            ('Alice Johnson', 92, 3.8),
            ('Bob Smith', 78, 3.2),
            ('Charlie Davis', 88, 3.6),
            ('Diana Wilson', 65, 2.8),
            ('Eve Brown', 95, 3.9),
            ('Frank Miller', 72, 3.0)
        ]
        cursor.executemany('INSERT INTO students_advanced (name, marks, gpa) VALUES (?, ?, ?)', students)
        
        # Insert enrollments
        enrollments = [
            (1, 1), (1, 4), (2, 2), (3, 1), (3, 3), (4, 2),
            (5, 1), (5, 3), (5, 4)
        ]
        cursor.executemany('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', enrollments)
        
        conn.commit()
        
        print(f"✓ {len(courses)} courses inserted")
        print(f"✓ {len(students)} students inserted")
        print(f"✓ {len(enrollments)} enrollments inserted")
        print(f"✓ Database: {db_name}")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_setup()
