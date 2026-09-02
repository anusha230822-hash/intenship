-- SQLite3 Practice - Part B: Intermediate SQL
-- Question 14: Transactions - INSERT Multiple Records Safely (Commit and Rollback)

-- TRANSACTION EXAMPLE 1: Successful Transaction (COMMIT)
BEGIN TRANSACTION;

INSERT INTO students_intermediate (name, marks, course) VALUES ('Student 1', 88, 'Python');
INSERT INTO students_intermediate (name, marks, course) VALUES ('Student 2', 92, 'Java');
INSERT INTO students_intermediate (name, marks, course) VALUES ('Student 3', 85, 'C++');

COMMIT;

-- TRANSACTION EXAMPLE 2: Failed Transaction (ROLLBACK)
BEGIN TRANSACTION;

INSERT INTO students_intermediate (name, marks, course) VALUES ('Student 4', 95, 'Python');
UPDATE students_intermediate SET marks = 150 WHERE id = 1;  -- Invalid: marks > 100

-- If error occurs, use ROLLBACK:
ROLLBACK;

-- Verify data after transactions
SELECT * FROM students_intermediate;
