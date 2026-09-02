-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 3: Display the Top 3 Students

SELECT name, marks FROM students_intermediate 
ORDER BY marks DESC 
LIMIT 3;
