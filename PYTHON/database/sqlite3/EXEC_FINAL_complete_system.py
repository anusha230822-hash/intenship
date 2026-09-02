"""
SQLite3 Final Challenge - Complete Student Management System
Menu-driven application with all CRUD operations
"""

import sqlite3
from sqlite3 import Error


class StudentManagementSystem:
    """Complete Student Management System using SQLite3"""
    
    def __init__(self, db_name='student_management.db'):
        self.db_name = db_name
        self.conn = None
        self.initialize()
    
    def initialize(self):
        """Initialize database and create table"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row
            cursor = self.conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    marks REAL NOT NULL CHECK(marks >= 0 AND marks <= 100),
                    course TEXT NOT NULL,
                    enrollment_date TEXT DEFAULT CURRENT_DATE
                )
            ''')
            self.conn.commit()
        except Error as e:
            print(f"✗ Error: {e}")
    
    def add_student(self, name, marks, course):
        """Menu Option 1: Add Student"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, marks, course)
                VALUES (?, ?, ?)
            ''', (name, marks, course))
            self.conn.commit()
            return f"✓ Student '{name}' added (ID: {cursor.lastrowid})"
        except Error as e:
            self.conn.rollback()
            return f"✗ Error: {e}"
    
    def view_all_students(self):
        """Menu Option 2: View All Students"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM students ORDER BY name')
            return cursor.fetchall()
        except Error as e:
            return f"✗ Error: {e}"
    
    def search_student(self, search_type, search_value):
        """Menu Option 3: Search Student"""
        try:
            cursor = self.conn.cursor()
            
            if search_type == 'id':
                cursor.execute('SELECT * FROM students WHERE student_id = ?', (search_value,))
            elif search_type == 'name':
                cursor.execute('SELECT * FROM students WHERE name LIKE ?', (f"%{search_value}%",))
            elif search_type == 'course':
                cursor.execute('SELECT * FROM students WHERE course = ?', (search_value,))
            
            return cursor.fetchall()
        except Error as e:
            return f"✗ Error: {e}"
    
    def update_student(self, student_id, name=None, marks=None, course=None):
        """Menu Option 4: Update Student"""
        try:
            cursor = self.conn.cursor()
            
            if name:
                cursor.execute('UPDATE students SET name = ? WHERE student_id = ?', (name, student_id))
            if marks is not None:
                cursor.execute('UPDATE students SET marks = ? WHERE student_id = ?', (marks, student_id))
            if course:
                cursor.execute('UPDATE students SET course = ? WHERE student_id = ?', (course, student_id))
            
            self.conn.commit()
            return f"✓ Student {student_id} updated"
        except Error as e:
            self.conn.rollback()
            return f"✗ Error: {e}"
    
    def delete_student(self, student_id):
        """Menu Option 5: Delete Student"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
            self.conn.commit()
            return f"✓ Student {student_id} deleted"
        except Error as e:
            self.conn.rollback()
            return f"✗ Error: {e}"
    
    def show_top_students(self, limit=5):
        """Menu Option 6: Show Top Students"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT * FROM students
                ORDER BY marks DESC
                LIMIT ?
            ''', (limit,))
            return cursor.fetchall()
        except Error as e:
            return f"✗ Error: {e}"
    
    def course_statistics(self):
        """Menu Option 7: Course-wise Statistics"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT 
                    course,
                    COUNT(*) as count,
                    ROUND(AVG(marks), 2) as avg_marks,
                    MAX(marks) as max_marks,
                    MIN(marks) as min_marks
                FROM students
                GROUP BY course
                ORDER BY course
            ''')
            return cursor.fetchall()
        except Error as e:
            return f"✗ Error: {e}"
    
    def average_marks(self):
        """Menu Option 8: Average Marks"""
        try:
            cursor = self.conn.cursor()
            
            # Overall average
            cursor.execute('SELECT ROUND(AVG(marks), 2) FROM students')
            overall_avg = cursor.fetchone()[0]
            
            # By course
            cursor.execute('''
                SELECT course, ROUND(AVG(marks), 2)
                FROM students
                GROUP BY course
                ORDER BY course
            ''')
            by_course = cursor.fetchall()
            
            return overall_avg, by_course
        except Error as e:
            return f"✗ Error: {e}"
    
    def student_count(self):
        """Menu Option 9: Student Count"""
        try:
            cursor = self.conn.cursor()
            
            # Total
            cursor.execute('SELECT COUNT(*) FROM students')
            total = cursor.fetchone()[0]
            
            # By course
            cursor.execute('''
                SELECT course, COUNT(*)
                FROM students
                GROUP BY course
                ORDER BY course
            ''')
            by_course = cursor.fetchall()
            
            return total, by_course
        except Error as e:
            return f"✗ Error: {e}"
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()


def display_students_table(students):
    """Helper function to display students in table format"""
    if isinstance(students, str):  # Error message
        print(students)
        return
    
    if not students:
        print("✗ No students found")
        return
    
    print(f"\n{'ID':<5} {'Name':<20} {'Marks':<10} {'Course':<15} {'Date':<12}")
    print("-" * 70)
    
    for student in students:
        print(f"{student['student_id']:<5} {student['name']:<20} {student['marks']:<10} {student['course']:<15} {student['enrollment_date']:<12}")


def main():
    """Main menu-driven application"""
    system = StudentManagementSystem()
    
    print("\n" + "*" * 70)
    print("STUDENT MANAGEMENT SYSTEM - Python Version")
    print("*" * 70)
    
    # Demo: Add some students
    print("\n--- Demo: Adding Students ---")
    print(system.add_student('Alice Johnson', 92.0, 'Python'))
    print(system.add_student('Bob Smith', 78.5, 'Java'))
    print(system.add_student('Charlie Davis', 88.0, 'C++'))
    
    # Demo: View all
    print("\n--- Demo: View All Students ---")
    display_students_table(system.view_all_students())
    
    # Demo: Top students
    print("\n--- Demo: Top Students ---")
    top = system.show_top_students(limit=2)
    display_students_table(top)
    
    # Demo: Course statistics
    print("\n--- Demo: Course Statistics ---")
    stats = system.course_statistics()
    if isinstance(stats, str):  # Error
        print(stats)
    else:
        print(f"\n{'Course':<15} {'Count':<8} {'Avg':<8} {'Max':<8} {'Min':<8}")
        print("-" * 50)
        for row in stats:
            print(f"{row['course']:<15} {row['count']:<8} {row['avg_marks']:<8} {row['max_marks']:<8} {row['min_marks']:<8}")
    
    # Demo: Average marks
    print("\n--- Demo: Average Marks ---")
    avg, by_course = system.average_marks()
    if isinstance(avg, str):  # Error
        print(avg)
    else:
        print(f"Overall Average: {avg}")
        print("\nBy Course:")
        for course, avg_val in by_course:
            print(f"  {course}: {avg_val}")
    
    # Demo: Student count
    print("\n--- Demo: Student Count ---")
    total, by_course = system.student_count()
    if isinstance(total, str):  # Error
        print(total)
    else:
        print(f"Total Students: {total}")
        print("\nBy Course:")
        for course, count in by_course:
            print(f"  {course}: {count}")
    
    print("\n" + "*" * 70)
    print("✓ Demo completed successfully!")
    print("*" * 70 + "\n")
    
    system.close()


if __name__ == "__main__":
    main()
