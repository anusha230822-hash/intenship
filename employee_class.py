from database_manager import DatabaseManager


class Employee:
    def __init__(self):
        self.database = DatabaseManager()

    def create(self, employee_id, name, department, salary, joining_date):
        self.database.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", (employee_id, name, department, salary, joining_date))
        self.database.commit()
        print("Employee inserted successfully.")

    def read(self):
        return self.database.fetch_all("SELECT employee_id, name, department, salary, joining_date FROM employees")

    def update(self, employee_id, department, salary):
        self.database.execute("UPDATE employees SET department = %s, salary = %s WHERE employee_id = %s", (department, salary, employee_id))
        self.database.commit()
        print(f"Employee updated. Rows changed: {self.database.row_count}")

    def delete(self, employee_id):
        self.database.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))
        self.database.commit()
        print(f"Employee deleted. Rows deleted: {self.database.row_count}")

    def close(self):
        self.database.close()
