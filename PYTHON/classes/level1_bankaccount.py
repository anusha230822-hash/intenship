class BankAccount:
    def __init__(self, holder, account_number):
        self.holder = holder
        self.account_number = account_number

if __name__ == '__main__':
    a = BankAccount('Sam','12345')
    print('Account:', a.holder, a.account_number)
