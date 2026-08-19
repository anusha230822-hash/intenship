import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

if connection.is_connected():
    print("Successfully connected to the MySQL database 'college_db'.")

connection.close()
