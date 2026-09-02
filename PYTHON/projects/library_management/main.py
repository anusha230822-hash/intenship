from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def info(self):
        pass

class Book(Item):
    def info(self):
        return 'Book info'

if __name__ == '__main__':
    print(Book().info())
