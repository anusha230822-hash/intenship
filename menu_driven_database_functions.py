import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )


def add_student(cursor, connection):
    student = (
        int(input("Enter ID: ")),
        input("Enter name: "),
        int(input("Enter age: ")),
        input("Enter course: "),
        float(input("Enter marks: ")),
    )
    cursor.execute(
        "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
        student,
    )
    connection.commit()
    print("Student added successfully.")


def list_students(cursor):
    cursor.execute("SELECT id, name, age, course, marks FROM students ORDER BY id")
    students = cursor.fetchall()
    for student in students:
        print(student)
    if not students:
        print("No students found.")


def search_student(cursor):
    student_id = int(input("Enter student ID: "))
    cursor.execute(
        "SELECT id, name, age, course, marks FROM students WHERE id = %s",
        (student_id,),
    )
    student = cursor.fetchone()
    print(student if student else "Student not found.")


def update_student_marks(cursor, connection):
    student_id = int(input("Enter student ID: "))
    marks = float(input("Enter new marks: "))
    cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (marks, student_id))
    connection.commit()
    print(f"Student updated. Rows changed: {cursor.rowcount}")


def delete_student(cursor, connection):
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    connection.commit()
    print(f"Student deleted. Rows deleted: {cursor.rowcount}")


def main():
    connection = get_connection()
    cursor = connection.cursor()
    actions = {
        "1": lambda: add_student(cursor, connection),
        "2": lambda: list_students(cursor),
        "3": lambda: search_student(cursor),
        "4": lambda: update_student_marks(cursor, connection),
        "5": lambda: delete_student(cursor, connection),
    }
    try:
        while True:
            print("\nDatabase Menu")
            print("1. Add student")
            print("2. List students")
            print("3. Search student")
            print("4. Update marks")
            print("5. Delete student")
            print("6. Exit")
            choice = input("Enter choice: ")
            if choice == "6":
                print("Exiting database application.")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice.")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
