class Employee:
    company_name = 'TechCorp'

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    e1 = Employee('E1')
    e2 = Employee('E2')
    e3 = Employee('E3')
    for e in (e1,e2,e3):
        print(e.name, '-', Employee.company_name)
