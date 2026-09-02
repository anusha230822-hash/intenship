class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

if __name__ == '__main__':
    p1 = Product('Pen', 2, 10)
    p2 = Product('Notebook', 50, 2)
    p3 = Product('Bag', 800, 1)
    for p in (p1, p2, p3):
        print(p.name, p.price, p.quantity, 'Total:', p.total_price())
