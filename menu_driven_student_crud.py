import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="college_db",
    )


def display_students(cursor, students):
    if not students:
        print("No student records found.")
        return
    print("ID | Name | Age | Course | Marks")
    for student_id, name, age, course, marks in students:
        print(f"{student_id} | {name} | {age} | {course} | {marks}")


def main():
    connection = get_connection()
    cursor = connection.cursor()

    while True:
        print("\nStudent CRUD Menu")
        print("1. Insert student")
        print("2. Display all students")
        print("3. Update student marks")
        print("4. Delete student")
        print("5. Search student by ID")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student = (
                int(input("Enter student ID: ")),
                input("Enter student name: "),
                int(input("Enter student age: ")),
                input("Enter student course: "),
                float(input("Enter student marks: ")),
            )
            cursor.execute(
                "INSERT INTO students (id, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)",
                student,
            )
            connection.commit()
            print("Student inserted successfully.")
        elif choice == "2":
            cursor.execute("SELECT id, name, age, course, marks FROM students")
            display_students(cursor, cursor.fetchall())
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            new_marks = float(input("Enter new marks: "))
            cursor.execute(
                "UPDATE students SET marks = %s WHERE id = %s",
                (new_marks, student_id),
            )
            connection.commit()
            print(f"Student marks updated. Rows changed: {cursor.rowcount}")
        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            connection.commit()
            print(f"Student deleted. Rows deleted: {cursor.rowcount}")
        elif choice == "5":
            student_id = int(input("Enter student ID to search: "))
            cursor.execute(
                "SELECT id, name, age, course, marks FROM students WHERE id = %s",
                (student_id,),
            )
            display_students(cursor, cursor.fetchall())
        elif choice == "6":
            print("Exiting the CRUD menu.")
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
