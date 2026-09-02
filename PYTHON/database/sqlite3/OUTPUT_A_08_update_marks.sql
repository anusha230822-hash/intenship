-- SQLite3 Practice - Part A: Basic SQL
-- Question 9: Update the Marks of One Student
-- Expected Output: 1 row updated, then verify the update

-- SQL Query (Update):
UPDATE students 
SET marks = 80.5 
WHERE id = 2;

-- Expected Output after UPDATE:
-- (No output means success)
-- ✓ 1 row(s) affected

-- Verification Query:
SELECT * FROM students WHERE id = 2;

-- Expected Output (Verification):
-- id | name      | marks | course
-- ---|-----------|-------|-------
-- 2  | Bob Smith | 80.5  | Java
-- (Note: marks changed from 72.0 to 80.5)
