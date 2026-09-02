class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError('Division by zero')
        return a / b

if __name__ == '__main__':
    calc = Calculator()
    print('Add:', calc.add(7, 3))
    print('Sub:', calc.subtract(7, 3))
    print('Mul:', calc.multiply(7, 3))
    print('Div:', calc.divide(7, 3))
