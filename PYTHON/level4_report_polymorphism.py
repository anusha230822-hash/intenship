from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        return 'PDF generated'

class ExcelReport(Report):
    def generate(self):
        return 'Excel generated'

if __name__ == '__main__':
    reps = [PDFReport(), ExcelReport()]
    for r in reps:
        print(type(r).__name__, r.generate())
