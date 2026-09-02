from mysql_helper import connect


class CompleteProject:
    def __init__(self):
        self.connection = connect()
        self.cursor = self.connection.cursor()

    def setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS mini_project_items (id INT PRIMARY KEY, name VARCHAR(100), value DECIMAL(10,2))")
        self.connection.commit()

    def create(self, item_id, name, value):
        self.cursor.execute("INSERT INTO mini_project_items VALUES (%s, %s, %s)", (item_id, name, value))
        self.connection.commit()

    def read_with_aggregation(self):
        self.cursor.execute("SELECT COUNT(*), COALESCE(SUM(value), 0) FROM mini_project_items")
        return self.cursor.fetchone()

    def update(self, item_id, value):
        self.cursor.execute("UPDATE mini_project_items SET value = %s WHERE id = %s", (value, item_id))
        self.connection.commit()

    def transaction_demo(self):
        try:
            self.cursor.execute("UPDATE mini_project_items SET value = value + %s", (10,))
            self.connection.commit()
            print("Transaction committed.")
        except Exception as error:
            self.connection.rollback()
            print(f"Transaction rolled back: {error}")

    def close(self):
        self.cursor.close()
        self.connection.close()


def parameterized_search(project, name):
    project.cursor.execute("SELECT * FROM mini_project_items WHERE name = %s", (name,))
    return project.cursor.fetchall()


if __name__ == "__main__":
    project = CompleteProject()
    project.setup()
    print("Complete Python + MySQL project ready.")
    print("Count and total:", project.read_with_aggregation())
    project.close()
