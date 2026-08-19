import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS relationship_orders")
cursor.execute("DROP TABLE IF EXISTS relationship_customers")
cursor.execute(
    """
    CREATE TABLE relationship_customers (
        customer_id INT PRIMARY KEY,
        customer_name VARCHAR(100) NOT NULL
    )
    """
)
cursor.execute(
    """
    CREATE TABLE relationship_orders (
        order_id INT PRIMARY KEY,
        customer_id INT NOT NULL,
        order_date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        CONSTRAINT fk_order_customer
            FOREIGN KEY (customer_id) REFERENCES relationship_customers(customer_id)
    )
    """
)
cursor.executemany(
    "INSERT INTO relationship_customers VALUES (%s, %s)",
    [(1, "Anusha"), (2, "Rahul"), (3, "Priya")],
)
cursor.executemany(
    "INSERT INTO relationship_orders VALUES (%s, %s, %s, %s)",
    [
        (1001, 1, "2026-01-10", 1500),
        (1002, 1, "2026-02-15", 2300),
        (1003, 2, "2026-03-20", 1800),
    ],
)
connection.commit()
print("Customers and orders tables created with a foreign-key relationship.")

cursor.close()
connection.close()
