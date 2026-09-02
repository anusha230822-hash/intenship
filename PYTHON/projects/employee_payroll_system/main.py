from abc import ABC, abstractmethod

class Payroll(ABC):
    @abstractmethod
    def compute(self):
        pass

class FullTime(Payroll):
    def compute(self):
        return 'Compute full time pay'

if __name__ == '__main__':
    print(FullTime().compute())
