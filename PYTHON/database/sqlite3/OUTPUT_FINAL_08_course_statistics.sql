-- SQLite3 Final Challenge - Student Management System
-- Menu Option 7: Course-wise Statistics
-- Expected Output: Statistics grouped by course

-- SQL Query:
SELECT 
    course,
    COUNT(*) as student_count,
    ROUND(AVG(marks), 2) as average_marks,
    MAX(marks) as highest_marks,
    MIN(marks) as lowest_marks
FROM students_management
GROUP BY course
ORDER BY course;

-- Expected Output (Example):
-- course | student_count | average_marks | highest_marks | lowest_marks
-- --------|---------------|--------------|--------------|--------------
-- C++    | 1             | 78.50        | 78.5         | 78.5
-- Java   | 1             | 92.00        | 92.0         | 92.0
-- Python | 2             | 86.75        | 88.0         | 85.5
