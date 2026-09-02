"""
SQLite3 Practice - Part B Question 14: Transactions
Demonstrate COMMIT and ROLLBACK
"""

import sqlite3
from sqlite3 import Error


def execute_transactions(db_name='college_partB.db'):
    """Demonstrate transaction operations"""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print("=" * 70)
        print("Part B - Question 14: Transactions (COMMIT & ROLLBACK)")
        print("=" * 70)
        
        # Show current count
        cursor.execute('SELECT COUNT(*) FROM students_intermediate')
        initial_count = cursor.fetchone()[0]
        print(f"\n--- Initial Count: {initial_count} students ---")
        
        # Transaction 1: Successful INSERT (COMMIT)
        print("\n--- Transaction 1: Successful INSERT (COMMIT) ---")
        try:
            cursor.execute('BEGIN TRANSACTION')
            cursor.execute('''
                INSERT INTO students_intermediate (name, marks, course) 
                VALUES (?, ?, ?)
            ''', ('Kevin Chen', 89, 'Python'))
            cursor.execute('''
                INSERT INTO students_intermediate (name, marks, course) 
                VALUES (?, ?, ?)
            ''', ('Lisa Adams', 94, 'Java'))
            conn.commit()
            print("✓ Transaction committed successfully")
        except Error as e:
            conn.rollback()
            print(f"✗ Transaction rolled back: {e}")
        
        # Transaction 2: Failed UPDATE (ROLLBACK)
        print("\n--- Transaction 2: Failed UPDATE (ROLLBACK) ---")
        try:
            cursor.execute('BEGIN TRANSACTION')
            cursor.execute('''
                UPDATE students_intermediate SET marks = 150 WHERE id = 1
            ''')  # Invalid: marks > 100
            # Simulate error - marks exceed valid range
            print("✗ Invalid marks detected - rolling back")
            conn.rollback()
            print("✓ Transaction rolled back successfully")
        except Error as e:
            conn.rollback()
            print(f"✗ Error: {e}")
        
        # Show final count
        cursor.execute('SELECT COUNT(*) FROM students_intermediate')
        final_count = cursor.fetchone()[0]
        print(f"\n--- Final Count: {final_count} students ---")
        print(f"Records added: {final_count - initial_count}")
        
        conn.close()
        
    except Error as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    execute_transactions()
