from abc import ABC, abstractmethod

class ECommercePayment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class UPI(ECommercePayment):
    def process_payment(self, amount):
        return f"UPI processed {amount}"

class CreditCard(ECommercePayment):
    def process_payment(self, amount):
        return f"CreditCard charged {amount}"

class DebitCard(ECommercePayment):
    def process_payment(self, amount):
        return f"DebitCard charged {amount}"

class NetBanking(ECommercePayment):
    def process_payment(self, amount):
        return f"NetBanking transferred {amount}"

if __name__ == '__main__':
    methods = [UPI(), CreditCard(), DebitCard(), NetBanking()]
    for m in methods:
        print(type(m).__name__, m.process_payment(250))
