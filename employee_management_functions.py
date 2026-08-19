import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )


def add_employee(employee_id, name, department, salary, joining_date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO employees (employee_id, name, department, salary, joining_date) VALUES (%s, %s, %s, %s, %s)",
        (employee_id, name, department, salary, joining_date),
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("Employee added successfully.")


def get_employees():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT employee_id, name, department, salary, joining_date FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees


def update_employee(employee_id, department, salary):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE employees SET department = %s, salary = %s WHERE employee_id = %s",
        (department, salary, employee_id),
    )
    connection.commit()
    print(f"Employee updated. Rows changed: {cursor.rowcount}")
    cursor.close()
    connection.close()


def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))
    connection.commit()
    print(f"Employee deleted. Rows deleted: {cursor.rowcount}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    print("Employees:")
    for employee in get_employees():
        print(employee)
