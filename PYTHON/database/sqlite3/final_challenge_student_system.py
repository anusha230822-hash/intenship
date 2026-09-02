"""
SQLite3 Final Challenge - Student Management System
Complete menu-driven application with CRUD operations, exception handling, and transactions
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
        """Initialize database connection and create tables"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row
            print("✓ Database initialized successfully\n")
            self.create_table()
        except Error as e:
            print(f"✗ Database Error: {e}\n")
    
    def create_table(self):
        """Create students table"""
        cursor = self.conn.cursor()
        try:
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
            print(f"✗ Error creating table: {e}")
    
    def add_student(self):
        """Add a new student to the database"""
        print("\n" + "="*50)
        print("ADD STUDENT")
        print("="*50)
        
        try:
            name = input("Enter student name: ").strip()
            if not name:
                print("✗ Name cannot be empty!")
                return
            
            # Parameterized input for marks
            try:
                marks = float(input("Enter marks (0-100): "))
                if marks < 0 or marks > 100:
                    print("✗ Marks must be between 0 and 100!")
                    return
            except ValueError:
                print("✗ Invalid marks! Please enter a number.")
                return
            
            course = input("Enter course name: ").strip()
            if not course:
                print("✗ Course cannot be empty!")
                return
            
            cursor = self.conn.cursor()
            # Using parameterized query to prevent SQL injection
            cursor.execute('''
                INSERT INTO students (name, marks, course)
                VALUES (?, ?, ?)
            ''', (name, marks, course))
            
            self.conn.commit()
            print(f"✓ Student '{name}' added successfully! (ID: {cursor.lastrowid})")
        
        except Error as e:
            self.conn.rollback()
            print(f"✗ Error adding student: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
    
    def view_all_students(self):
        """Display all students"""
        print("\n" + "="*50)
        print("VIEW ALL STUDENTS")
        print("="*50)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM students ORDER BY name')
            students = cursor.fetchall()
            
            if not students:
                print("✗ No students found in database")
                return
            
            print(f"\n{'ID':<5} {'Name':<20} {'Marks':<8} {'Course':<15}")
            print("-" * 50)
            
            for student in students:
                print(f"{student['student_id']:<5} {student['name']:<20} {student['marks']:<8} {student['course']:<15}")
            
            print(f"\nTotal students: {len(students)}")
        
        except Error as e:
            print(f"✗ Error retrieving students: {e}")
    
    def search_student(self):
        """Search for a student"""
        print("\n" + "="*50)
        print("SEARCH STUDENT")
        print("="*50)
        print("Search by:\n1. ID\n2. Name\n3. Course")
        
        try:
            choice = input("Enter your choice (1-3): ").strip()
            cursor = self.conn.cursor()
            
            if choice == '1':
                try:
                    student_id = int(input("Enter student ID: "))
                    cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
                except ValueError:
                    print("✗ Invalid ID format!")
                    return
            
            elif choice == '2':
                name = input("Enter student name: ").strip()
                cursor.execute('SELECT * FROM students WHERE name LIKE ?', (f"%{name}%",))
            
            elif choice == '3':
                course = input("Enter course name: ").strip()
                cursor.execute('SELECT * FROM students WHERE course = ?', (course,))
            
            else:
                print("✗ Invalid choice!")
                return
            
            results = cursor.fetchall()
            
            if not results:
                print("✗ No students found!")
                return
            
            print(f"\n{'ID':<5} {'Name':<20} {'Marks':<8} {'Course':<15}")
            print("-" * 50)
            
            for student in results:
                print(f"{student['student_id']:<5} {student['name']:<20} {student['marks']:<8} {student['course']:<15}")
        
        except Error as e:
            print(f"✗ Error searching students: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
    
    def update_student(self):
        """Update student information"""
        print("\n" + "="*50)
        print("UPDATE STUDENT")
        print("="*50)
        
        try:
            try:
                student_id = int(input("Enter student ID to update: "))
            except ValueError:
                print("✗ Invalid ID format!")
                return
            
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            student = cursor.fetchone()
            
            if not student:
                print(f"✗ Student with ID {student_id} not found!")
                return
            
            print(f"\nCurrent details: Name={student['name']}, Marks={student['marks']}, Course={student['course']}")
            print("\nUpdate (leave blank to keep current):")
            
            new_name = input("New name: ").strip() or student['name']
            
            try:
                marks_input = input("New marks: ").strip()
                new_marks = float(marks_input) if marks_input else student['marks']
                
                if new_marks < 0 or new_marks > 100:
                    print("✗ Marks must be between 0 and 100!")
                    return
            except ValueError:
                print("✗ Invalid marks format!")
                return
            
            new_course = input("New course: ").strip() or student['course']
            
            # Begin transaction
            cursor.execute('''
                UPDATE students 
                SET name = ?, marks = ?, course = ?
                WHERE student_id = ?
            ''', (new_name, new_marks, new_course, student_id))
            
            self.conn.commit()
            print(f"✓ Student ID {student_id} updated successfully!")
        
        except Error as e:
            self.conn.rollback()
            print(f"✗ Error updating student: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
    
    def delete_student(self):
        """Delete a student"""
        print("\n" + "="*50)
        print("DELETE STUDENT")
        print("="*50)
        
        try:
            try:
                student_id = int(input("Enter student ID to delete: "))
            except ValueError:
                print("✗ Invalid ID format!")
                return
            
            cursor = self.conn.cursor()
            cursor.execute('SELECT name FROM students WHERE student_id = ?', (student_id,))
            student = cursor.fetchone()
            
            if not student:
                print(f"✗ Student with ID {student_id} not found!")
                return
            
            confirm = input(f"Are you sure you want to delete '{student['name']}'? (yes/no): ").lower()
            
            if confirm == 'yes':
                cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
                self.conn.commit()
                print(f"✓ Student '{student['name']}' deleted successfully!")
            else:
                print("✗ Deletion cancelled")
        
        except Error as e:
            self.conn.rollback()
            print(f"✗ Error deleting student: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
    
    def show_top_students(self):
        """Display top students by marks"""
        print("\n" + "="*50)
        print("TOP STUDENTS")
        print("="*50)
        
        try:
            try:
                limit = int(input("Enter number of top students to display (default 5): ") or "5")
                if limit <= 0:
                    print("✗ Number must be positive!")
                    return
            except ValueError:
                print("✗ Invalid number format!")
                return
            
            cursor = self.conn.cursor()
            # Parameterized query with LIMIT
            cursor.execute('''
                SELECT * FROM students
                ORDER BY marks DESC
                LIMIT ?
            ''', (limit,))
            
            students = cursor.fetchall()
            
            if not students:
                print("✗ No students found!")
                return
            
            print(f"\n{'Rank':<6} {'ID':<5} {'Name':<20} {'Marks':<8} {'Course':<15}")
            print("-" * 55)
            
            for rank, student in enumerate(students, 1):
                print(f"{rank:<6} {student['student_id']:<5} {student['name']:<20} {student['marks']:<8} {student['course']:<15}")
        
        except Error as e:
            print(f"✗ Error retrieving top students: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
    
    def course_wise_statistics(self):
        """Display statistics by course"""
        print("\n" + "="*50)
        print("COURSE-WISE STATISTICS")
        print("="*50)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT 
                    course,
                    COUNT(*) as count,
                    AVG(marks) as avg_marks,
                    MAX(marks) as max_marks,
                    MIN(marks) as min_marks
                FROM students
                GROUP BY course
                ORDER BY course
            ''')
            
            results = cursor.fetchall()
            
            if not results:
                print("✗ No data available!")
                return
            
            print(f"\n{'Course':<15} {'Students':<10} {'Avg Marks':<12} {'Max':<8} {'Min':<8}")
            print("-" * 55)
            
            for row in results:
                print(f"{row['course']:<15} {row['count']:<10} {row['avg_marks']:<12.2f} {row['max_marks']:<8} {row['min_marks']:<8}")
        
        except Error as e:
            print(f"✗ Error retrieving course statistics: {e}")
    
    def average_marks(self):
        """Display overall average marks"""
        print("\n" + "="*50)
        print("AVERAGE MARKS")
        print("="*50)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT AVG(marks) as avg_marks FROM students')
            result = cursor.fetchone()
            
            if result['avg_marks'] is None:
                print("✗ No students in database!")
                return
            
            print(f"\nOverall average marks: {result['avg_marks']:.2f}")
        
        except Error as e:
            print(f"✗ Error calculating average: {e}")
    
    def student_count(self):
        """Display total student count"""
        print("\n" + "="*50)
        print("STUDENT COUNT")
        print("="*50)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT COUNT(*) as total FROM students')
            result = cursor.fetchone()
            
            print(f"\nTotal students in database: {result['total']}")
            
            # Count by course
            cursor.execute('''
                SELECT course, COUNT(*) as count
                FROM students
                GROUP BY course
                ORDER BY count DESC
            ''')
            
            courses = cursor.fetchall()
            if courses:
                print("\nCount by course:")
                for course in courses:
                    print(f"  {course['course']}: {course['count']}")
        
        except Error as e:
            print(f"✗ Error counting students: {e}")
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Top Students")
        print("7. Course-wise Statistics")
        print("8. Average Marks")
        print("9. Student Count")
        print("10. Exit")
        print("="*50)
    
    def run(self):
        """Main application loop"""
        print("\n" + "*"*50)
        print("Welcome to Student Management System")
        print("*"*50)
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-10): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                self.show_top_students()
            elif choice == '7':
                self.course_wise_statistics()
            elif choice == '8':
                self.average_marks()
            elif choice == '9':
                self.student_count()
            elif choice == '10':
                print("\n✓ Thank you for using Student Management System!")
                print("✓ Closing database connection...\n")
                self.close()
                break
            else:
                print("✗ Invalid choice! Please enter a number between 1 and 10.")
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()


def main():
    """Main function to start the application"""
    system = StudentManagementSystem()
    system.run()


if __name__ == "__main__":
    main()
