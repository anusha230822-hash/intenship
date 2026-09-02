-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 1: Create Students Table for Intermediate Level

CREATE TABLE IF NOT EXISTS students_intermediate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL NOT NULL,
    course TEXT NOT NULL
);
