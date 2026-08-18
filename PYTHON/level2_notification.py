from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def schedule(self, message, time):
        pass

class Email(Notification):
    def send(self, message):
        return f"Email: {message}"
    def schedule(self, message, time):
        return f"Email scheduled at {time}: {message}"

class SMS(Notification):
    def send(self, message):
        return f"SMS: {message}"
    def schedule(self, message, time):
        return f"SMS scheduled at {time}: {message}"

class WhatsApp(Notification):
    def send(self, message):
        return f"WhatsApp: {message}"
    def schedule(self, message, time):
        return f"WhatsApp scheduled at {time}: {message}"

if __name__ == "__main__":
    for n in (Email(), SMS(), WhatsApp()):
        print(n.send('Hi'))
        print(n.schedule('Reminder', '10:00'))
