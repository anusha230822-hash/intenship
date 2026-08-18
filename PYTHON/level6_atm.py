from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class BankATM(ATM):
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return f"Withdrawn {amount}. New balance: {self._balance}"

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self._balance += amount
        return f"Deposited {amount}. New balance: {self._balance}"

    def check_balance(self):
        return self._balance

if __name__ == '__main__':
    atm = BankATM(1000)
    print(atm.check_balance())
    print(atm.withdraw(200))
    print(atm.deposit(500))
    print(atm.withdraw(2000))
