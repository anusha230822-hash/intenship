from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start_course(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass

class OnlineCourse(Course):
    def __init__(self, duration):
        self.duration = duration
    def start_course(self):
        return "Starting online course"
    def get_duration(self):
        return self.duration

class OfflineCourse(Course):
    def __init__(self, duration):
        self.duration = duration
    def start_course(self):
        return "Starting offline course"
    def get_duration(self):
        return self.duration

if __name__ == "__main__":
    o = OnlineCourse('6 weeks')
    off = OfflineCourse('8 weeks')
    print(o.start_course(), o.get_duration())
    print(off.start_course(), off.get_duration())
