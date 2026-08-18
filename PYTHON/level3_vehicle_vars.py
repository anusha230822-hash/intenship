from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} started"
    def stop(self):
        return f"{self.brand} {self.model} stopped"

class Bike(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} started"
    def stop(self):
        return f"{self.brand} {self.model} stopped"

if __name__ == '__main__':
    c = Car('Toyota', 'Corolla')
    b = Bike('Yamaha', 'R15')
    print(c.start())
    print(c.stop())
    print(b.start())
    print(b.stop())
