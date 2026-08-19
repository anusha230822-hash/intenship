import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT MAX(salary) FROM employees")
highest_salary = cursor.fetchone()[0]
print(f"Highest employee salary: Rs. {highest_salary}")

cursor.close()
connection.close()
