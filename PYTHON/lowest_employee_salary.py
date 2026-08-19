import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT MIN(salary) FROM employees")
lowest_salary = cursor.fetchone()[0]
print(f"Lowest employee salary: Rs. {lowest_salary}")

cursor.close()
connection.close()
