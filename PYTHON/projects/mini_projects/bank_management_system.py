from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_accounts (id INT PRIMARY KEY, holder VARCHAR(100), balance DECIMAL(12,2))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_transactions (id INT AUTO_INCREMENT PRIMARY KEY, account_id INT, transaction_type VARCHAR(30), amount DECIMAL(12,2))")
    connection.commit()
    cursor.close()


def deposit(connection, account_id, amount):
    cursor = connection.cursor()
    cursor.execute("UPDATE mini_accounts SET balance = balance + %s WHERE id = %s", (amount, account_id))
    cursor.execute("INSERT INTO mini_transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)", (account_id, "DEPOSIT", amount))
    connection.commit()
    cursor.close()


def transfer(connection, source_id, target_id, amount):
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE mini_accounts SET balance = balance - %s WHERE id = %s AND balance >= %s", (amount, source_id, amount))
        if cursor.rowcount != 1:
            raise ValueError("Insufficient balance or source account missing.")
        cursor.execute("UPDATE mini_accounts SET balance = balance + %s WHERE id = %s", (amount, target_id))
        if cursor.rowcount != 1:
            raise ValueError("Target account missing.")
        connection.commit()
        print("Transfer committed successfully.")
    except (ValueError, Exception) as error:
        connection.rollback()
        print(f"Transfer rolled back: {error}")
    cursor.close()


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("Bank Management System ready.")
    database.close()
