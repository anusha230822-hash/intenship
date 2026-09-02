from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start(self):
        pass

class OnlineCourse(Course):
    def start(self):
        return 'Online course started'

if __name__ == '__main__':
    print(OnlineCourse().start())
