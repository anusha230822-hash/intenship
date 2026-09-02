"""
SQLite3 Practice - Part A Question 8: Find Student by ID
Executes: A_07_select_by_id.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db', student_id=1):
    """Find student by ID"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print(f"Part A - Question 8: Find Student by ID ({student_id})")
        print("=" * 70)
        
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        student = cursor.fetchone()
        
        if student:
            print(f"\n{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
            print("-" * 70)
            print(f"{student[0]:<5} {student[1]:<20} {student[2]:<10} {student[3]:<15}")
        else:
            print(f"\n✗ Student with ID {student_id} not found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query(student_id=1)
