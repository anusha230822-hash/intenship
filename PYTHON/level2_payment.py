from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        return f"UPI paid {amount}"
    def refund(self, amount):
        return f"UPI refunded {amount}"

class CreditCard(Payment):
    def pay(self, amount):
        return f"CreditCard charged {amount}"
    def refund(self, amount):
        return f"CreditCard refunded {amount}"

class NetBanking(Payment):
    def pay(self, amount):
        return f"NetBanking paid {amount}"
    def refund(self, amount):
        return f"NetBanking refunded {amount}"

if __name__ == "__main__":
    for p in (UPI(), CreditCard(), NetBanking()):
        print(p.pay(100))
        print(p.refund(50))
