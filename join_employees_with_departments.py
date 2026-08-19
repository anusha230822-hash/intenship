import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS relationship_employees")
cursor.execute("DROP TABLE IF EXISTS relationship_departments")
cursor.execute(
    """
    CREATE TABLE relationship_departments (
        department_id INT PRIMARY KEY,
        department_name VARCHAR(100) NOT NULL
    )
    """
)
cursor.execute(
    """
    CREATE TABLE relationship_employees (
        employee_id INT PRIMARY KEY,
        employee_name VARCHAR(100) NOT NULL,
        department_id INT,
        CONSTRAINT fk_employee_department
            FOREIGN KEY (department_id) REFERENCES relationship_departments(department_id)
    )
    """
)
cursor.executemany(
    "INSERT INTO relationship_departments VALUES (%s, %s)",
    [(1, "IT"), (2, "HR"), (3, "Finance")],
)
cursor.executemany(
    "INSERT INTO relationship_employees VALUES (%s, %s, %s)",
    [(101, "Anusha", 1), (102, "Rahul", 2), (103, "Priya", 1)],
)
connection.commit()

cursor.execute(
    """
    SELECT employee_id, employee_name, department_name
    FROM relationship_employees
    JOIN relationship_departments USING (department_id)
    ORDER BY employee_id
    """
)
print("Employees with their department names:")
for employee in cursor.fetchall():
    print(employee)

cursor.close()
connection.close()
