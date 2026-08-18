from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate(self, weight):
        pass

class Standard(Delivery):
    def calculate(self, weight):
        return 5 + weight * 1

class Express(Delivery):
    def calculate(self, weight):
        return 10 + weight * 2

if __name__ == '__main__':
    options = [Standard(), Express()]
    for o in options:
        print(type(o).__name__, o.calculate(3))
