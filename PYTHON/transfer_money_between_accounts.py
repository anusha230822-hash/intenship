import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

source_account = int(input("Enter source account ID: "))
target_account = int(input("Enter target account ID: "))
amount = float(input("Enter transfer amount: "))
cursor = connection.cursor()

try:
    if amount <= 0 or source_account == target_account:
        raise ValueError("Use two different accounts and a positive amount.")

    cursor.execute(
        "UPDATE bank_accounts SET balance = balance - %s "
        "WHERE account_id = %s AND balance >= %s",
        (amount, source_account, amount),
    )
    if cursor.rowcount != 1:
        raise ValueError("Source account not found or has insufficient balance.")

    cursor.execute(
        "UPDATE bank_accounts SET balance = balance + %s WHERE account_id = %s",
        (amount, target_account),
    )
    if cursor.rowcount != 1:
        raise ValueError("Target account not found.")

    connection.commit()
    print("Money transfer completed successfully.")
except (ValueError, mysql.connector.Error) as error:
    connection.rollback()
    print(f"Transfer failed. All changes were rolled back: {error}")

cursor.close()
connection.close()
