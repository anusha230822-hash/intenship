import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

letter = input("Enter the starting letter: ")
query = """
    SELECT employee_id, name, department, salary, joining_date
    FROM employees
    WHERE name LIKE %s
    ORDER BY name
"""

cursor = connection.cursor()
cursor.execute(query, (f"{letter}%",))

print(f"Employees whose names start with '{letter}':")
for employee in cursor.fetchall():
    print(employee)

cursor.close()
connection.close()
