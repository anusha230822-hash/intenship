import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT AVG(salary) FROM employees")
average_salary = cursor.fetchone()[0]
print(f"Average employee salary: Rs. {average_salary:.2f}")

cursor.close()
connection.close()
