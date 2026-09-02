-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 3: Display the Top 3 Students
-- Expected Output: Top 3 students by marks

-- SQL Query:
SELECT name, marks FROM students_intermediate 
ORDER BY marks DESC 
LIMIT 3;

-- Expected Output:
-- name             | marks
-- ------------------|-------
-- Eve Brown         | 95
-- Alice Johnson     | 92
-- Henry Taylor      | 91
