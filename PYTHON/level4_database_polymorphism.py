from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return "Connected MySQL"

class PostgreSQL(Database):
    def connect(self):
        return "Connected PostgreSQL"

class SQLite(Database):
    def connect(self):
        return "Connected SQLite"

if __name__ == '__main__':
    dbs = [MySQL(), PostgreSQL(), SQLite()]
    for db in dbs:
        print(type(db).__name__, db.connect())
