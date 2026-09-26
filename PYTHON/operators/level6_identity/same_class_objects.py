class Student:
	pass

first_student = Student()
second_student = Student()
print("Same class:", type(first_student) is type(second_student))
print("Same object:", first_student is second_student)