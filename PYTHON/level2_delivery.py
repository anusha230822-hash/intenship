from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self, weight):
        pass

    @abstractmethod
    def deliver(self, address):
        pass

class StandardDelivery(Delivery):
    def calculate_charge(self, weight):
        return 5 + 1 * weight
    def deliver(self, address):
        return f"Standard delivery to {address}"

class ExpressDelivery(Delivery):
    def calculate_charge(self, weight):
        return 10 + 2 * weight
    def deliver(self, address):
        return f"Express delivery to {address}"

if __name__ == "__main__":
    s = StandardDelivery()
    e = ExpressDelivery()
    print(s.calculate_charge(3), s.deliver('Home'))
    print(e.calculate_charge(3), e.deliver('Office'))
