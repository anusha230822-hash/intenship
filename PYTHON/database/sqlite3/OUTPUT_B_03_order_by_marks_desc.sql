-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 2: Display Students in Descending Order of Marks
-- Expected Output: 10 students sorted by marks (highest to lowest)

-- SQL Query:
SELECT name, marks, course FROM students_intermediate 
ORDER BY marks DESC;

-- Expected Output:
-- name             | marks | course
-- ------------------|-------|--------
-- Eve Brown         | 95    | Python
-- Alice Johnson     | 92    | Python
-- Henry Taylor      | 91    | Python
-- Charlie Davis     | 88    | Python
-- Jack Anderson     | 87    | C++
-- Grace Lee         | 85    | C++
-- Bob Smith         | 78    | Java
-- Frank Miller      | 72    | Java
-- Iris Martin       | 68    | Java
-- Diana Wilson      | 65    | C++
