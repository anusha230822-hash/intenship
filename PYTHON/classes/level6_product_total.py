class Product:
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price

    def total_price(self, quantity):
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        return self.unit_price * quantity

if __name__ == '__main__':
    p = Product('Pen', 10)
    print('Total for 4:', p.total_price(4))
