"""
SQLite3 Practice - Part B Question 2: Order by Marks (Descending)
Executes: B_03_order_by_marks_desc.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partB.db'):
    """Display students ordered by marks descending"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part B - Question 2: Order by Marks (Descending)")
        print("=" * 70)
        
        cursor.execute('''
            SELECT name, marks, course FROM students_intermediate 
            ORDER BY marks DESC
        ''')
        
        students = cursor.fetchall()
        
        print(f"\n{'Name':<20} {'Marks':<10} {'Course':<15}")
        print("-" * 70)
        
        if students:
            for student in students:
                print(f"{student[0]:<20} {student[1]:<10} {student[2]:<15}")
            print(f"\nTotal: {len(students)} students")
        else:
            print("✗ No students found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
