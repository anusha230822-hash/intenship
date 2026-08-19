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
    SELECT customer_name, COUNT(order_id) AS order_count
    FROM relationship_customers
    JOIN relationship_orders USING (customer_id)
    GROUP BY customer_id, customer_name
    HAVING COUNT(order_id) > 1
    """
)

print("Customers who placed more than one order:")
for customer_name, order_count in cursor.fetchall():
    print(f"{customer_name}: {order_count} orders")

cursor.close()
connection.close()
