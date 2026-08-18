from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"SMS sent: {message}"

if __name__ == "__main__":
    print(EmailNotification().send('Hello'))
    print(SMSNotification().send('Hi'))
