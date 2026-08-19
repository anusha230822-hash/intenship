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
    SELECT employee_id, name, department, salary, joining_date
    FROM employees
    WHERE salary > %s
    """,
    (50000,),
)
employees = cursor.fetchall()

print("Employees with salary greater than Rs. 50,000:")
for employee in employees:
    print(employee)

cursor.close()
connection.close()
