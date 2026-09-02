-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 11-13: CRUD Operations (Create, Read, Update, Delete)
-- These demonstrate parameterized query patterns

-- CREATE (INSERT)
-- Pattern: INSERT INTO students_intermediate (name, marks, course) VALUES (?, ?, ?);
-- Example with actual values:
INSERT INTO students_intermediate (name, marks, course) VALUES ('New Student', 85, 'Python');

-- READ (SELECT)
-- Pattern: SELECT * FROM students_intermediate WHERE id = ?;
SELECT * FROM students_intermediate WHERE id = 1;

-- UPDATE
-- Pattern: UPDATE students_intermediate SET marks = ? WHERE id = ?;
UPDATE students_intermediate SET marks = 90 WHERE id = 1;

-- DELETE
-- Pattern: DELETE FROM students_intermediate WHERE id = ?;
DELETE FROM students_intermediate WHERE id = 1;
