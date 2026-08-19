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
    CREATE TABLE IF NOT EXISTS store_products (
        product_id INT PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        stock INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    )
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS store_orders (
        order_id INT PRIMARY KEY AUTO_INCREMENT,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        total_amount DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (product_id) REFERENCES store_products(product_id)
    )
    """
)
cursor.execute(
    """
    INSERT IGNORE INTO store_products (product_id, product_name, stock, price)
    VALUES (1, 'Laptop', 10, 55000)
    """
)
connection.commit()

product_id = int(input("Enter product ID: "))
quantity = int(input("Enter quantity: "))

try:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    cursor.execute(
        "SELECT price FROM store_products WHERE product_id = %s AND stock >= %s",
        (product_id, quantity),
    )
    product = cursor.fetchone()
    if product is None:
        raise ValueError("Product not found or insufficient stock.")

    total_amount = product[0] * quantity
    cursor.execute(
        "INSERT INTO store_orders (product_id, quantity, total_amount) VALUES (%s, %s, %s)",
        (product_id, quantity, total_amount),
    )
    cursor.execute(
        "UPDATE store_products SET stock = stock - %s WHERE product_id = %s",
        (quantity, product_id),
    )
    connection.commit()
    print("Order created and product stock updated successfully.")
except (ValueError, mysql.connector.Error) as error:
    connection.rollback()
    print(f"Order failed. Transaction rolled back: {error}")

cursor.close()
connection.close()
