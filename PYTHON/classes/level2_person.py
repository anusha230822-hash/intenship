class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

if __name__ == '__main__':
    p1 = Person('Anna', 30, 'Delhi')
    p2 = Person('Rahul', 25, 'Mumbai')
    print(p1.name, p1.age, p1.city)
    print(p2.name, p2.age, p2.city)
