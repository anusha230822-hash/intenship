def withdraw_money(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


try:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter withdrawal amount: "))
    print(f"Remaining balance: {withdraw_money(balance, amount)}")
except ValueError as error:
    print(f"Withdrawal error: {error}")
