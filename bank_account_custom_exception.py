class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient account balance.")
        self.balance -= amount
        return self.balance


try:
    account = BankAccount(1000)
    print(f"Remaining balance: {account.withdraw(1200)}")
except InsufficientBalanceError as error:
    print(f"InsufficientBalanceError: {error}")
