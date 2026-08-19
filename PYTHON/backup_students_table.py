import os

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", ""),
    database="college_db",
)

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS students_backup")
cursor.execute("CREATE TABLE students_backup LIKE students")
cursor.execute("INSERT INTO students_backup SELECT * FROM students")
connection.commit()

cursor.execute("SELECT COUNT(*) FROM students_backup")
backup_count = cursor.fetchone()[0]
print(f"Students backup table created successfully with {backup_count} records.")

cursor.close()
connection.close()
