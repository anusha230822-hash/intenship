class InvalidPinError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidWithdrawalError(Exception):
    pass


class InvalidAccountError(Exception):
    pass


class ATM:
    def __init__(self):
        self.accounts = {1001: {"pin": "1234", "balance": 5000}}

    def withdraw(self, account_id, pin, amount):
        if account_id not in self.accounts:
            raise InvalidAccountError("Account does not exist.")
        account = self.accounts[account_id]
        if account["pin"] != pin:
            raise InvalidPinError("Invalid PIN.")
        if amount <= 0:
            raise InvalidWithdrawalError("Withdrawal amount must be positive.")
        if amount > account["balance"]:
            raise InsufficientBalanceError("Insufficient balance.")
        account["balance"] -= amount
        return account["balance"]


try:
    atm = ATM()
    print(f"Withdrawal successful. Balance: {atm.withdraw(1001, '1234', 500)}")
except (InvalidPinError, InsufficientBalanceError, InvalidWithdrawalError, InvalidAccountError) as error:
    print(f"ATM error: {error}")
