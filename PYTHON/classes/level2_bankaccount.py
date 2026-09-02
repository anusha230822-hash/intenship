class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

if __name__ == '__main__':
    a1 = BankAccount('Sam','A001',5000)
    a2 = BankAccount('Nina','A002',10000)
    print(a1.account_holder, a1.account_number, a1.balance)
    print(a2.account_holder, a2.account_number, a2.balance)
