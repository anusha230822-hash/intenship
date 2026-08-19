import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

joining_date = input("Enter date (YYYY-MM-DD): ")
query = """
    SELECT employee_id, name, department, salary, joining_date
    FROM employees
    WHERE joining_date > %s
    ORDER BY joining_date
"""

cursor = connection.cursor()
cursor.execute(query, (joining_date,))

print(f"Employees who joined after {joining_date}:")
for employee in cursor.fetchall():
    print(employee)

cursor.close()
connection.close()
