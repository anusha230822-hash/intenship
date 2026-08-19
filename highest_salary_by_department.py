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
    SELECT employee_id, name, department, salary
    FROM employees employee
    WHERE salary = (
        SELECT MAX(salary)
        FROM employees department_employee
        WHERE department_employee.department = employee.department
    )
    ORDER BY department
    """
)

print("Highest-paid employee in each department:")
for employee in cursor.fetchall():
    print(employee)

cursor.close()
connection.close()
