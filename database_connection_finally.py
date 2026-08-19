import os

import mysql.connector


connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )
    print("Database connection successful.")
except mysql.connector.Error as error:
    print(f"Database connection failed: {error}")
finally:
    if connection is not None and connection.is_connected():
        connection.close()
        print("Database connection closed in finally.")
