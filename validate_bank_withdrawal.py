try:
    balance = float(input("Enter available balance: "))
    withdrawal = float(input("Enter withdrawal amount: "))
    if withdrawal > balance:
        raise ValueError("Withdrawal amount cannot exceed the available balance.")
    print("Withdrawal approved.")
except ValueError as error:
    print(f"Withdrawal validation error: {error}")
