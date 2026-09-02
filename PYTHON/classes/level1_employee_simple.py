class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

if __name__ == '__main__':
    e = Employee('Bob','E123')
    print('Employee:', e.name, e.emp_id)
