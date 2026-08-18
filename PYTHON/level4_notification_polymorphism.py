from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, msg):
        pass

class Email(Notification):
    def send(self, msg):
        return f"Email: {msg}"

class SMS(Notification):
    def send(self, msg):
        return f"SMS: {msg}"

class WhatsApp(Notification):
    def send(self, msg):
        return f"WhatsApp: {msg}"

if __name__ == '__main__':
    notifs = [Email(), SMS(), WhatsApp()]
    for n in notifs:
        print(type(n).__name__, n.send('Hello'))
