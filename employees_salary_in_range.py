import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

minimum_salary = float(input("Enter minimum salary: "))
maximum_salary = float(input("Enter maximum salary: "))
query = """
    SELECT employee_id, name, department, salary, joining_date
    FROM employees
    WHERE salary BETWEEN %s AND %s
    ORDER BY salary
"""

cursor = connection.cursor()
cursor.execute(query, (minimum_salary, maximum_salary))

print(f"Employees with salary between Rs. {minimum_salary:g} and Rs. {maximum_salary:g}:")
for employee in cursor.fetchall():
    print(employee)

cursor.close()
connection.close()
