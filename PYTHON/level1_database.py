from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL"

if __name__ == "__main__":
    print(MySQLDatabase().connect())
    print(PostgreSQLDatabase().connect())
