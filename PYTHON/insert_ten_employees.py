import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

employees = [
    (101, "Anusha", "IT", 75000, "2021-06-15"),
    (102, "Rahul", "HR", 52000, "2020-03-10"),
    (103, "Priya", "IT", 68000, "2022-01-20"),
    (104, "Vikram", "Finance", 60000, "2019-11-05"),
    (105, "Neha", "Sales", 48000, "2023-04-12"),
    (106, "Arjun", "IT", 82000, "2018-08-25"),
    (107, "Sneha", "HR", 55000, "2021-09-18"),
    (108, "Karan", "Finance", 71000, "2020-12-01"),
    (109, "Meera", "Sales", 45000, "2024-02-14"),
    (110, "Rohan", "IT", 90000, "2017-07-30"),
]
query = """
    INSERT INTO employees
    (employee_id, name, department, salary, joining_date)
    VALUES (%s, %s, %s, %s, %s)
"""

cursor = connection.cursor()
cursor.executemany(query, employees)
connection.commit()
print(f"{cursor.rowcount} employee records inserted successfully.")

cursor.close()
connection.close()
