class Student:
    def __init__(self, name):
        self.name = name


student = Student("Anusha")

try:
    print(student.address)
except AttributeError:
    print("Error: The object does not have an 'address' attribute.")
