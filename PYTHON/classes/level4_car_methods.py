class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.running = False

    def start(self):
        self.running = True
        return 'Car started'

    def stop(self):
        self.running = False
        return 'Car stopped'

    def display_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Running: {self.running}"

if __name__ == '__main__':
    c = Car('Hyundai','i20')
    print(c.start())
    print(c.display_details())
    print(c.stop())
    print(c.display_details())
