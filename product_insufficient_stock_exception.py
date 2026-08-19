class InsufficientStockError(Exception):
    pass


class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.stock:
            raise InsufficientStockError("Requested quantity exceeds available stock.")
        self.stock -= quantity
        return self.stock


try:
    product = Product("Laptop", 3)
    print(f"Remaining stock: {product.sell(5)}")
except (ValueError, InsufficientStockError) as error:
    print(f"Stock error: {error}")
