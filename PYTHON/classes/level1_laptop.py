class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

if __name__ == '__main__':
    lap = Laptop('Dell','8GB','i5',700)
    print('Laptop:', lap.brand, lap.ram, lap.processor, lap.price)
