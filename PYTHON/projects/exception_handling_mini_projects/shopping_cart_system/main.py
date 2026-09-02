class InvalidProductError(Exception):
    pass


class InsufficientStockError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.products = {"Laptop": {"price": 55000, "stock": 3}}
        self.items = []

    def add(self, product, quantity):
        if product not in self.products:
            raise InvalidProductError("Product does not exist.")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be positive.")
        if quantity > self.products[product]["stock"]:
            raise InsufficientStockError("Insufficient product stock.")
        self.products[product]["stock"] -= quantity
        self.items.append((product, quantity))


try:
    cart = ShoppingCart()
    cart.add("Laptop", 1)
    print("Product added to cart successfully.")
except (InvalidProductError, InsufficientStockError, InvalidQuantityError) as error:
    print(f"Shopping cart error: {error}")
