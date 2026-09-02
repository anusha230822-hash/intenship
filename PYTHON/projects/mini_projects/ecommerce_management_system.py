from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_customers (id INT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_products (id INT PRIMARY KEY, name VARCHAR(100), price DECIMAL(10,2), stock INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_orders (id INT PRIMARY KEY, customer_id INT, product_id INT, quantity INT, FOREIGN KEY (customer_id) REFERENCES mini_customers(id), FOREIGN KEY (product_id) REFERENCES mini_products(id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_payments (id INT PRIMARY KEY, order_id INT, amount DECIMAL(10,2), status VARCHAR(30))")
    connection.commit()
    cursor.close()


def place_order(connection, order_id, customer_id, product_id, quantity):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT price, stock FROM mini_products WHERE id = %s FOR UPDATE", (product_id,))
        product = cursor.fetchone()
        if not product or product[1] < quantity:
            raise ValueError("Product unavailable or stock is insufficient.")
        cursor.execute("INSERT INTO mini_orders VALUES (%s, %s, %s, %s)", (order_id, customer_id, product_id, quantity))
        cursor.execute("UPDATE mini_products SET stock = stock - %s WHERE id = %s", (quantity, product_id))
        cursor.execute("INSERT INTO mini_payments VALUES (%s, %s, %s, %s)", (order_id, order_id, product[0] * quantity, "PAID"))
        connection.commit()
        print("Order, payment, and inventory update committed.")
    except (ValueError, Exception) as error:
        connection.rollback()
        print(f"E-commerce transaction rolled back: {error}")
    cursor.close()


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("E-Commerce Management System ready.")
    database.close()
