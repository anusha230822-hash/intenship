-- SQLite3 Practice - Part C: Advanced SQL
-- Question 5: Find the Number of Students in Each Course
-- Expected Output: Student count per course

-- SQL Query:
SELECT 
    c.course_name, 
    COUNT(e.student_id) as student_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- Expected Output:
-- course_name      | student_count
-- ------------------|---------------
-- Python           | 3
-- Java             | 3
-- C++              | 2
-- Database Design  | 2
