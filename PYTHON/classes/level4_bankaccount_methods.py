class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        return 'Invalid amount'

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return 'Insufficient funds'

if __name__ == '__main__':
    a = BankAccount('Sam', 1000)
    print('Balance:', a.deposit(500))
    print('Balance after withdraw:', a.withdraw(300))
    print('Withdraw too much:', a.withdraw(5000))
