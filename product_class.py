from database_manager import DatabaseManager


class Product:
    def __init__(self):
        self.database = DatabaseManager()

    def add(self, product_id, name, price, stock_quantity):
        self.database.execute(
            "INSERT INTO inventory_products (product_id, product_name, price, stock_quantity) VALUES (%s, %s, %s, %s)",
            (product_id, name, price, stock_quantity),
        )
        self.database.commit()
        print("Product added successfully.")

    def update(self, product_id, price, stock_quantity):
        self.database.execute(
            "UPDATE inventory_products SET price = %s, stock_quantity = %s WHERE product_id = %s",
            (price, stock_quantity, product_id),
        )
        self.database.commit()
        print(f"Product updated. Rows changed: {self.database.row_count}")

    def delete(self, product_id):
        self.database.execute("DELETE FROM inventory_products WHERE product_id = %s", (product_id,))
        self.database.commit()
        print(f"Product deleted. Rows deleted: {self.database.row_count}")

    def search(self, name):
        return self.database.fetch_all(
            "SELECT product_id, product_name, price, stock_quantity FROM inventory_products WHERE product_name LIKE %s",
            (f"%{name}%",),
        )

    def close(self):
        self.database.close()


if __name__ == "__main__":
    product = Product()
    print(product.search("Laptop"))
    product.close()
