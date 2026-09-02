-- SQLite3 Final Challenge - Student Management System
-- Menu Option 8: Average Marks
-- Expected Output: Overall and per-course averages

-- SQL Query 1 - Overall Average:
SELECT ROUND(AVG(marks), 2) as overall_average_marks 
FROM students_management;

-- Expected Output 1:
-- overall_average_marks
-- ---------------------
-- 86.00

-- SQL Query 2 - Average by Course:
SELECT 
    course,
    ROUND(AVG(marks), 2) as average_marks
FROM students_management
GROUP BY course
ORDER BY average_marks DESC;

-- Expected Output 2 (Example):
-- course | average_marks
-- --------|---------------
-- Python | 86.75
-- Java   | 92.00
-- C++    | 78.50
