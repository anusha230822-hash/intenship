-- SQLite3 Final Challenge - Student Management System
-- Menu Option 2: View All Students
-- Expected Output: All students in tabular format

-- SQL Query:
SELECT 
    student_id,
    name,
    marks,
    course,
    enrollment_date
FROM students_management
ORDER BY name;

-- Expected Output:
-- student_id | name           | marks | course | enrollment_date
-- -----------|----------------|-------|--------|----------------
-- 3          | Jane Smith     | 92.0  | Java   | 2026-09-01
-- 1          | John Doe       | 85.5  | Python | 2026-09-01
-- 2          | Mike Johnson   | 78.5  | C++    | 2026-09-01
-- 4          | Sarah Davis    | 88.0  | Python | 2026-09-01
