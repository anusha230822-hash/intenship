"""
SQLite3 Practice - Part A Question 9: Update Student Marks
Executes: A_08_update_marks.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db', student_id=2, new_marks=80.5):
    """Update student marks"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print(f"Part A - Question 9: Update Student Marks (ID={student_id})")
        print("=" * 70)
        
        # Get old record
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        old_student = cursor.fetchone()
        
        if old_student:
            print(f"\n--- Before Update ---")
            print(f"{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
            print("-" * 70)
            print(f"{old_student[0]:<5} {old_student[1]:<20} {old_student[2]:<10} {old_student[3]:<15}")
            
            # Update marks
            cursor.execute('UPDATE students SET marks = ? WHERE id = ?', (new_marks, student_id))
            conn.commit()
            
            print(f"\n✓ Updated marks to {new_marks}")
            
            # Get new record
            cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
            new_student = cursor.fetchone()
            
            print(f"\n--- After Update ---")
            print(f"{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
            print("-" * 70)
            print(f"{new_student[0]:<5} {new_student[1]:<20} {new_student[2]:<10} {new_student[3]:<15}")
        else:
            print(f"\n✗ Student with ID {student_id} not found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query(student_id=2, new_marks=80.5)
