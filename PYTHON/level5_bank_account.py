from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        return "Balance shown"

class Savings(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def calculate_interest(self):
        return self.balance * 0.03

class Current(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def calculate_interest(self):
        return 0.0

if __name__ == '__main__':
    s = Savings(2000)
    c = Current(2000)
    print(s.calculate_interest(), s.display_balance())
    print(c.calculate_interest(), c.display_balance())
