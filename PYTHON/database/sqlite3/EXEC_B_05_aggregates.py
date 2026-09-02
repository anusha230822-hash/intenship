"""
SQLite3 Practice - Part B Questions 4-6: Aggregate Functions
COUNT, AVG, MAX, MIN
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partB.db'):
    """Display aggregate statistics"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part B - Questions 4-6: Aggregate Functions (COUNT, AVG, MAX, MIN)")
        print("=" * 70)
        
        # Question 4: Count
        cursor.execute('SELECT COUNT(*) as total_students FROM students_intermediate')
        count_result = cursor.fetchone()
        
        # Question 5: Average
        cursor.execute('SELECT AVG(marks) as average_marks FROM students_intermediate')
        avg_result = cursor.fetchone()
        
        # Question 6: Max and Min
        cursor.execute('SELECT MAX(marks) as highest, MIN(marks) as lowest FROM students_intermediate')
        maxmin_result = cursor.fetchone()
        
        print("\n--- Question 4: Total Students (COUNT) ---")
        print(f"Total Students: {count_result[0]}")
        
        print("\n--- Question 5: Average Marks (AVG) ---")
        print(f"Average Marks: {avg_result[0]:.2f}")
        
        print("\n--- Question 6: Highest & Lowest Marks ---")
        print(f"Highest Marks: {maxmin_result[0]}")
        print(f"Lowest Marks: {maxmin_result[1]}")
        print(f"Range: {maxmin_result[0] - maxmin_result[1]}")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
