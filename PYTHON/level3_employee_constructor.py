from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary):
        super().__init__(name, employee_id)
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

if __name__ == '__main__':
    dev = Developer('Alice', 'E001', 5000)
    print(dev.name, dev.employee_id, dev.calculate_salary())
