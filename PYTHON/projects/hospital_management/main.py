from abc import ABC, abstractmethod

class HospitalEmployee(ABC):
    @abstractmethod
    def duty(self):
        pass

class Doctor(HospitalEmployee):
    def duty(self):
        return 'Treat patients'

if __name__ == '__main__':
    print(Doctor().duty())
