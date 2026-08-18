from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

class Electronic(Product):
    def calculate_discount(self):
        return self.price * 0.1

class Grocery(Product):
    def calculate_discount(self):
        return self.price * 0.05

if __name__ == '__main__':
    e = Electronic('Phone', 1000)
    g = Grocery('Rice', 50)
    print(e.name, e.price, e.calculate_discount())
    print(g.name, g.price, g.calculate_discount())
