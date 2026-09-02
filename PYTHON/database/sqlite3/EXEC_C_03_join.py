"""
SQLite3 Practice - Part C Question 3: JOIN - Students with Courses
Executes: C_03_join_students_courses.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partC.db'):
    """Display students with their courses using JOIN"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 80)
        print("Part C - Question 3: JOIN - Students with Their Courses")
        print("=" * 80)
        
        cursor.execute('''
            SELECT 
                s.name, 
                c.course_name, 
                c.credits
            FROM students_advanced s
            LEFT JOIN enrollments e ON s.student_id = e.student_id
            LEFT JOIN courses c ON e.course_id = c.course_id
            ORDER BY s.name
        ''')
        
        results = cursor.fetchall()
        
        print(f"\n{'Student Name':<20} {'Course Name':<20} {'Credits':<10}")
        print("-" * 80)
        
        if results:
            for row in results:
                course = row[1] if row[1] else "(Not enrolled)"
                credits = row[2] if row[2] else "-"
                print(f"{row[0]:<20} {str(course):<20} {str(credits):<10}")
            print(f"\nTotal rows: {len(results)}")
        else:
            print("✗ No data found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
