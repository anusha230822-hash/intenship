from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        return "Course details displayed"

class Online(Course):
    def start(self):
        return "Online course started"

class Offline(Course):
    def start(self):
        return "Offline course started"

if __name__ == '__main__':
    print(Online().start(), Online().display_course_details())
    print(Offline().start(), Offline().display_course_details())
