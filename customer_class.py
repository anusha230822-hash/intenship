from database_manager import DatabaseManager


class Customer:
    def __init__(self):
        self.database = DatabaseManager()

    def add(self, customer_id, name):
        self.database.execute(
            "INSERT INTO relationship_customers (customer_id, customer_name) VALUES (%s, %s)",
            (customer_id, name),
        )
        self.database.commit()
        print("Customer added successfully.")

    def get_all(self):
        return self.database.fetch_all(
            "SELECT customer_id, customer_name FROM relationship_customers"
        )

    def update(self, customer_id, name):
        self.database.execute(
            "UPDATE relationship_customers SET customer_name = %s WHERE customer_id = %s",
            (name, customer_id),
        )
        self.database.commit()
        print(f"Customer updated. Rows changed: {self.database.row_count}")

    def delete(self, customer_id):
        self.database.execute(
            "DELETE FROM relationship_customers WHERE customer_id = %s",
            (customer_id,),
        )
        self.database.commit()
        print(f"Customer deleted. Rows deleted: {self.database.row_count}")

    def close(self):
        self.database.close()


if __name__ == "__main__":
    customer = Customer()
    print(customer.get_all())
    customer.close()
