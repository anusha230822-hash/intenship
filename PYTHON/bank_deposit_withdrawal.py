import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS bank_accounts (
        account_id INT PRIMARY KEY,
        account_holder VARCHAR(100) NOT NULL,
        balance DECIMAL(12, 2) NOT NULL DEFAULT 0
    )
    """
)
cursor.executemany(
    "INSERT IGNORE INTO bank_accounts (account_id, account_holder, balance) VALUES (%s, %s, %s)",
    [(1, "Anusha", 10000), (2, "Rahul", 5000)],
)
connection.commit()

account_id = int(input("Enter account ID: "))
operation = input("Enter operation (deposit/withdraw): ").lower()
amount = float(input("Enter amount: "))

try:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if operation == "deposit":
        cursor.execute(
            "UPDATE bank_accounts SET balance = balance + %s WHERE account_id = %s",
            (amount, account_id),
        )
    elif operation == "withdraw":
        cursor.execute(
            "UPDATE bank_accounts SET balance = balance - %s "
            "WHERE account_id = %s AND balance >= %s",
            (amount, account_id, amount),
        )
    else:
        raise ValueError("Choose deposit or withdraw.")

    if cursor.rowcount != 1:
        raise ValueError("Account not found or insufficient balance.")
    connection.commit()
    print(f"{operation.title()} completed successfully.")
except (ValueError, mysql.connector.Error) as error:
    connection.rollback()
    print(f"Operation failed and was rolled back: {error}")

cursor.close()
connection.close()
