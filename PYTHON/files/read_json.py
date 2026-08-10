import json

with open("files/student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student)
print(student["name"])
