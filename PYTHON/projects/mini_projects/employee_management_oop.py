from mysql_helper import connect


class EmployeeManager:
    def __init__(self, connection):
        self.connection = connection

    def setup(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mini_employees (id INT PRIMARY KEY, name VARCHAR(100), department VARCHAR(100), salary DECIMAL(10,2))")
        self.connection.commit()
        cursor.close()

    def create(self, employee_id, name, department, salary):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO mini_employees VALUES (%s, %s, %s, %s)", (employee_id, name, department, salary))
        self.connection.commit()
        cursor.close()

    def read(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM mini_employees")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def update(self, employee_id, salary):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE mini_employees SET salary = %s WHERE id = %s", (salary, employee_id))
        self.connection.commit()
        cursor.close()

    def delete(self, employee_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM mini_employees WHERE id = %s", (employee_id,))
        self.connection.commit()
        cursor.close()


if __name__ == "__main__":
    manager = EmployeeManager(connect())
    manager.setup()
    print("Employee Management System ready.")
    print("Employees:", manager.read())
