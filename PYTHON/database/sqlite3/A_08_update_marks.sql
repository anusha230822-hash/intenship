-- SQLite3 Practice - Part A: Basic SQL
-- Question 9: Update the Marks of One Student

UPDATE students 
SET marks = 80.5 
WHERE id = 2;

-- Verify the update
SELECT * FROM students WHERE id = 2;
