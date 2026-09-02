-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 9: Search Students Whose Names Start with "A"

SELECT name, marks FROM students_intermediate 
WHERE name LIKE 'A%' 
ORDER BY name;
