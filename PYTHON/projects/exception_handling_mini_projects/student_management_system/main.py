class InvalidMarksError(Exception):
    pass


class DuplicateStudentError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add(self, student_id, name, marks):
        if student_id in self.students:
            raise DuplicateStudentError("Student ID already exists.")
        if not 0 <= marks <= 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        self.students[student_id] = (name, marks)

    def get(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError("Student was not found.")
        return self.students[student_id]


try:
    system = StudentManagementSystem()
    system.add(1, "Anusha", 88)
    print(system.get(1))
except (InvalidMarksError, DuplicateStudentError, StudentNotFoundError) as error:
    print(f"Student management error: {error}")
