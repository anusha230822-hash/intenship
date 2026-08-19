import os
from datetime import date

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )


def add_order(order_id, customer_id, amount, order_date=None):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO relationship_orders (order_id, customer_id, order_date, amount) VALUES (%s, %s, %s, %s)",
        (order_id, customer_id, order_date or date.today(), amount),
    )
    connection.commit()
    print("Order added successfully.")
    cursor.close()
    connection.close()


def get_orders():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT order_id, customer_id, order_date, amount FROM relationship_orders ORDER BY order_date"
    )
    orders = cursor.fetchall()
    cursor.close()
    connection.close()
    return orders


def update_order(order_id, amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE relationship_orders SET amount = %s WHERE order_id = %s",
        (amount, order_id),
    )
    connection.commit()
    print(f"Order updated. Rows changed: {cursor.rowcount}")
    cursor.close()
    connection.close()


def delete_order(order_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM relationship_orders WHERE order_id = %s", (order_id,))
    connection.commit()
    print(f"Order deleted. Rows deleted: {cursor.rowcount}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    print("Orders:")
    for order in get_orders():
        print(order)
