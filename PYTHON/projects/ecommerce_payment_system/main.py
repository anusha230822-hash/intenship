from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        return f'UPI paid {amount}'

if __name__ == '__main__':
    print(UPIPayment().pay(150))
