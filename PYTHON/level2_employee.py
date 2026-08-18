from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

class Manager(Employee):
    def __init__(self, name, base):
        self.name = name
        self.base = base
    def calculate_salary(self):
        return self.base + 1000
    def display_details(self):
        return f"Manager: {self.name}, Salary: {self.calculate_salary()}"

class Developer(Employee):
    def __init__(self, name, base):
        self.name = name
        self.base = base
    def calculate_salary(self):
        return self.base + 500
    def display_details(self):
        return f"Developer: {self.name}, Salary: {self.calculate_salary()}"

if __name__ == "__main__":
    m = Manager('Alice', 5000)
    d = Developer('Bob', 4000)
    print(m.display_details())
    print(d.display_details())
