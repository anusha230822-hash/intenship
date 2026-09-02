-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 8: Find the Average Marks for Each Course
-- Expected Output: Average marks grouped by course

-- SQL Query:
SELECT course, AVG(marks) as average_marks 
FROM students_intermediate 
GROUP BY course;

-- Expected Output:
-- course | average_marks
-- --------|---------------
-- C++    | 81.33
-- Java   | 72.67
-- Python | 91.5
