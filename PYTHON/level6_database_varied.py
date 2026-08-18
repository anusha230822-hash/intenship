from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        return 'Connected MySQL'

class PostgreSQL(Database):
    def connect(self):
        return 'Connected PostgreSQL'

class MongoDB(Database):
    def connect(self):
        return 'Connected MongoDB'

class SQLite(Database):
    def connect(self):
        return 'Connected SQLite'

if __name__ == '__main__':
    dbs = [MySQL(), PostgreSQL(), MongoDB(), SQLite()]
    for d in dbs:
        print(type(d).__name__, '-', d.connect())
