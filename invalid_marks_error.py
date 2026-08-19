class InvalidMarksError(Exception):
    pass


try:
    marks = float(input("Enter student marks: "))
    if not 0 <= marks <= 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    print("Student marks are valid.")
except InvalidMarksError as error:
    print(f"InvalidMarksError: {error}")
except ValueError:
    print("Please enter a valid number.")
