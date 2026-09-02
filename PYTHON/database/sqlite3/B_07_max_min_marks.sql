-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 6: Find the Highest and Lowest Marks

SELECT 
    MAX(marks) as highest_marks,
    MIN(marks) as lowest_marks 
FROM students_intermediate;
