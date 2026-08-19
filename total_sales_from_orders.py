import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM relationship_orders")
total_sales = cursor.fetchone()[0]
print(f"Total sales from orders: Rs. {total_sales}")

cursor.close()
connection.close()
