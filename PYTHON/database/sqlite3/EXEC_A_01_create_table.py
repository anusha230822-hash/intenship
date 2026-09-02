"""
SQLite3 Practice - Part A Question 1: Create Students Table
Executes: A_01_create_table.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db'):
    """Create students table"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 60)
        print("Part A - Question 1: Create Students Table")
        print("=" * 60)
        
        # Execute the CREATE TABLE query
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                marks REAL NOT NULL,
                course TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        print("\n✓ Table 'students' created successfully!")
        print(f"✓ Database: {db_name}")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query()
