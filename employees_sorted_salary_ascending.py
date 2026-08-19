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
    ORDER BY salary ASC
    """
)

print("Employees sorted by salary in ascending order:")
for employee in cursor.fetchall():
    print(employee)

cursor.close()
connection.close()
