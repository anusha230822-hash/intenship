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
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department VARCHAR(100) NOT NULL,
        salary DECIMAL(10, 2) NOT NULL,
        joining_date DATE NOT NULL
    )
    """
)
connection.commit()
print("Table 'employees' created successfully.")

cursor.close()
connection.close()
