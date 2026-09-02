-- SQLite3 Final Challenge - Student Management System
-- Menu Option 9: Student Count
-- Expected Output: Total and per-course counts

-- SQL Query 1 - Total Students:
SELECT COUNT(*) as total_students FROM students_management;

-- Expected Output 1:
-- total_students
-- ---------------
-- 4

-- SQL Query 2 - Count by Course:
SELECT 
    course,
    COUNT(*) as student_count
FROM students_management
GROUP BY course
ORDER BY course;

-- Expected Output 2 (Example):
-- course | student_count
-- --------|---------------
-- C++    | 1
-- Java   | 1
-- Python | 2

-- SQL Query 3 - Count with Percentages:
SELECT 
    course,
    COUNT(*) as student_count,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM students_management)), 2) as percentage
FROM students_management
GROUP BY course
ORDER BY student_count DESC;

-- Expected Output 3 (Example):
-- course | student_count | percentage
-- --------|---------------|----------
-- Python | 2             | 50.00
-- C++    | 1             | 25.00
-- Java   | 1             | 25.00
