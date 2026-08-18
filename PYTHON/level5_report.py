from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        return "Report info"

class PDFReport(Report):
    def generate(self):
        return "PDF generated"

class ExcelReport(Report):
    def generate(self):
        return "Excel generated"

if __name__ == '__main__':
    print(PDFReport().generate(), PDFReport().display_report_info())
    print(ExcelReport().generate(), ExcelReport().display_report_info())
