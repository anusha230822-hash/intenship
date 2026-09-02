-- SQLite3 Final Challenge - Student Management System
-- Create the main students table for the management system

CREATE TABLE IF NOT EXISTS students_management (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL NOT NULL CHECK(marks >= 0 AND marks <= 100),
    course TEXT NOT NULL,
    enrollment_date TEXT DEFAULT CURRENT_DATE
);
