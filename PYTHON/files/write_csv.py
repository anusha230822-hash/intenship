import csv

students = [
    ["Name", "Course", "Marks"],
    ["Ravi", "Python", 85],
    ["Sita", "Java", 90],
]

with open("files/students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")
