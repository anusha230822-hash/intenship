from database_manager import DatabaseManager


class BankAccount:
    def __init__(self):
        self.database = DatabaseManager()

    def create(self, account_id, holder, balance):
        self.database.execute(
            "INSERT INTO bank_accounts (account_id, account_holder, balance) VALUES (%s, %s, %s)",
            (account_id, holder, balance),
        )
        self.database.commit()
        print("Bank account created successfully.")

    def get_balance(self, account_id):
        result = self.database.fetch_one(
            "SELECT account_id, account_holder, balance FROM bank_accounts WHERE account_id = %s",
            (account_id,),
        )
        return result

    def deposit(self, account_id, amount):
        self.database.execute(
            "UPDATE bank_accounts SET balance = balance + %s WHERE account_id = %s",
            (amount, account_id),
        )
        self.database.commit()
        print("Deposit completed successfully.")

    def withdraw(self, account_id, amount):
        self.database.execute(
            "UPDATE bank_accounts SET balance = balance - %s WHERE account_id = %s AND balance >= %s",
            (amount, account_id, amount),
        )
        self.database.commit()
        print(f"Withdrawal completed. Rows changed: {self.database.row_count}")

    def close(self):
        self.database.close()


if __name__ == "__main__":
    account = BankAccount()
    print(account.get_balance(1))
    account.close()
