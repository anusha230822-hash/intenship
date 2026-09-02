class InvalidAmountError(Exception):
    pass


class InvalidAccountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class BankingSystem:
    def __init__(self):
        self.accounts = {1001: 5000.0}

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise InvalidAccountError("Account number is invalid.")
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        if amount > self.accounts[account_number]:
            raise InsufficientBalanceError("Insufficient balance.")
        self.accounts[account_number] -= amount
        return self.accounts[account_number]


try:
    bank = BankingSystem()
    print(f"Remaining balance: {bank.withdraw(1001, 1000)}")
except (InvalidAccountError, InvalidAmountError, InsufficientBalanceError) as error:
    print(f"Banking error: {error}")
