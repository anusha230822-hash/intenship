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
    SELECT department_name
    FROM relationship_departments
    LEFT JOIN relationship_employees USING (department_id)
    WHERE employee_id IS NULL
    """
)

print("Departments with no employees:")
for (department_name,) in cursor.fetchall():
    print(department_name)

cursor.close()
connection.close()
