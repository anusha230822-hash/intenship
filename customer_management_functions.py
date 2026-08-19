import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )


def add_customer(customer_id, name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO relationship_customers (customer_id, customer_name) VALUES (%s, %s)",
        (customer_id, name),
    )
    connection.commit()
    print("Customer added successfully.")
    cursor.close()
    connection.close()


def get_customers():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT customer_id, customer_name FROM relationship_customers")
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return customers


def update_customer(customer_id, name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE relationship_customers SET customer_name = %s WHERE customer_id = %s",
        (name, customer_id),
    )
    connection.commit()
    print(f"Customer updated. Rows changed: {cursor.rowcount}")
    cursor.close()
    connection.close()


def delete_customer(customer_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM relationship_customers WHERE customer_id = %s", (customer_id,))
    connection.commit()
    print(f"Customer deleted. Rows deleted: {cursor.rowcount}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    print("Customers:")
    for customer in get_customers():
        print(customer)
