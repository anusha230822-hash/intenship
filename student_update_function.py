import os

import mysql.connector


def update_student(student_id, name=None, age=None, course=None, marks=None):
    updates = []
    values = []
    for column, value in (("name", name), ("age", age), ("course", course), ("marks", marks)):
        if value is not None:
            updates.append(f"{column} = %s")
            values.append(value)
    if not updates:
        raise ValueError("Provide at least one student detail to update.")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )
    cursor = connection.cursor()
    values.append(student_id)
    cursor.execute(
        f"UPDATE students SET {', '.join(updates)} WHERE id = %s",
        tuple(values),
    )
    connection.commit()
    print(f"Student updated successfully. Rows changed: {cursor.rowcount}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    update_student(10, marks=90.0)
