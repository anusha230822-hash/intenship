"""
SQLite3 Practice - Part A Question 10: Delete Student
Executes: A_09_delete_student.sql
"""

import sqlite3
from sqlite3 import Error


def execute_query(db_name='college_partA.db', student_id=5):
    """Delete a student"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print(f"Part A - Question 10: Delete Student (ID={student_id})")
        print("=" * 70)
        
        # Get record before deletion
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        student = cursor.fetchone()
        
        if student:
            print(f"\n--- Before Deletion ---")
            print(f"{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
            print("-" * 70)
            print(f"{student[0]:<5} {student[1]:<20} {student[2]:<10} {student[3]:<15}")
            
            # Delete student
            cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            conn.commit()
            
            print(f"\n✓ Student with ID {student_id} deleted successfully!")
            
            # Show all remaining records
            cursor.execute('SELECT COUNT(*) FROM students')
            count = cursor.fetchone()[0]
            
            print(f"\n--- After Deletion ---")
            cursor.execute('SELECT * FROM students ORDER BY id')
            remaining = cursor.fetchall()
            
            print(f"{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15}")
            print("-" * 70)
            for rec in remaining:
                print(f"{rec[0]:<5} {rec[1]:<20} {rec[2]:<10} {rec[3]:<15}")
            
            print(f"\nTotal Remaining: {count} students")
        else:
            print(f"\n✗ Student with ID {student_id} not found")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_query(student_id=5)
