from abc import ABC, abstractmethod

class EmployeePayroll(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class FullTimeEmployee(EmployeePayroll):
    def __init__(self, salary):
        self.salary = salary
    def calculate_pay(self):
        return self.salary

class PartTimeEmployee(EmployeePayroll):
    def __init__(self, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours
    def calculate_pay(self):
        return self.hourly_rate * self.hours

class ContractEmployee(EmployeePayroll):
    def __init__(self, contract_amount):
        self.contract_amount = contract_amount
    def calculate_pay(self):
        return self.contract_amount

if __name__ == '__main__':
    workers = [FullTimeEmployee(5000), PartTimeEmployee(20, 80), ContractEmployee(2000)]
    for w in workers:
        print(type(w).__name__, '-', w.calculate_pay())
