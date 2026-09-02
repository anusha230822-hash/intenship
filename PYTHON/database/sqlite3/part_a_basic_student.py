"""
SQLite3 Practice - Part A (Basic) - Student Version
This file contains basic SQL operations for beginners
"""

import sqlite3
from sqlite3 import Error


def create_database():
    """Create and return a connection to the college.db database"""
    try:
        conn = sqlite3.connect('college.db')
        print("✓ Database connection established")
        return conn
    except Error as e:
        print(f"✗ Error connecting to database: {e}")
        return None


def create_table(conn):
    """Create a students table with id, name, marks, and course"""
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                marks REAL NOT NULL,
                course TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("✓ Table 'students' created successfully")
    except Error as e:
        print(f"✗ Error creating table: {e}")


def insert_students(conn):
    """Insert 5 student records"""
    cursor = conn.cursor()
    students = [
        ('Alice Johnson', 85.5, 'Python'),
        ('Bob Smith', 72.0, 'Java'),
        ('Charlie Davis', 91.0, 'Python'),
        ('Diana Wilson', 68.5, 'C++'),
        ('Eve Brown', 78.5, 'Java')
    ]
    
    try:
        cursor.executemany('''
            INSERT INTO students (name, marks, course)
            VALUES (?, ?, ?)
        ''', students)
        conn.commit()
        print(f"✓ {cursor.rowcount} student records inserted successfully")
    except Error as e:
        print(f"✗ Error inserting records: {e}")


def display_all_students(conn):
    """Task 4: Display all students"""
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        print("\n--- All Students ---")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}, Course: {student[3]}")
    except Error as e:
        print(f"✗ Error: {e}")


def display_student_names(conn):
    """Task 5: Display only student names"""
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT name FROM students')
        names = cursor.fetchall()
        print("\n--- Student Names ---")
        for name in names:
            print(f"• {name[0]}")
    except Error as e:
        print(f"✗ Error: {e}")


def display_high_scorers(conn):
    """Task 6: Display students who scored more than 75 marks"""
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM students WHERE marks > 75')
        students = cursor.fetchall()
        print("\n--- Students with Marks > 75 ---")
        for student in students:
            print(f"{student[1]}: {student[2]} marks ({student[3]})")
    except Error as e:
        print(f"✗ Error: {e}")


def display_python_course_students(conn):
    """Task 7: Find students belonging to the Python course"""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE course = 'Python'")
        students = cursor.fetchall()
        print("\n--- Python Course Students ---")
        for student in students:
            print(f"{student[1]}: {student[2]} marks")
    except Error as e:
        print(f"✗ Error: {e}")


def find_student_by_id(conn, student_id):
    """Task 8: Find the student with a particular ID"""
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        student = cursor.fetchone()
        if student:
            print(f"\n--- Student Details ---")
            print(f"ID: {student[0]}\nName: {student[1]}\nMarks: {student[2]}\nCourse: {student[3]}")
        else:
            print(f"✗ Student with ID {student_id} not found")
    except Error as e:
        print(f"✗ Error: {e}")


def update_student_marks(conn, student_id, new_marks):
    """Task 9: Update the marks of one student"""
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE students SET marks = ? WHERE id = ?', (new_marks, student_id))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"✓ Student {student_id} marks updated to {new_marks}")
        else:
            print(f"✗ Student with ID {student_id} not found")
    except Error as e:
        print(f"✗ Error: {e}")


def delete_student(conn, student_id):
    """Task 10: Delete one student"""
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"✓ Student {student_id} deleted successfully")
        else:
            print(f"✗ Student with ID {student_id} not found")
    except Error as e:
        print(f"✗ Error: {e}")


def main():
    """Main function to run all basic operations"""
    print("=" * 50)
    print("SQLite3 - Part A (Basic) Practice")
    print("=" * 50)
    
    # Task 1: Create database
    conn = create_database()
    if conn is None:
        return
    
    # Task 2-3: Create table and insert students
    create_table(conn)
    insert_students(conn)
    
    # Task 4: Display all students
    display_all_students(conn)
    
    # Task 5: Display only names
    display_student_names(conn)
    
    # Task 6: Display high scorers
    display_high_scorers(conn)
    
    # Task 7: Display Python students
    display_python_course_students(conn)
    
    # Task 8: Find student by ID
    find_student_by_id(conn, 1)
    
    # Task 9: Update marks
    update_student_marks(conn, 2, 85.0)
    
    # Display updated records
    print("\n--- Updated Records ---")
    display_all_students(conn)
    
    # Task 10: Delete student
    delete_student(conn, 5)
    
    # Display final records
    print("\n--- Final Records ---")
    display_all_students(conn)
    
    # Close connection
    conn.close()
    print("\n✓ Database connection closed")


if __name__ == "__main__":
    main()
