from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(dog.sound())
    print(cat.sound())
