-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 10: Search Students Whose Marks are Between 60 and 90
-- Expected Output: 7 students with marks between 60-90

-- SQL Query:
SELECT name, marks, course FROM students_intermediate 
WHERE marks BETWEEN 60 AND 90 
ORDER BY marks DESC;

-- Expected Output:
-- name             | marks | course
-- ------------------|-------|--------
-- Charlie Davis     | 88    | Python
-- Grace Lee         | 85    | C++
-- Bob Smith         | 78    | Java
-- Frank Miller      | 72    | Java
-- Iris Martin       | 68    | Java
-- Diana Wilson      | 65    | C++
