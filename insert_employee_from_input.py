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
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department VARCHAR(100) NOT NULL,
        salary DECIMAL(10, 2) NOT NULL
    )
    """
)

employee = (
    int(input("Enter employee ID: ")),
    input("Enter employee name: "),
    input("Enter department: "),
    float(input("Enter salary: ")),
)
query = "INSERT INTO employees (id, name, department, salary) VALUES (%s, %s, %s, %s)"
cursor.execute(query, employee)
connection.commit()
print("Employee details inserted successfully.")

cursor.close()
connection.close()
