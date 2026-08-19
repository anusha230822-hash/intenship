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
    SELECT customer_name, order_id, order_date, amount
    FROM relationship_customers
    JOIN relationship_orders USING (customer_id)
    ORDER BY customer_name, order_date
    """
)

print("Customers with their orders:")
for customer_name, order_id, order_date, amount in cursor.fetchall():
    print(f"{customer_name} | Order {order_id} | {order_date} | Rs. {amount}")

cursor.close()
connection.close()
