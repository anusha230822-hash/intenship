-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 10: Search Students Whose Marks are Between 60 and 90

SELECT name, marks, course FROM students_intermediate 
WHERE marks BETWEEN 60 AND 90 
ORDER BY marks DESC;
