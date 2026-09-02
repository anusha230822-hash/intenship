from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def rent(self):
        pass

class Car(Vehicle):
    def rent(self):
        return 'Car rented'

if __name__ == '__main__':
    print(Car().rent())
