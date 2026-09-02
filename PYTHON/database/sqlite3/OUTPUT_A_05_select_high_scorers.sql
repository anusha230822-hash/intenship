-- SQLite3 Practice - Part A: Basic SQL
-- Question 6: Display Students Who Scored More Than 75 Marks
-- Expected Output: 3 students with marks > 75

-- SQL Query:
SELECT * FROM students WHERE marks > 75;

-- Expected Output:
-- id | name             | marks | course
-- ---|------------------|-------|--------
-- 1  | Alice Johnson    | 85.5  | Python
-- 3  | Charlie Davis    | 91.0  | Python
-- 5  | Eve Brown        | 78.5  | Java
