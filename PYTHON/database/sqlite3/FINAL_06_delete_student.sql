-- SQLite3 Final Challenge - Student Management System
-- Menu Option 5: Delete Student

-- Delete a single student by ID (using parameterized query pattern)
-- Pattern: DELETE FROM students_management WHERE student_id = ?;
DELETE FROM students_management WHERE student_id = 1;

-- Verify the deletion
SELECT COUNT(*) as total_students FROM students_management;

-- View remaining students
SELECT * FROM students_management;
