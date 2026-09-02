-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 8: Find the Average Marks for Each Course

SELECT course, AVG(marks) as average_marks 
FROM students_intermediate 
GROUP BY course;
