from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        return 'Student'

class Teacher(Person):
    def role(self):
        return 'Teacher'

class Doctor(Person):
    def role(self):
        return 'Doctor'

if __name__ == '__main__':
    s = Student('Sam', 20)
    t = Teacher('Tina', 35)
    d = Doctor('Dan', 45)
    print(s.name, s.age, s.role())
    print(t.name, t.age, t.role())
    print(d.name, d.age, d.role())
