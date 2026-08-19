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
    SELECT department, AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
    ORDER BY department
    """
)

print("Average salary for each department:")
for department, average_salary in cursor.fetchall():
    print(f"{department}: Rs. {average_salary:.2f}")

cursor.close()
connection.close()
