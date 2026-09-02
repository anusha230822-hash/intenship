-- SQLite3 Practice - Part A: Basic SQL
-- Question 1: Create Students Table
-- Expected Output: Table created successfully

-- SQL Query:
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL NOT NULL,
    course TEXT NOT NULL
);

-- Expected Output:
-- ✓ Table created successfully
-- (No output means success in SQLite3)
