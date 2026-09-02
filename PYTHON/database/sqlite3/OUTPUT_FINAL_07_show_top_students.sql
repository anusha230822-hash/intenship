-- SQLite3 Final Challenge - Student Management System
-- Menu Option 6: Show Top Students
-- Expected Output: Top 5 students by marks

-- SQL Query:
SELECT 
    student_id,
    name,
    marks,
    course
FROM students_management
ORDER BY marks DESC
LIMIT 5;

-- Expected Output (Example with 4 students):
-- student_id | name           | marks | course
-- -----------|----------------|-------|--------
-- 3          | Jane Smith     | 92.0  | Java
-- 4          | Sarah Davis    | 88.0  | Python
-- 1          | John Doe       | 85.5  | Python
-- 2          | Mike Johnson   | 78.5  | C++
