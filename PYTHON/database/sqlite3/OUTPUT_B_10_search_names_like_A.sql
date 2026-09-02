-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 9: Search Students Whose Names Start with "A"
-- Expected Output: Students with names starting with 'A'

-- SQL Query:
SELECT name, marks FROM students_intermediate 
WHERE name LIKE 'A%' 
ORDER BY name;

-- Expected Output:
-- name             | marks
-- ------------------|-------
-- Alice Johnson     | 92
