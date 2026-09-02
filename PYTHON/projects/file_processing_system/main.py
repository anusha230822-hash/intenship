from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

class CSVHandler(FileHandler):
    def read(self):
        return 'CSV read'

if __name__ == '__main__':
    print(CSVHandler().read())
