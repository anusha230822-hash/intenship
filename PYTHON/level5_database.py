from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    def display_database_name(self):
        return "DefaultDB"

class MySQL(Database):
    def connect(self):
        return "Connected MySQL"

class PostgreSQL(Database):
    def connect(self):
        return "Connected PostgreSQL"

if __name__ == '__main__':
    print(MySQL().connect(), MySQL().display_database_name())
    print(PostgreSQL().connect(), PostgreSQL().display_database_name())
