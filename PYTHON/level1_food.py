from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(Food):
    def prepare(self):
        return "Preparing Pizza"

class Burger(Food):
    def prepare(self):
        return "Preparing Burger"

if __name__ == "__main__":
    print(Pizza().prepare())
    print(Burger().prepare())
