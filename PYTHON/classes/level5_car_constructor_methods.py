class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.running = False

    def start(self):
        self.running = True
        print('Car started')

    def stop(self):
        self.running = False
        print('Car stopped')

    def display(self):
        print(f"{self.brand} {self.model} ({self.year}) - Running: {self.running}")

if __name__ == '__main__':
    c = Car('Toyota', 'Corolla', 2020)
    c.start()
    c.display()
    c.stop()
    c.display()
