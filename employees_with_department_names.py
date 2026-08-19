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
    SELECT employee_name, department_name
    FROM relationship_employees
    LEFT JOIN relationship_departments USING (department_id)
    ORDER BY employee_name
    """
)

print("Employees with department names:")
for employee_name, department_name in cursor.fetchall():
    print(f"{employee_name} | {department_name}")

cursor.close()
connection.close()
