from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        return 8000

class Developer(Employee):
    def salary(self):
        return 5000

class Tester(Employee):
    def salary(self):
        return 3500

if __name__ == '__main__':
    staff = [Manager(), Developer(), Tester()]
    for e in staff:
        print(type(e).__name__, e.salary())
