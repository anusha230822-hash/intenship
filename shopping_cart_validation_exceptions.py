class InvalidProductError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self, products):
        self.products = products
        self.items = []

    def add_item(self, product, quantity):
        if product not in self.products:
            raise InvalidProductError("Product is not available.")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero.")
        self.items.append((product, quantity))
        return "Item added to cart."


try:
    cart = ShoppingCart({"Laptop": 55000})
    print(cart.add_item("Phone", 1))
except (InvalidProductError, InvalidQuantityError) as error:
    print(f"Shopping cart error: {error}")
