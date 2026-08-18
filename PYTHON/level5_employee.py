from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        return "Company: Acme Corp"

class Developer(Employee):
    def __init__(self, base):
        self.base = base
    def calculate_salary(self):
        return self.base + 500

class Manager(Employee):
    def __init__(self, base):
        self.base = base
    def calculate_salary(self):
        return self.base + 1000

if __name__ == '__main__':
    dev = Developer(4000)
    man = Manager(6000)
    print(dev.calculate_salary(), dev.display_company())
    print(man.calculate_salary(), man.display_company())
