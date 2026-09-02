class BankAccount:
    def __init__(self, holder, account_number, balance=0.0):
        self.holder = holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        raise ValueError('Deposit amount must be positive')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        raise ValueError('Insufficient funds')

    def display(self):
        print(f"Holder: {self.holder}, Account: {self.account_number}, Balance: {self.balance}")

if __name__ == '__main__':
    acc = BankAccount('Sam', 'ACC123', 1000.0)
    acc.display()
    print('After deposit:', acc.deposit(500))
    print('After withdraw:', acc.withdraw(300))
    acc.display()
