"""
SQLite3 Practice - Part B Question 1: Create and Insert 10 Students
Setup for Part B exercises
"""

import sqlite3
from sqlite3 import Error


def execute_setup(db_name='college_partB.db'):
    """Create table and insert 10 students"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part B - Setup: Create Table and Insert 10 Students")
        print("=" * 70)
        
        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students_intermediate (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                marks REAL NOT NULL,
                course TEXT NOT NULL
            )
        ''')
        
        # Insert 10 students
        students = [
            ('Alice Johnson', 92, 'Python'),
            ('Bob Smith', 78, 'Java'),
            ('Charlie Davis', 88, 'Python'),
            ('Diana Wilson', 65, 'C++'),
            ('Eve Brown', 95, 'Python'),
            ('Frank Miller', 72, 'Java'),
            ('Grace Lee', 85, 'C++'),
            ('Henry Taylor', 91, 'Python'),
            ('Iris Martin', 68, 'Java'),
            ('Jack Anderson', 87, 'C++')
        ]
        
        cursor.executemany('''
            INSERT INTO students_intermediate (name, marks, course) VALUES (?, ?, ?)
        ''', students)
        
        conn.commit()
        
        print(f"\n✓ Table created successfully")
        print(f"✓ {cursor.rowcount} students inserted")
        print(f"✓ Database: {db_name}\n")
        
        # Display all
        cursor.execute('SELECT * FROM students_intermediate')
        all_students = cursor.fetchall()
        
        print(f"{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
        print("-" * 70)
        for student in all_students:
            print(f"{student[0]:<5} {student[1]:<20} {student[2]:<10} {student[3]:<15}")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_setup()
