from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def display_info(self):
        return "Vehicle info available"

class Car(Vehicle):
    def start(self):
        return "Car started"

class Bike(Vehicle):
    def start(self):
        return "Bike started"

if __name__ == '__main__':
    print(Car().start(), Car().display_info())
    print(Bike().start(), Bike().display_info())
