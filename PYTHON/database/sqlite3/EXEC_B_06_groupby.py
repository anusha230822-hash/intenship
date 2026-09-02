"""
SQLite3 Practice - Part B Questions 7-8: GROUP BY Operations
Count and Average by Course
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partB.db'):
    """Display GROUP BY statistics"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part B - Questions 7-8: GROUP BY (Course-wise Statistics)")
        print("=" * 70)
        
        # Question 7: Count by course
        print("\n--- Question 7: Count Students by Course ---")
        cursor.execute('''
            SELECT course, COUNT(*) as student_count 
            FROM students_intermediate 
            GROUP BY course
        ''')
        
        course_counts = cursor.fetchall()
        print(f"\n{'Course':<15} {'Student Count':<15}")
        print("-" * 35)
        
        for row in course_counts:
            print(f"{row[0]:<15} {row[1]:<15}")
        
        # Question 8: Average by course
        print("\n--- Question 8: Average Marks by Course ---")
        cursor.execute('''
            SELECT course, AVG(marks) as average_marks 
            FROM students_intermediate 
            GROUP BY course
        ''')
        
        course_avgs = cursor.fetchall()
        print(f"\n{'Course':<15} {'Average Marks':<15}")
        print("-" * 35)
        
        for row in course_avgs:
            print(f"{row[0]:<15} {row[1]:<15.2f}")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
