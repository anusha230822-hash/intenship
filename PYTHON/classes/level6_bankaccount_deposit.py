class BankAccount:
    def __init__(self, holder, account_number, balance=0.0):
        self.holder = holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit must be positive')
        self.balance += amount
        return self.balance

if __name__ == '__main__':
    a = BankAccount('Sam', 'ACC200', 200.0)
    print('Balance before:', a.balance)
    print('After deposit:', a.deposit(150))
