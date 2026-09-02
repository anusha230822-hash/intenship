"""
SQLite3 Practice - Part A Question 4: Display All Students
Executes: A_03_select_all_students.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db'):
    """Display all students"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part A - Question 4: Display All Students")
        print("=" * 70)
        
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        
        if students:
            print(f"\n{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
            print("-" * 70)
            for student in students:
                print(f"{student[0]:<5} {student[1]:<20} {student[2]:<10} {student[3]:<15}")
            print(f"\nTotal Records: {len(students)}")
        else:
            print("✗ No students found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
