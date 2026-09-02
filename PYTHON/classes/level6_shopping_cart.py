class ShoppingCart:
    def __init__(self):
        self.items = {}  # name -> (unit_price, qty)

    def add_product(self, name, price, qty=1):
        if qty <= 0:
            raise ValueError('Quantity must be positive')
        if name in self.items:
            cur_price, cur_qty = self.items[name]
            self.items[name] = (price, cur_qty + qty)
        else:
            self.items[name] = (price, qty)

    def remove_product(self, name, qty=None):
        if name not in self.items:
            raise KeyError('Product not in cart')
        price, cur_qty = self.items[name]
        if qty is None or qty >= cur_qty:
            del self.items[name]
        else:
            self.items[name] = (price, cur_qty - qty)

    def total(self):
        return sum(price * qty for price, qty in self.items.values())

if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_product('Apple', 5, 3)
    cart.add_product('Banana', 2, 5)
    print('Total:', cart.total())
    cart.remove_product('Apple', 1)
    print('Total after removing 1 apple:', cart.total())
