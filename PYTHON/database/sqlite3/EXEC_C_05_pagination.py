"""
SQLite3 Practice - Part C Question 8: Pagination
Using LIMIT and OFFSET
"""

import sqlite3
from sqlite3 import Error


def execute_pagination(db_name='college_partC.db', page=1, page_size=2):
    """Display paginated results"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print(f"Part C - Question 8: Pagination (Page {page}, Size {page_size})")
        print("=" * 70)
        
        offset = (page - 1) * page_size
        
        cursor.execute('''
            SELECT student_id, name, marks, gpa FROM students_advanced
            ORDER BY name
            LIMIT ? OFFSET ?
        ''', (page_size, offset))
        
        results = cursor.fetchall()
        
        print(f"\n{'ID':<5} {'Name':<20} {'Marks':<10} {'GPA':<10}")
        print("-" * 50)
        
        if results:
            for row in results:
                print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<10}")
        else:
            print("✗ No more results")
        
        # Show total count
        cursor.execute('SELECT COUNT(*) FROM students_advanced')
        total = cursor.fetchone()[0]
        total_pages = (total + page_size - 1) // page_size
        
        print(f"\nPage {page} of {total_pages} (Total: {total} students)")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    # Show multiple pages
    execute_pagination(page=1, page_size=2)
    print("\n" + "=" * 70 + "\n")
    execute_pagination(page=2, page_size=2)
    print("\n" + "=" * 70 + "\n")
    execute_pagination(page=3, page_size=2)
