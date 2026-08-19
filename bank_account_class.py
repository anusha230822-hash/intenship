from database_manager import DatabaseManager


class BankAccount:
    def __init__(self):
        self.database = DatabaseManager()

    def create(self, account_id, holder, balance):
        self.database.execute("INSERT INTO bank_accounts VALUES (%s, %s, %s)", (account_id, holder, balance))
        self.database.commit()
        print("Bank account created successfully.")

    def get_balance(self, account_id):
        return self.database.fetch_one("SELECT * FROM bank_accounts WHERE account_id = %s", (account_id,))

    def deposit(self, account_id, amount):
        self.database.execute("UPDATE bank_accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id))
        self.database.commit()
        print("Deposit completed successfully.")

    def withdraw(self, account_id, amount):
        self.database.execute("UPDATE bank_accounts SET balance = balance - %s WHERE account_id = %s AND balance >= %s", (amount, account_id, amount))
        self.database.commit()
        print(f"Withdrawal completed. Rows changed: {self.database.row_count}")

    def close(self):
        self.database.close()
