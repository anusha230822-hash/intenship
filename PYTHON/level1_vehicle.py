from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car started"

class Bike(Vehicle):
    def start(self):
        return "Bike started"

if __name__ == "__main__":
    print(Car().start())
    print(Bike().start())
