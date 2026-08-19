from database_manager import DatabaseManager


class StudentManagement:
    def __init__(self):
        self.database = DatabaseManager()

    def add_student(self, student_id, name, age, course, marks):
        self.database.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s)", (student_id, name, age, course, marks))
        self.database.commit()
        print("Student added successfully.")

    def list_students(self):
        return self.database.fetch_all("SELECT * FROM students ORDER BY id")

    def update_marks(self, student_id, marks):
        self.database.execute("UPDATE students SET marks = %s WHERE id = %s", (marks, student_id))
        self.database.commit()
        print(f"Marks updated. Rows changed: {self.database.row_count}")

    def remove_student(self, student_id):
        self.database.execute("DELETE FROM students WHERE id = %s", (student_id,))
        self.database.commit()
        print(f"Student removed. Rows deleted: {self.database.row_count}")

    def close(self):
        self.database.close()
