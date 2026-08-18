from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self, path):
        pass

class PDFReport(Report):
    def generate(self):
        return "PDF report generated"
    def export(self, path):
        return f"Exported PDF to {path}"

class ExcelReport(Report):
    def generate(self):
        return "Excel report generated"
    def export(self, path):
        return f"Exported Excel to {path}"

if __name__ == "__main__":
    p = PDFReport()
    e = ExcelReport()
    print(p.generate())
    print(p.export('report.pdf'))
    print(e.generate())
    print(e.export('report.xlsx'))
