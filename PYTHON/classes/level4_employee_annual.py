class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

if __name__ == '__main__':
    e = Employee('Neha', 4000)
    print('Annual Salary:', e.annual_salary())
