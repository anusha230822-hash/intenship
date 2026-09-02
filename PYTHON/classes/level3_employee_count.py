class Employee:
    company_name = 'BizCorp'
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

if __name__ == '__main__':
    e1 = Employee('E1')
    e2 = Employee('E2')
    print('Company:', Employee.company_name)
    print('Employees:', Employee.employee_count)
