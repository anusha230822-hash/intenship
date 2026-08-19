try:
    salary = float(input("Enter employee salary: "))
    if salary < 0:
        raise ValueError("Employee salary cannot be negative.")
    print(f"Valid employee salary: {salary}")
except ValueError as error:
    print(f"Salary validation error: {error}")
