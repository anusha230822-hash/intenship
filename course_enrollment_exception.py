class InvalidEnrollmentError(Exception):
    pass


class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def enroll(self, student_name):
        if not student_name.strip():
            raise InvalidEnrollmentError("Student name cannot be empty.")
        if student_name in self.students:
            raise InvalidEnrollmentError("Student is already enrolled.")
        if len(self.students) >= self.capacity:
            raise InvalidEnrollmentError("Course has reached its capacity.")
        self.students.append(student_name)
        return f"{student_name} enrolled in {self.name}."


try:
    course = Course("Python", 1)
    course.enroll("Anusha")
    print(course.enroll("Rahul"))
except InvalidEnrollmentError as error:
    print(f"InvalidEnrollmentError: {error}")
