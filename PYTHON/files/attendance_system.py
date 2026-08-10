from datetime import datetime

name = input("Enter student name: ")
current_date = datetime.now().strftime("%d-%m-%Y")
current_time = datetime.now().strftime("%I:%M %p")

with open("files/attendance.txt", "a", encoding="utf-8") as file:
    file.write(f"{name},{current_date},{current_time},Present\n")

print("Attendance recorded successfully.")
