from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, account_number):
        self.holder = holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, holder, account_number, balance):
        super().__init__(holder, account_number)
        self.balance = balance
    def calculate_interest(self):
        return self.balance * 0.03

class CurrentAccount(BankAccount):
    def __init__(self, holder, account_number, balance):
        super().__init__(holder, account_number)
        self.balance = balance
    def calculate_interest(self):
        return 0.0

if __name__ == '__main__':
    s = SavingsAccount('anu', 'A100', 2000)
    c = CurrentAccount('yashu', 'A200', 2000)
    print(s.holder, s.account_number, s.calculate_interest())
    print(c.holder, c.account_number, c.calculate_interest())
