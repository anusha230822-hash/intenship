from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

    def display_product(self):
        return "Product displayed"

class Electronics(Product):
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 0.1

class Grocery(Product):
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 0.05

if __name__ == '__main__':
    e = Electronics(1000)
    g = Grocery(50)
    print(e.calculate_discount(), e.display_product())
    print(g.calculate_discount(), g.display_product())
