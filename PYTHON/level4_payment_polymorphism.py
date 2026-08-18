from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class UPI(Payment):
    def process(self, amount):
        return f"UPI processed {amount}"

class CreditCard(Payment):
    def process(self, amount):
        return f"CreditCard charged {amount}"

class NetBanking(Payment):
    def process(self, amount):
        return f"NetBanking transferred {amount}"

if __name__ == '__main__':
    payments = [UPI(), CreditCard(), NetBanking()]
    for p in payments:
        print(type(p).__name__, p.process(150))
