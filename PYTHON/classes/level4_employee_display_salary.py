class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

if __name__ == '__main__':
    e = Employee('Ravi', 45000)
    print(e.display_salary())
