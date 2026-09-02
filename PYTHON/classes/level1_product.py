class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

if __name__ == '__main__':
    p = Product('Pen', 2, 50)
    print('Product:', p.name, p.price, p.quantity)
