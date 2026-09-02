"""
SQLite3 Practice - Part A Question 2-3: Insert 5 Student Records
Executes: A_02_insert_5_students.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db'):
    """Insert 5 student records"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 60)
        print("Part A - Question 2-3: Insert 5 Student Records")
        print("=" * 60)
        
        # Insert data
        students = [
            ('Alice Johnson', 85.5, 'Python'),
            ('Bob Smith', 72.0, 'Java'),
            ('Charlie Davis', 91.0, 'Python'),
            ('Diana Wilson', 68.5, 'C++'),
            ('Eve Brown', 78.5, 'Java')
        ]
        
        cursor.executemany('''
            INSERT INTO students (name, marks, course) VALUES (?, ?, ?)
        ''', students)
        
        conn.commit()
        
        print(f"\n✓ {cursor.rowcount} student records inserted successfully!")
        print(f"✓ Database: {db_name}\n")
        
        # Verify count
        cursor.execute('SELECT COUNT(*) FROM students')
        count = cursor.fetchone()[0]
        print(f"Verification: Total students = {count}")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
