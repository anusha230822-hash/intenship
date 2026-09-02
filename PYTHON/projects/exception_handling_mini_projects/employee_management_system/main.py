class InvalidEmployeeIdError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


class InvalidDepartmentError(Exception):
    pass


class EmployeeManagement:
    departments = {"IT", "HR", "Finance"}

    def add_employee(self, employee_id, name, salary, department):
        if employee_id <= 0:
            raise InvalidEmployeeIdError("Employee ID must be positive.")
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative.")
        if department not in self.departments:
            raise InvalidDepartmentError("Department is not registered.")
        return f"Employee {name} added to {department}."


try:
    employees = EmployeeManagement()
    print(employees.add_employee(1, "Rahul", 50000, "IT"))
except (InvalidEmployeeIdError, InvalidSalaryError, InvalidDepartmentError) as error:
    print(f"Employee management error: {error}")
