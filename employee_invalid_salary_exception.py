class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative.")
        self.name = name
        self.salary = salary


try:
    employee = Employee("Rahul", -5000)
    print(f"{employee.name}: {employee.salary}")
except InvalidSalaryError as error:
    print(f"InvalidSalaryError: {error}")
