class InvalidMarksError(Exception):
    pass


class Student:
    def __init__(self, name, marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        self.name = name
        self.marks = marks


try:
    student = Student("Anusha", 120)
    print(f"{student.name}: {student.marks}")
except InvalidMarksError as error:
    print(f"InvalidMarksError: {error}")
