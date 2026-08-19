balance = 1000.0

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: {balance}")
except ValueError as error:
    print(f"Withdrawal failed: {error}")
finally:
    print("Bank transaction finished.")
