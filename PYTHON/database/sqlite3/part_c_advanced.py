"""
SQLite3 Practice - Part C (Advanced)
This file contains advanced SQL operations including relationships, JOINs, and database class design
"""

import sqlite3
from sqlite3 import Error
from datetime import datetime


class AdvancedDatabase:
    """Advanced database operations with relationships and CRUD methods"""
    
    def __init__(self, db_name='college_advanced.db'):
        self.db_name = db_name
        self.conn = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row  # Return rows as dictionaries
            print("✓ Database connection established")
            return self.conn
        except Error as e:
            print(f"✗ Error: {e}")
            return None
    
    def create_tables(self):
        """Task 1: Create three tables with relationships"""
        cursor = self.conn.cursor()
        try:
            # Create courses table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT NOT NULL UNIQUE,
                    credits INTEGER NOT NULL
                )
            ''')
            
            # Create students table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    marks REAL NOT NULL,
                    gpa REAL
                )
            ''')
            
            # Create enrollments table (relationship/junction table)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS enrollments (
                    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    course_id INTEGER NOT NULL,
                    enrollment_date TEXT DEFAULT CURRENT_DATE,
                    FOREIGN KEY (student_id) REFERENCES students(student_id),
                    FOREIGN KEY (course_id) REFERENCES courses(course_id)
                )
            ''')
            
            self.conn.commit()
            print("✓ Task 1: Three tables with relationships created")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def clear_tables(self):
        """Clear all tables"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('DELETE FROM enrollments')
            cursor.execute('DELETE FROM students')
            cursor.execute('DELETE FROM courses')
            self.conn.commit()
        except Error as e:
            print(f"✗ Error: {e}")
    
    def insert_sample_data(self):
        """Insert sample data into all tables"""
        cursor = self.conn.cursor()
        try:
            # Insert courses
            courses = [
                ('Python', 3),
                ('Java', 3),
                ('C++', 4),
                ('Database Design', 3)
            ]
            cursor.executemany('INSERT INTO courses (course_name, credits) VALUES (?, ?)', courses)
            
            # Insert students
            students = [
                ('Alice Johnson', 92, 3.8),
                ('Bob Smith', 78, 3.2),
                ('Charlie Davis', 88, 3.6),
                ('Diana Wilson', 65, 2.8),
                ('Eve Brown', 95, 3.9),
                ('Frank Miller', 72, 3.0)
            ]
            cursor.executemany('INSERT INTO students (name, marks, gpa) VALUES (?, ?, ?)', students)
            
            # Insert enrollments
            enrollments = [
                (1, 1),  # Alice - Python
                (1, 4),  # Alice - Database Design
                (2, 2),  # Bob - Java
                (3, 1),  # Charlie - Python
                (3, 3),  # Charlie - C++
                (4, 2),  # Diana - Java
                (5, 1),  # Eve - Python
                (5, 3),  # Eve - C++
                (5, 4),  # Eve - Database Design
                # Frank is not enrolled in any course
            ]
            cursor.executemany('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', enrollments)
            
            self.conn.commit()
            print("✓ Sample data inserted into all tables")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def display_students_with_courses(self):
        """Task 3: Display student names with their course names using JOIN"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT s.name, c.course_name, c.credits
                FROM students s
                LEFT JOIN enrollments e ON s.student_id = e.student_id
                LEFT JOIN courses c ON e.course_id = c.course_id
                ORDER BY s.name
            ''')
            results = cursor.fetchall()
            print(f"\n--- Task 3: Students with Their Courses (JOIN) ---")
            for row in results:
                course_info = f"{row[1]} ({row[2]} credits)" if row[1] else "Not enrolled"
                print(f"  {row[0]}: {course_info}")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def find_unenrolled_students(self):
        """Task 4: Find students who are not enrolled in any course"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT s.student_id, s.name, s.marks
                FROM students s
                WHERE s.student_id NOT IN (SELECT student_id FROM enrollments)
            ''')
            results = cursor.fetchall()
            print(f"\n--- Task 4: Students Not Enrolled in Any Course ---")
            if results:
                for row in results:
                    print(f"  {row[1]} (ID: {row[0]}, Marks: {row[2]})")
            else:
                print(f"  No unenrolled students")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def count_students_per_course(self):
        """Task 5: Find the number of students in each course"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                SELECT c.course_name, COUNT(e.student_id) as student_count
                FROM courses c
                LEFT JOIN enrollments e ON c.course_id = e.course_id
                GROUP BY c.course_id, c.course_name
            ''')
            results = cursor.fetchall()
            print(f"\n--- Task 5: Number of Students per Course ---")
            for row in results:
                print(f"  {row[0]}: {row[1]} students")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def create_student_search_filter(self, min_marks=None, max_marks=None, gpa_min=None):
        """Task 7: Student search feature with multiple filters"""
        cursor = self.conn.cursor()
        try:
            query = 'SELECT * FROM students WHERE 1=1'
            params = []
            
            if min_marks is not None:
                query += ' AND marks >= ?'
                params.append(min_marks)
            if max_marks is not None:
                query += ' AND marks <= ?'
                params.append(max_marks)
            if gpa_min is not None:
                query += ' AND gpa >= ?'
                params.append(gpa_min)
            
            cursor.execute(query, params)
            results = cursor.fetchall()
            print(f"\n--- Task 7: Student Search with Filters ---")
            for row in results:
                print(f"  {row['name']}: Marks={row['marks']}, GPA={row['gpa']}")
            return results
        except Error as e:
            print(f"✗ Error: {e}")
            return []
    
    def display_with_pagination(self, page=1, page_size=2):
        """Task 8: Display students with pagination using LIMIT and OFFSET"""
        cursor = self.conn.cursor()
        try:
            offset = (page - 1) * page_size
            cursor.execute('''
                SELECT student_id, name, marks, gpa FROM students
                ORDER BY name
                LIMIT ? OFFSET ?
            ''', (page_size, offset))
            
            results = cursor.fetchall()
            print(f"\n--- Task 8: Pagination (Page {page}, Size {page_size}) ---")
            for row in results:
                print(f"  ID {row['student_id']}: {row['name']} - Marks: {row['marks']}, GPA: {row['gpa']}")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def create_index(self):
        """Task 9: Create indexes on frequently searched columns"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_student_name ON students(name)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_student_marks ON students(marks)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_enrollment_student ON enrollments(student_id)')
            self.conn.commit()
            print("✓ Task 9: Indexes created on frequently searched columns")
        except Error as e:
            print(f"✗ Error: {e}")
    
    def transaction_insert_multiple(self, students_data):
        """Task 10: Use SQLite transactions to insert multiple records safely"""
        cursor = self.conn.cursor()
        try:
            self.conn.execute('BEGIN TRANSACTION')
            cursor.executemany(
                'INSERT INTO students (name, marks, gpa) VALUES (?, ?, ?)',
                students_data
            )
            self.conn.commit()
            print(f"✓ Task 10: {cursor.rowcount} records inserted within transaction")
        except Error as e:
            self.conn.rollback()
            print(f"✗ Error: Transaction rolled back - {e}")
    
    # CRUD Methods for students
    def add_student(self, name, marks, gpa):
        """CREATE: Add a new student"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO students (name, marks, gpa) VALUES (?, ?, ?)',
                (name, marks, gpa)
            )
            self.conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"✗ Error: {e}")
            return None
    
    def read_student(self, student_id):
        """READ: Get student by ID"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"✗ Error: {e}")
            return None
    
    def update_student(self, student_id, name=None, marks=None, gpa=None):
        """UPDATE: Update student details"""
        cursor = self.conn.cursor()
        try:
            if name:
                cursor.execute('UPDATE students SET name = ? WHERE student_id = ?', (name, student_id))
            if marks is not None:
                cursor.execute('UPDATE students SET marks = ? WHERE student_id = ?', (marks, student_id))
            if gpa is not None:
                cursor.execute('UPDATE students SET gpa = ? WHERE student_id = ?', (gpa, student_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"✗ Error: {e}")
            return False
    
    def delete_student(self, student_id):
        """DELETE: Delete a student"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('DELETE FROM enrollments WHERE student_id = ?', (student_id,))
            cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"✗ Error: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print("\n✓ Database connection closed")


def main():
    """Main function to run advanced operations"""
    print("=" * 70)
    print("SQLite3 - Part C (Advanced) Practice - Relationships & CRUD")
    print("=" * 70)
    
    db = AdvancedDatabase()
    db.connect()
    db.create_tables()
    db.clear_tables()
    db.insert_sample_data()
    db.create_index()
    
    # Task 3: Display students with courses
    db.display_students_with_courses()
    
    # Task 4: Find unenrolled students
    db.find_unenrolled_students()
    
    # Task 5: Count students per course
    db.count_students_per_course()
    
    # Task 7: Search with filters
    print(f"\n--- Task 7: Search - Students with marks >= 80 and GPA >= 3.5 ---")
    db.create_student_search_filter(min_marks=80, gpa_min=3.5)
    
    # Task 8: Pagination
    for page in range(1, 3):
        db.display_with_pagination(page=page, page_size=2)
    
    # Task 10: Transaction with multiple inserts
    print(f"\n--- Task 10: Transaction with Multiple Inserts ---")
    new_students = [
        ('George King', 88, 3.7),
        ('Helen White', 91, 3.8)
    ]
    db.transaction_insert_multiple(new_students)
    
    # Demonstrate CRUD operations
    print(f"\n--- CRUD Operations Demo ---")
    
    # CREATE
    new_id = db.add_student('Ivy Johnson', 89, 3.7)
    print(f"✓ Student added with ID: {new_id}")
    
    # READ
    student = db.read_student(new_id)
    print(f"✓ Read: {student['name']} - Marks: {student['marks']}")
    
    # UPDATE
    success = db.update_student(new_id, marks=92)
    print(f"✓ Updated: Student {new_id} marks updated" if success else "✗ Update failed")
    
    # DELETE
    success = db.delete_student(new_id)
    print(f"✓ Deleted: Student {new_id}" if success else "✗ Delete failed")
    
    db.close()


if __name__ == "__main__":
    main()
