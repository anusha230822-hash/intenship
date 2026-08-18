from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        return f"Logged to file: {message}"

class DatabaseLogger(Logger):
    def log(self, message):
        return f"Logged to database: {message}"

class ConsoleLogger(Logger):
    def log(self, message):
        return f"Console: {message}"

if __name__ == '__main__':
    loggers = [FileLogger(), DatabaseLogger(), ConsoleLogger()]
    for l in loggers:
        print(type(l).__name__, '-', l.log('Test message'))
