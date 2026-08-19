import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )


def add_product(product_id, name, price, stock_quantity):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO inventory_products (product_id, product_name, price, stock_quantity) VALUES (%s, %s, %s, %s)",
        (product_id, name, price, stock_quantity),
    )
    connection.commit()
    print("Product added successfully.")
    cursor.close()
    connection.close()


def get_products():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, product_name, price, stock_quantity FROM inventory_products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products


def update_product(product_id, price, stock_quantity):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE inventory_products SET price = %s, stock_quantity = %s WHERE product_id = %s",
        (price, stock_quantity, product_id),
    )
    connection.commit()
    print(f"Product updated. Rows changed: {cursor.rowcount}")
    cursor.close()
    connection.close()


def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory_products WHERE product_id = %s", (product_id,))
    connection.commit()
    print(f"Product deleted. Rows deleted: {cursor.rowcount}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    print("Products:")
    for product in get_products():
        print(product)
