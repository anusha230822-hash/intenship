from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.04

class CurrentAccount(Account):
    def calculate_interest(self):
        return 0.0

if __name__ == '__main__':
    s = SavingsAccount('A1', 1000)
    c = CurrentAccount('A2', 1000)
    print(s.account_number, s.calculate_interest())
    print(c.account_number, c.calculate_interest())
