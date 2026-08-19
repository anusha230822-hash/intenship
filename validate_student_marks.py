try:
    marks = float(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    print(f"Valid marks: {marks}")
except ValueError as error:
    print(f"Marks validation error: {error}")
