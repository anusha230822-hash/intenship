-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 6: Find the Highest and Lowest Marks
-- Expected Output: Max and Min values

-- SQL Query:
SELECT 
    MAX(marks) as highest_marks,
    MIN(marks) as lowest_marks 
FROM students_intermediate;

-- Expected Output:
-- highest_marks | lowest_marks
-- --------------|---------------
-- 95            | 65
