"""
SQLite3 Practice - Part B Question 3: Top 3 Students
Executes: B_04_top_3_students.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partB.db'):
    """Display top 3 students by marks"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part B - Question 3: Top 3 Students")
        print("=" * 70)
        
        cursor.execute('''
            SELECT name, marks FROM students_intermediate 
            ORDER BY marks DESC 
            LIMIT 3
        ''')
        
        students = cursor.fetchall()
        
        print(f"\n{'Rank':<6} {'Name':<20} {'Marks':<10}")
        print("-" * 70)
        
        if students:
            for rank, student in enumerate(students, 1):
                print(f"{rank}. {student[0]:<18} {student[1]:<10}")
        else:
            print("✗ No students found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
