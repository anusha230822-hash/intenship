-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 7: Count Students Course-wise Using GROUP BY
-- Expected Output: Count grouped by course

-- SQL Query:
SELECT course, COUNT(*) as student_count 
FROM students_intermediate 
GROUP BY course;

-- Expected Output:
-- course | student_count
-- --------|---------------
-- C++    | 3
-- Java   | 3
-- Python | 4
