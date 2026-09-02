"""
SQLite3 Practice - Part A Question 6: Display Students with Marks > 75
Executes: A_05_select_high_scorers.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db'):
    """Display high scorers"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part A - Question 6: Display Students with Marks > 75")
        print("=" * 70)
        
        cursor.execute('SELECT * FROM students WHERE marks > 75')
        students = cursor.fetchall()
        
        print(f"\n{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
        print("-" * 70)
        
        if students:
            for student in students:
                print(f"{student[0]:<5} {student[1]:<20} {student[2]:<10} {student[3]:<15}")
            print(f"\nTotal: {len(students)} students with marks > 75")
        else:
            print("✗ No students found with marks > 75")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
