"""
SQLite3 Practice - Part B (Intermediate)
This file contains intermediate SQL operations including aggregations, GROUP BY, and transactions
"""

import sqlite3
from sqlite3 import Error


class IntermediateDatabase:
    """Intermediate database operations class"""
    
    def __init__(self, db_name='college_intermediate.db'):
        self.db_name = db_name
        self.conn = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            print("✓ Database connection established")
            return self.conn
        except Error as e:
            print(f"✗ Error: {e}")
            return None
    
    def create_table(self):
        """Create students table"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    marks REAL NOT NULL,
                    course TEXT NOT NULL
                )
            ''')
            self.conn.commit()
            print("✓ Table created successfully")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def clear_table(self):
        """Clear all records from students table"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('DELETE FROM students')
            self.conn.commit()
            print("✓ Table cleared")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def insert_10_students(self):
        """Task 1: Insert 10 students using executemany()"""
        cursor = self.conn.cursor()
        students = [
            ('Alice Johnson', 92, 'Python'),
            ('Bob Smith', 78, 'Java'),
            ('Charlie Davis', 88, 'Python'),
            ('Diana Wilson', 65, 'C++'),
            ('Eve Brown', 95, 'Python'),
            ('Frank Miller', 72, 'Java'),
            ('Grace Lee', 85, 'C++'),
            ('Henry Taylor', 91, 'Python'),
            ('Iris Martin', 68, 'Java'),
            ('Jack Anderson', 87, 'C++')
        ]
        
        try:
            cursor.executemany('''
                INSERT INTO students (name, marks, course)
                VALUES (?, ?, ?)
            ''', students)
            self.conn.commit()
            print(f"✓ Task 1: {cursor.rowcount} students inserted using executemany()")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def display_descending_marks(self):
        """Task 2: Display students in descending order of marks"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT name, marks, course FROM students ORDER BY marks DESC')
            students = cursor.fetchall()
            print("\n--- Task 2: Students by Marks (Descending) ---")
            for student in students:
                print(f"  {student[0]}: {student[1]} marks ({student[2]})")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def display_top_3_students(self):
        """Task 3: Display the top 3 students"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT name, marks FROM students ORDER BY marks DESC LIMIT 3')
            students = cursor.fetchall()
            print("\n--- Task 3: Top 3 Students ---")
            for i, student in enumerate(students, 1):
                print(f"  {i}. {student[0]}: {student[1]} marks")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def count_total_students(self):
        """Task 4: Find the total number of students using COUNT()"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT COUNT(*) FROM students')
            count = cursor.fetchone()[0]
            print(f"\n--- Task 4: Total Students ---")
            print(f"  Total count: {count}")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def average_marks(self):
        """Task 5: Find the average marks using AVG()"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT AVG(marks) FROM students')
            avg = cursor.fetchone()[0]
            print(f"\n--- Task 5: Average Marks ---")
            print(f"  Average: {avg:.2f}")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def highest_lowest_marks(self):
        """Task 6: Find the highest and lowest marks"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT MAX(marks), MIN(marks) FROM students')
            result = cursor.fetchone()
            print(f"\n--- Task 6: Highest & Lowest Marks ---")
            print(f"  Highest: {result[0]}")
            print(f"  Lowest: {result[1]}")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def count_course_wise(self):
        """Task 7: Count students course-wise using GROUP BY"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT course, COUNT(*) FROM students GROUP BY course')
            results = cursor.fetchall()
            print(f"\n--- Task 7: Students Count by Course (GROUP BY) ---")
            for course, count in results:
                print(f"  {course}: {count} students")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def average_marks_per_course(self):
        """Task 8: Find the average marks for each course"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT course, AVG(marks) FROM students GROUP BY course')
            results = cursor.fetchall()
            print(f"\n--- Task 8: Average Marks per Course ---")
            for course, avg in results:
                print(f"  {course}: {avg:.2f}")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def search_names_starting_with(self, letter):
        """Task 9: Search students whose names start with a specific letter"""
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT name, marks FROM students WHERE name LIKE ? ORDER BY name", 
                         (f"{letter}%",))
            students = cursor.fetchall()
            print(f"\n--- Task 9: Students with Names Starting with '{letter}' ---")
            if students:
                for student in students:
                    print(f"  {student[0]}: {student[1]} marks")
            else:
                print(f"  No students found")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def search_marks_between(self, min_marks, max_marks):
        """Task 10: Search students whose marks are between specified values"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT name, marks, course FROM students 
                WHERE marks BETWEEN ? AND ? 
                ORDER BY marks DESC
            ''', (min_marks, max_marks))
            students = cursor.fetchall()
            print(f"\n--- Task 10: Students with Marks between {min_marks}-{max_marks} ---")
            if students:
                for student in students:
                    print(f"  {student[0]}: {student[1]} marks ({student[2]})")
            else:
                print(f"  No students found")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def update_with_transaction(self, student_id, new_marks):
        """Task 14: Implement commit() and rollback() with transaction"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('UPDATE students SET marks = ? WHERE id = ?', (new_marks, student_id))
            if new_marks < 0 or new_marks > 100:
                self.conn.rollback()
                print(f"✗ Invalid marks! Transaction rolled back.")
            else:
                self.conn.commit()
                print(f"✓ Student {student_id} marks updated to {new_marks} (committed)")
        except Error as e:
            self.conn.rollback()
            print(f"✗ Error: {e} (rolled back)")
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print("\n✓ Database connection closed")


def main():
    """Main function to run intermediate operations"""
    print("=" * 60)
    print("SQLite3 - Part B (Intermediate) Practice")
    print("=" * 60)
    
    db = IntermediateDatabase()
    db.connect()
    db.create_table()
    db.clear_table()
    
    # Task 1: Insert 10 students
    db.insert_10_students()
    
    # Task 2: Display in descending order
    db.display_descending_marks()
    
    # Task 3: Top 3 students
    db.display_top_3_students()
    
    # Task 4: Count total students
    db.count_total_students()
    
    # Task 5: Average marks
    db.average_marks()
    
    # Task 6: Highest and lowest marks
    db.highest_lowest_marks()
    
    # Task 7: Count course-wise
    db.count_course_wise()
    
    # Task 8: Average marks per course
    db.average_marks_per_course()
    
    # Task 9: Search names starting with "A"
    db.search_names_starting_with("A")
    
    # Task 10: Search marks between 60 and 90
    db.search_marks_between(60, 90)
    
    # Task 14: Transaction with commit/rollback
    print(f"\n--- Task 14: Transaction Operations ---")
    db.update_with_transaction(1, 95)  # Valid update
    db.update_with_transaction(2, 150)  # Invalid update - will rollback
    
    db.close()


if __name__ == "__main__":
    main()
