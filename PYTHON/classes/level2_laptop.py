class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

if __name__ == '__main__':
    l1 = Laptop('Dell','8GB','256GB',600)
    l2 = Laptop('HP','16GB','512GB',900)
    l3 = Laptop('Lenovo','8GB','1TB',700)
    for l in (l1,l2,l3):
        print(l.brand, l.ram, l.storage, l.price)
