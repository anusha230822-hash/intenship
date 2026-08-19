class InvalidSalaryError(Exception):
    pass


try:
    salary = float(input("Enter employee salary: "))
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")
    print("Employee salary is valid.")
except InvalidSalaryError as error:
    print(f"InvalidSalaryError: {error}")
except ValueError:
    print("Please enter a valid salary.")
