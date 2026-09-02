class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

if __name__ == '__main__':
    p = Product('Bottle', 20, 5)
    print('Total cost:', p.total_cost())
