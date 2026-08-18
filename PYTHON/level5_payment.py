from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    def display_amount(self, amount):
        return f"Amount: {amount}"

class UPI(Payment):
    def pay(self, amount):
        return f"UPI paid {amount}"

class Card(Payment):
    def pay(self, amount):
        return f"Card charged {amount}"

if __name__ == '__main__':
    print(UPI().pay(100), UPI().display_amount(100))
    print(Card().pay(200), Card().display_amount(200))
