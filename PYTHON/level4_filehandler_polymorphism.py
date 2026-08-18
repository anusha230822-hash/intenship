from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

class PDF(FileHandler):
    def read(self):
        return 'PDF content'

class CSV(FileHandler):
    def read(self):
        return 'CSV content'

class JSONFile(FileHandler):
    def read(self):
        return 'JSON content'

if __name__ == '__main__':
    files = [PDF(), CSV(), JSONFile()]
    for f in files:
        print(type(f).__name__, f.read())
