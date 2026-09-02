class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

if __name__ == '__main__':
    p = Product('Notebook', 50, 3)
    print('Product:', p.name)
    print('Total Price:', p.total_price())
