-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 7: Count Students Course-wise Using GROUP BY

SELECT course, COUNT(*) as student_count 
FROM students_intermediate 
GROUP BY course;
