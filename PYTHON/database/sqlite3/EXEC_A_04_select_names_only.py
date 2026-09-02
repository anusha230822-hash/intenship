"""
SQLite3 Practice - Part A Question 5: Display Only Student Names
Executes: A_04_select_names_only.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db'):
    """Display only student names"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 60)
        print("Part A - Question 5: Display Only Student Names")
        print("=" * 60)
        
        cursor.execute('SELECT name FROM students')
        names = cursor.fetchall()
        
        print(f"\n{'Name':<25}")
        print("-" * 25)
        
        if names:
            for i, name in enumerate(names, 1):
                print(f"{i}. {name[0]}")
            print(f"\nTotal: {len(names)} students")
        else:
            print("✗ No students found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
