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
    CREATE TABLE IF NOT EXISTS inventory_products (
        product_id INT PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        stock_quantity INT NOT NULL
    )
    """
)
connection.commit()

cursor.execute(
    "SELECT COALESCE(SUM(price * stock_quantity), 0) FROM inventory_products"
)
total_inventory_value = cursor.fetchone()[0]
print(f"Total inventory value: Rs. {total_inventory_value}")

cursor.close()
connection.close()
