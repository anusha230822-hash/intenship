name = input("Enter student name: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

with open("files/students.txt", "a", encoding="utf-8") as file:
    file.write(f"{name},{course},{marks}\n")

print("Student record saved successfully.")
