from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_departments (id INT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_teachers (id INT PRIMARY KEY, name VARCHAR(100), department_id INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_college_students (id INT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_courses (id INT PRIMARY KEY, name VARCHAR(100), teacher_id INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_enrollments (student_id INT, course_id INT, PRIMARY KEY (student_id, course_id))")
    connection.commit()
    cursor.close()


def enroll(connection, student_id, course_id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mini_enrollments VALUES (%s, %s)", (student_id, course_id))
    connection.commit()
    cursor.close()


def student_courses(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT s.name, c.name FROM mini_college_students s JOIN mini_enrollments e ON s.id = e.student_id JOIN mini_courses c ON c.id = e.course_id")
    rows = cursor.fetchall()
    cursor.close()
    return rows


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("College Management System ready.")
    database.close()
