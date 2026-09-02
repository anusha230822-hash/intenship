class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

if __name__ == '__main__':
    employees = [
        Employee('E1','HR',3000),
        Employee('E2','IT',4000),
        Employee('E3','Sales',3500),
        Employee('E4','Finance',3800),
        Employee('E5','Support',2800),
    ]
    for e in employees:
        print(e.name, e.department, e.salary)
