from database_manager import DatabaseManager


class Order:
    def __init__(self):
        self.database = DatabaseManager()

    def create(self, order_id, customer_id, order_date, amount):
        self.database.execute(
            "INSERT INTO relationship_orders (order_id, customer_id, order_date, amount) VALUES (%s, %s, %s, %s)",
            (order_id, customer_id, order_date, amount),
        )
        self.database.commit()
        print("Order created successfully.")

    def get_all(self):
        return self.database.fetch_all(
            "SELECT order_id, customer_id, order_date, amount FROM relationship_orders ORDER BY order_date"
        )

    def get_by_customer(self, customer_id):
        return self.database.fetch_all(
            "SELECT order_id, order_date, amount FROM relationship_orders WHERE customer_id = %s",
            (customer_id,),
        )

    def close(self):
        self.database.close()


if __name__ == "__main__":
    order = Order()
    print(order.get_all())
    order.close()
