class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b if b != 0 else 'Infinity'

if __name__ == '__main__':
    calc = Calculator()
    print('Add:', calc.add(10,5))
    print('Sub:', calc.subtract(10,5))
    print('Mul:', calc.multiply(10,5))
    print('Div:', calc.divide(10,5))
