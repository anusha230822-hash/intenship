class InsufficientStockError(Exception):
    pass


stock = 5
try:
    quantity = int(input("Enter required product quantity: "))
    if quantity > stock:
        raise InsufficientStockError("Requested quantity is greater than available stock.")
    stock -= quantity
    print(f"Purchase successful. Remaining stock: {stock}")
except InsufficientStockError as error:
    print(f"InsufficientStockError: {error}")
except ValueError:
    print("Please enter a valid quantity.")
