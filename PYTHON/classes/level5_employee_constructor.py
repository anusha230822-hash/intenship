class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name} (ID: {self.emp_id}), Dept: {self.department}, Salary: {self.salary}")

    def annual_salary(self):
        return self.salary * 12

if __name__ == '__main__':
    e = Employee('E001', 'Ravi', 'HR', 45000)
    e.display()
    print('Annual Salary:', e.annual_salary())
