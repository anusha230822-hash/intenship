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
    SELECT department, COUNT(*)
    FROM employees
    GROUP BY department
    ORDER BY department
    """
)

print("Employee count by department:")
for department, employee_count in cursor.fetchall():
    print(f"{department}: {employee_count}")

cursor.close()
connection.close()
