class Product:
    category = 'General'

    def __init__(self, name, price):
        self.name = name
        self.price = price

if __name__ == '__main__':
    p1 = Product('Pen', 2)
    p2 = Product('Book', 100)
    for p in (p1,p2):
        print(p.name, p.price, '-', Product.category)
