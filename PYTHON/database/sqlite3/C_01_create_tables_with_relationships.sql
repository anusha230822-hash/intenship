-- SQLite3 Practice - Part C: Advanced SQL
-- Question 1: Create Three Tables with Relationships

-- Create courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL UNIQUE,
    credits INTEGER NOT NULL
);

-- Create students table (Advanced Level)
CREATE TABLE IF NOT EXISTS students_advanced (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL NOT NULL,
    gpa REAL
);

-- Create enrollments table (Junction/Relationship Table)
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date TEXT DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students_advanced(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
