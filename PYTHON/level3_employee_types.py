from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 1000

class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 500

class Tester(Employee):
    def calculate_salary(self):
        return self.salary + 300

if __name__ == '__main__':
    m = Manager('M', 5000)
    d = Developer('D', 4000)
    t = Tester('T', 3000)
    print(m.name, m.calculate_salary())
    print(d.name, d.calculate_salary())
    print(t.name, t.calculate_salary())
