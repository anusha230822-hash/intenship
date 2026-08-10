import json

student = {
    "name": "Ravi",
    "course": "Python",
    "marks": 85
}

with open("files/student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")
