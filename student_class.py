from database_manager import DatabaseManager


class Student:
    def __init__(self):
        self.database = DatabaseManager()

    def insert(self, student_id, name, age, course, marks):
        self.database.execute(
            "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
            (student_id, name, age, course, marks),
        )
        self.database.commit()
        print("Student inserted successfully.")

    def update(self, student_id, name, marks):
        self.database.execute(
            "UPDATE students SET name = %s, marks = %s WHERE id = %s",
            (name, marks, student_id),
        )
        self.database.commit()
        print(f"Student updated. Rows changed: {self.database.row_count}")

    def delete(self, student_id):
        self.database.execute("DELETE FROM students WHERE id = %s", (student_id,))
        self.database.commit()
        print(f"Student deleted. Rows deleted: {self.database.row_count}")

    def retrieve(self):
        return self.database.fetch_all(
            "SELECT id, name, age, course, marks FROM students ORDER BY id"
        )

    def close(self):
        self.database.close()


if __name__ == "__main__":
    student = Student()
    print(student.retrieve())
    student.close()
