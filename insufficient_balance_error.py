class InsufficientBalanceError(Exception):
    pass


balance = 1000.0
try:
    withdrawal = float(input("Enter withdrawal amount: "))
    if withdrawal > balance:
        raise InsufficientBalanceError("Withdrawal exceeds the available balance.")
    balance -= withdrawal
    print(f"Withdrawal successful. Balance: {balance}")
except InsufficientBalanceError as error:
    print(f"InsufficientBalanceError: {error}")
