import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT SUM(salary) FROM employees")
total_salary = cursor.fetchone()[0]
print(f"Total salary paid by the company: Rs. {total_salary}")

cursor.close()
connection.close()
