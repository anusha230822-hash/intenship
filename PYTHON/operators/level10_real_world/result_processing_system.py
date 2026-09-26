marks = [85, 90, 95]
total = sum(marks)
average = total / len(marks)
percentage = average
grade = "A" if percentage >= 80 else "B"
passed = percentage >= 40
print("Total:", total, "Average:", average, "Grade:", grade, "Passed:", passed)