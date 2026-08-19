import os

import mysql.connector


class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("MYSQL_PASSWORD", ""),
            database="college_db",
        )
        self.cursor = self.connection.cursor()
        self.row_count = 0

    def execute(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        self.row_count = self.cursor.rowcount

    def fetch_one(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        return self.cursor.fetchone()

    def fetch_all(self, query, parameters=()):
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
        print("Database changes committed successfully.")

    def rollback(self):
        self.connection.rollback()
        print("Database changes rolled back successfully.")

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    manager = DatabaseManager()
    print("Database connection established successfully.")
    manager.close()
