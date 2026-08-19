import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

table_name = input("Enter table name: ")
allowed_tables = {"students", "employees", "products", "orders"}
if table_name not in allowed_tables:
    print("Invalid table name.")
else:
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_records = cursor.fetchone()[0]
    print(f"Total records in {table_name}: {total_records}")
    cursor.close()

connection.close()
