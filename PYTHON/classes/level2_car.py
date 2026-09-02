class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

if __name__ == '__main__':
    c1 = Car('Toyota','Corolla',2018,800000)
    c2 = Car('Honda','Civic',2020,1200000)
    c3 = Car('Ford','Mustang',2019,2500000)
    for c in (c1, c2, c3):
        print(c.brand, c.model, c.year, c.price)
