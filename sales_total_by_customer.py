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
    SELECT customer_name, COALESCE(SUM(amount), 0) AS total_sales
    FROM relationship_customers
    LEFT JOIN relationship_orders USING (customer_id)
    GROUP BY customer_id, customer_name
    ORDER BY total_sales DESC
    """
)

print("Total sales for each customer:")
for customer_name, total_sales in cursor.fetchall():
    print(f"{customer_name}: Rs. {total_sales}")

cursor.close()
connection.close()
