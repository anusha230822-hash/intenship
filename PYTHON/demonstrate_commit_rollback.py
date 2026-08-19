import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS transaction_demo (
        id INT PRIMARY KEY,
        message VARCHAR(100) NOT NULL
    )
    """
)
connection.commit()

try:
    cursor.execute(
        "INSERT INTO transaction_demo (id, message) VALUES (%s, %s)",
        (1, "This record is committed"),
    )
    connection.commit()
    print("First transaction committed successfully.")

    cursor.execute(
        "INSERT INTO transaction_demo (id, message) VALUES (%s, %s)",
        (2, "This record will be rolled back"),
    )
    connection.rollback()
    print("Second transaction rolled back successfully.")
except mysql.connector.Error as error:
    connection.rollback()
    print(f"Transaction failed and was rolled back: {error}")

cursor.close()
connection.close()
