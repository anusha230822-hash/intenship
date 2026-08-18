from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def calculate_interest(self):
        return self.balance * 0.04

class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def calculate_interest(self):
        return 0.0

if __name__ == "__main__":
    print(SavingsAccount(1000).calculate_interest())
    print(CurrentAccount(1000).calculate_interest())
