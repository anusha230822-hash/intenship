import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS college_db")
print("Database 'college_db' created successfully.")

cursor.close()
connection.close()
