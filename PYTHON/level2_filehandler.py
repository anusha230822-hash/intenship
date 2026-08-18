from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class PDFFile(FileHandler):
    def read(self):
        return "Reading PDF content"
    def write(self, data):
        return f"Writing to PDF: {data}"

class CSVFile(FileHandler):
    def read(self):
        return "Reading CSV content"
    def write(self, data):
        return f"Writing to CSV: {data}"

class ExcelFile(FileHandler):
    def read(self):
        return "Reading Excel content"
    def write(self, data):
        return f"Writing to Excel: {data}"

if __name__ == "__main__":
    for f in (PDFFile(), CSVFile(), ExcelFile()):
        print(f.read())
        print(f.write('data'))
