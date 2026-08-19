class InvalidTransactionError(Exception):
    pass


try:
    transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
    amount = float(input("Enter transaction amount: "))
    if transaction_type not in {"deposit", "withdraw"}:
        raise InvalidTransactionError("Transaction type must be deposit or withdraw.")
    if amount <= 0:
        raise InvalidTransactionError("Transaction amount must be positive.")
    print("Transaction is valid.")
except InvalidTransactionError as error:
    print(f"InvalidTransactionError: {error}")
except ValueError:
    print("Please enter a valid amount.")
