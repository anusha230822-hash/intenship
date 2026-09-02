"""
SQLite3 Practice - Part C Questions 4-5: Subqueries and Aggregations
Unenrolled students and count per course
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partC.db'):
    """Display advanced queries"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part C - Questions 4-5: Subqueries & GROUP BY with JOINs")
        print("=" * 70)
        
        # Question 4: Unenrolled students
        print("\n--- Question 4: Students Not Enrolled in Any Course ---")
        cursor.execute('''
            SELECT 
                s.student_id, 
                s.name, 
                s.marks
            FROM students_advanced s
            WHERE s.student_id NOT IN (SELECT student_id FROM enrollments)
        ''')
        
        unenrolled = cursor.fetchall()
        
        if unenrolled:
            print(f"\n{'ID':<5} {'Name':<20} {'Marks':<10}")
            print("-" * 40)
            for row in unenrolled:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10}")
        else:
            print("\n✓ All students are enrolled in at least one course")
        
        # Question 5: Count per course
        print("\n--- Question 5: Number of Students per Course ---")
        cursor.execute('''
            SELECT 
                c.course_name, 
                COUNT(e.student_id) as student_count
            FROM courses c
            LEFT JOIN enrollments e ON c.course_id = e.course_id
            GROUP BY c.course_id, c.course_name
        ''')
        
        course_counts = cursor.fetchall()
        
        print(f"\n{'Course Name':<20} {'Student Count':<15}")
        print("-" * 40)
        
        if course_counts:
            for row in course_counts:
                print(f"{row[0]:<20} {row[1]:<15}")
        else:
            print("✗ No courses found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
