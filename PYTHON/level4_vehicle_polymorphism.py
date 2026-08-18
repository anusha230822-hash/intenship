from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine vroom"

class Bike(Vehicle):
    def start(self):
        return "Bike engine vroom"

if __name__ == '__main__':
    fleet = [Car(), Bike()]
    for v in fleet:
        print(type(v).__name__, v.start())
