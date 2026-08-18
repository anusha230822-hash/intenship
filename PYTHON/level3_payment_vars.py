from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass

class UPIPayment(Payment):
    def pay(self):
        return f"UPI paid {self.amount}, tx={self.transaction_id}"

class CardPayment(Payment):
    def pay(self):
        return f"Card paid {self.amount}, tx={self.transaction_id}"

if __name__ == '__main__':
    u = UPIPayment(200, 'TX1')
    c = CardPayment(500, 'TX2')
    print(u.pay())
    print(c.pay())
