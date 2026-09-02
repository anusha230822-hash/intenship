class Car:
    number_of_wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

if __name__ == '__main__':
    c1 = Car('Toyota','C1')
    c2 = Car('Honda','C2')
    print(c1.brand, c1.model, 'Wheels:', Car.number_of_wheels)
    print(c2.brand, c2.model, 'Wheels:', c2.number_of_wheels)
