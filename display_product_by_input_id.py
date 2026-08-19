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
    CREATE TABLE IF NOT EXISTS products (
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        category VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    )
    """
)
connection.commit()

product_id = int(input("Enter product ID: "))
cursor.execute(
    "SELECT id, name, category, price FROM products WHERE id = %s",
    (product_id,),
)
product = cursor.fetchone()

if product:
    print("Product information:")
    print("ID | Name | Category | Price")
    print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")
else:
    print("Product not found.")

cursor.close()
connection.close()
