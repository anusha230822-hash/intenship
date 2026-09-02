-- SQLite3 Practice - Part A: Basic SQL
-- Question 10: Delete One Student
-- Expected Output: 1 row deleted, then verify deletion

-- SQL Query (Delete):
DELETE FROM students WHERE id = 5;

-- Expected Output after DELETE:
-- (No output means success)
-- ✓ 1 row(s) affected

-- Verification Query:
SELECT * FROM students;

-- Expected Output (Verification - 4 remaining records):
-- id | name             | marks | course
-- ---|------------------|-------|--------
-- 1  | Alice Johnson    | 85.5  | Python
-- 2  | Bob Smith        | 80.5  | Java
-- 3  | Charlie Davis    | 91.0  | Python
-- 4  | Diana Wilson     | 68.5  | C++
-- (Note: Eve Brown with id=5 is deleted)

-- Total Count:
SELECT COUNT(*) as total_students FROM students;

-- Expected Output:
-- total_students
-- ---------------
-- 4
