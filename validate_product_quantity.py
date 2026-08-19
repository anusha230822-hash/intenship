try:
    quantity = int(input("Enter product quantity: "))
    if quantity <= 0:
        raise ValueError("Product quantity must be greater than zero.")
    print(f"Valid product quantity: {quantity}")
except ValueError as error:
    print(f"Quantity validation error: {error}")
