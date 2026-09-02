from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Standard(Delivery):
    def deliver(self):
        return 'Deliver standard'

if __name__ == '__main__':
    print(Standard().deliver())
