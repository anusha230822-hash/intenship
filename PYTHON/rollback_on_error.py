import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
try:
    cursor.execute(
        "INSERT INTO transaction_demo (id, message) VALUES (%s, %s)",
        (3, "This insert is rolled back after an error"),
    )
    raise RuntimeError("Demonstration error occurred after the insert.")
except (RuntimeError, mysql.connector.Error) as error:
    connection.rollback()
    print(f"Error detected: {error}")
    print("Transaction rolled back successfully.")
else:
    connection.commit()

cursor.close()
connection.close()
