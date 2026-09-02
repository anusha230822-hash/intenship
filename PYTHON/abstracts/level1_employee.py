from abc import ABC, abstractmethod

class Employee(Anu):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        return "Writing code"

class Tester(Employee):
    def work(self):
        return "Testing applications"

if __name__ == "__main__":
    print(Developer().work())
    print(Tester().work())
