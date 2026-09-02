-- SQLite3 Practice - Part C: Advanced SQL
-- Question 10: Use Transactions to Insert/Update Multiple Records Safely

-- TRANSACTION 1: Insert Multiple Students Safely
BEGIN TRANSACTION;

INSERT INTO students_advanced (name, marks, gpa) VALUES ('George King', 88, 3.7);
INSERT INTO students_advanced (name, marks, gpa) VALUES ('Helen White', 91, 3.8);
INSERT INTO students_advanced (name, marks, gpa) VALUES ('Ivy Jackson', 86, 3.5);

COMMIT;

-- TRANSACTION 2: Enroll Students in Courses Safely
BEGIN TRANSACTION;

-- Get the IDs of newly inserted students and enroll them
INSERT INTO enrollments (student_id, course_id) 
SELECT student_id, 1 FROM students_advanced WHERE name = 'George King';

INSERT INTO enrollments (student_id, course_id) 
SELECT student_id, 2 FROM students_advanced WHERE name = 'Helen White';

COMMIT;

-- TRANSACTION 3: Update Multiple Records with Rollback on Error
BEGIN TRANSACTION;

UPDATE students_advanced SET marks = 100 WHERE name = 'George King';
UPDATE students_advanced SET gpa = 4.0 WHERE marks = 100;
-- If all updates succeed, COMMIT:
COMMIT;

-- If there's an error, use ROLLBACK to undo all changes:
-- ROLLBACK;

-- Verify all changes
SELECT * FROM students_advanced ORDER BY name;
SELECT * FROM enrollments ORDER BY student_id;
