-- SQLite3 Practice - Part A: Basic SQL
-- Question 1: Create Students Table
-- Create a table with id, name, marks, and course columns

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL NOT NULL,
    course TEXT NOT NULL
);
