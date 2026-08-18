from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, msg):
        pass

    def display_message(self, msg):
        return f"Message: {msg}"

class Email(Notification):
    def send(self, msg):
        return f"Email sent: {msg}"

class SMS(Notification):
    def send(self, msg):
        return f"SMS sent: {msg}"

if __name__ == '__main__':
    print(Email().send('Hi'), Email().display_message('Hi'))
    print(SMS().send('Hi'), SMS().display_message('Hi'))
