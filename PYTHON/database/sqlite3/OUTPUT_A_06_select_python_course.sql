-- SQLite3 Practice - Part A: Basic SQL
-- Question 7: Find Students Belonging to the Python Course
-- Expected Output: 2 Python course students

-- SQL Query:
SELECT * FROM students WHERE course = 'Python';

-- Expected Output:
-- id | name             | marks | course
-- ---|------------------|-------|--------
-- 1  | Alice Johnson    | 85.5  | Python
-- 3  | Charlie Davis    | 91.0  | Python
