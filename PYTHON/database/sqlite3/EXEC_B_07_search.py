"""
SQLite3 Practice - Part B Questions 9-10: Search Operations
LIKE pattern matching and BETWEEN range queries
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partB.db'):
    """Display search results"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part B - Questions 9-10: Search Operations (LIKE & BETWEEN)")
        print("=" * 70)
        
        # Question 9: Names starting with 'A'
        print("\n--- Question 9: Students with Names Starting with 'A' ---")
        cursor.execute('''
            SELECT name, marks FROM students_intermediate 
            WHERE name LIKE 'A%' 
            ORDER BY name
        ''')
        
        names_a = cursor.fetchall()
        
        if names_a:
            print(f"\n{'Name':<20} {'Marks':<10}")
            print("-" * 35)
            for row in names_a:
                print(f"{row[0]:<20} {row[1]:<10}")
        else:
            print("✗ No students found with names starting with 'A'")
        
        # Question 10: Marks between 60-90
        print("\n--- Question 10: Students with Marks Between 60-90 ---")
        cursor.execute('''
            SELECT name, marks, course FROM students_intermediate 
            WHERE marks BETWEEN 60 AND 90 
            ORDER BY marks DESC
        ''')
        
        marks_range = cursor.fetchall()
        
        print(f"\n{'Name':<20} {'Marks':<10} {'Course':<15}")
        print("-" * 50)
        
        if marks_range:
            for row in marks_range:
                print(f"{row[0]:<20} {row[1]:<10} {row[2]:<15}")
            print(f"\nTotal: {len(marks_range)} students")
        else:
            print("✗ No students found in marks range 60-90")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
