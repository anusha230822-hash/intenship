class Car:
    company = 'AutoCorp'
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

if __name__ == '__main__':
    c = Car('ModelX', 1500000)
    print('Company:', Car.company)
    print('Wheels:', Car.number_of_wheels)
    print('Model:', c.model, 'Price:', c.price)
