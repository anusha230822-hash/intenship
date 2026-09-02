class BankAccount:
    bank_name = 'National Bank'

    def __init__(self, holder, acc_no):
        self.holder = holder
        self.acc_no = acc_no

if __name__ == '__main__':
    a1 = BankAccount('Sam','A1')
    a2 = BankAccount('Nina','A2')
    for a in (a1,a2):
        print(a.holder, a.acc_no, '-', BankAccount.bank_name)
