import os

import mysql.connector


def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )


def execute(connection, query, parameters=()):
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    cursor.close()
