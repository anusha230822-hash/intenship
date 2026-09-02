class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

if __name__ == '__main__':
    m = Mobile('Samsung','A52',250)
    print('Mobile:', m.brand, m.model, m.price)
