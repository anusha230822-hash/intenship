def calculate_grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"


try:
    marks = float(input("Enter student marks: "))
    print(f"Grade: {calculate_grade(marks)}")
except ValueError as error:
    print(f"Grade error: {error}")
