from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def travel(self, distance):
        pass

class Bus(Transport):
    def travel(self, distance):
        return f"Bus travel for {distance} km. Fare: {distance * 0.5}"

class Train(Transport):
    def travel(self, distance):
        return f"Train travel for {distance} km. Fare: {distance * 0.3}"

class Flight(Transport):
    def travel(self, distance):
        return f"Flight travel for {distance} km. Fare: {distance * 0.8}"

class Cab(Transport):
    def travel(self, distance):
        return f"Cab travel for {distance} km. Fare: {distance * 1.2}"

if __name__ == '__main__':
    options = [Bus(), Train(), Flight(), Cab()]
    for o in options:
        print(type(o).__name__, '-', o.travel(100))
