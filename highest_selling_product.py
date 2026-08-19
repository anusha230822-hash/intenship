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
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS product_sales (
        sale_id INT PRIMARY KEY,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES inventory_products(product_id)
    )
    """
)
connection.commit()

cursor.execute(
    """
    SELECT product_name, SUM(quantity) AS units_sold
    FROM inventory_products
    JOIN product_sales USING (product_id)
    GROUP BY product_id, product_name
    ORDER BY units_sold DESC
    LIMIT 1
    """
)
highest_selling_product = cursor.fetchone()
if highest_selling_product:
    print(
        f"Highest-selling product: {highest_selling_product[0]} "
        f"({highest_selling_product[1]} units)"
    )
else:
    print("No product sales found.")

cursor.close()
connection.close()
