import sqlite3

# Questions 1 and 2: Connect to college.db and create the students table.
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        marks REAL
    )
""")

# Questions 25 and 26: Create courses and enrollments with relationships.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT UNIQUE
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
""")
connection.commit()


def display(rows):
    for row in rows:
        print(row)
    if not rows:
        print("No records found.")


def insert_five_students():
    # Questions 3 and 4: Insert five records and display all students.
    students = [
        (1, "Anu", 20, "Python", 88),
        (2, "king", 21, "Java", 74),
        (3, "manoj", 19, "Python", 93),
        (4, "yashu", 22, "SQL", 67),
        (5, "teju", 20, "Web Development", 81)
    ]
    for student in students:
        try:
            cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)
        except sqlite3.IntegrityError:
            pass
    connection.commit()


def insert_ten_students():
    # Question 11: Insert ten records using executemany().
    students = [(i, "Student" + str(i), 18, "Python", 60 + i) for i in range(10, 20)]
    try:
        cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", students)
        connection.commit()
        print("10 students inserted successfully.")
    except sqlite3.Error as error:
        connection.rollback()
        print("Insert failed. Rollback completed:", error)


def show_basic_queries():
    # Questions 5 to 10: Basic SELECT, WHERE, course, ID, update, and delete examples.
    print("\nALL STUDENTS")
    cursor.execute("SELECT * FROM students")
    display(cursor.fetchall())

    print("\nSTUDENT NAMES")
    cursor.execute("SELECT name FROM students")
    display(cursor.fetchall())

    print("\nMARKS MORE THAN 75")
    cursor.execute("SELECT * FROM students WHERE marks > ?", (75,))
    display(cursor.fetchall())

    print("\nPYTHON STUDENTS")
    cursor.execute("SELECT * FROM students WHERE course = ?", ("Python",))
    display(cursor.fetchall())

    print("\nSTUDENT WITH ID 1")
    cursor.execute("SELECT * FROM students WHERE id = ?", (1,))
    display(cursor.fetchall())

    # Questions 12 and 13: ORDER BY and the top three students.
    print("\nMARKS IN DESCENDING ORDER")
    cursor.execute("SELECT * FROM students ORDER BY marks DESC")
    display(cursor.fetchall())

    print("\nTOP 3 STUDENTS")
    cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
    display(cursor.fetchall())

    # Questions 19 and 20: Name search and marks between 60 and 90.
    print("\nMARKS BETWEEN 60 AND 90")
    cursor.execute("SELECT * FROM students WHERE marks BETWEEN ? AND ?", (60, 90))
    display(cursor.fetchall())

    # Questions 14, 15, and 16: Aggregate functions.
    print("\nCOUNT, AVERAGE, HIGHEST, LOWEST")
    cursor.execute("SELECT COUNT(*), AVG(marks), MAX(marks), MIN(marks) FROM students")
    print(cursor.fetchone())

    # Questions 17 and 18: GROUP BY course.
    print("\nCOURSE-WISE COUNT AND AVERAGE")
    cursor.execute("""
        SELECT course, COUNT(*), AVG(marks)
        FROM students
        GROUP BY course
    """)
    display(cursor.fetchall())


def show_relationship_queries():
    # Questions 27, 28, and 29: JOIN, students without courses, and course counts.
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("INSERT OR IGNORE INTO courses (course_name) SELECT DISTINCT course FROM students")
    cursor.execute("""
        INSERT INTO enrollments (student_id, course_id)
        SELECT students.id, courses.course_id
        FROM students JOIN courses ON students.course = courses.course_name
        WHERE NOT EXISTS (
            SELECT * FROM enrollments WHERE enrollments.student_id = students.id
        )
    """)
    connection.commit()

    print("\nSTUDENT NAMES WITH COURSE NAMES")
    cursor.execute("""
        SELECT students.name, courses.course_name
        FROM students
        JOIN enrollments ON students.id = enrollments.student_id
        JOIN courses ON enrollments.course_id = courses.course_id
    """)
    display(cursor.fetchall())

    print("\nNUMBER OF STUDENTS IN EACH COURSE")
    cursor.execute("""
        SELECT courses.course_name, COUNT(enrollments.student_id)
        FROM courses
        LEFT JOIN enrollments ON courses.course_id = enrollments.course_id
        GROUP BY courses.course_id
    """)
    display(cursor.fetchall())

    print("\nSTUDENTS WITHOUT A COURSE")
    cursor.execute("""
        SELECT students.name FROM students
        LEFT JOIN enrollments ON students.id = enrollments.student_id
        WHERE enrollments.student_id IS NULL
    """)
    display(cursor.fetchall())


def menu():
    # Questions 21, 22, and 23: Menu, try-except, and parameterized queries.
    while True:
        print("""
1. Add student
2. View all students
3. Search student by name
4. Update marks
5. Delete student
6. Show top 3 students
7. Show course statistics
8. Show average marks
9. Show student count
10. Show all SQL examples
11. Insert 10 students using executemany()
12. Exit
""")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                student = (
                    int(input("Enter ID: ")), input("Enter name: "),
                    int(input("Enter age: ")), input("Enter course: "),
                    float(input("Enter marks: "))
                )
                cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)
                connection.commit()
                print("Student added successfully.")
            elif choice == "2":
                cursor.execute("SELECT * FROM students")
                display(cursor.fetchall())
            elif choice == "3":
                name = input("Enter name: ")
                cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("%" + name + "%",))
                display(cursor.fetchall())
            elif choice == "4":
                student_id = int(input("Enter student ID: "))
                marks = float(input("Enter new marks: "))
                cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
                connection.commit()
                print(cursor.rowcount, "student updated.")
            elif choice == "5":
                student_id = int(input("Enter student ID: "))
                cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
                connection.commit()
                print(cursor.rowcount, "student deleted.")
            elif choice == "6":
                cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
                display(cursor.fetchall())
            elif choice == "7":
                cursor.execute("SELECT course, COUNT(*), AVG(marks) FROM students GROUP BY course")
                display(cursor.fetchall())
            elif choice == "8":
                cursor.execute("SELECT AVG(marks) FROM students")
                print("Average marks:", cursor.fetchone()[0])
            elif choice == "9":
                cursor.execute("SELECT COUNT(*) FROM students")
                print("Student count:", cursor.fetchone()[0])
            elif choice == "10":
                show_basic_queries()
                show_relationship_queries()
            elif choice == "11":
                insert_ten_students()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, sqlite3.Error) as error:
            connection.rollback()
            print("Error:", error)


# Insert the first five records and start the menu
insert_five_students()
menu()
connection.close()