class Student:
	pass

first_student = Student()
second_student = first_student
print("Objects are identical:", first_student is second_student)