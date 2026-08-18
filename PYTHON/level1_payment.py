from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via UPI"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via Card"

if __name__ == "__main__":
    print(UPIPayment().pay(100))
    print(CardPayment().pay(250))
