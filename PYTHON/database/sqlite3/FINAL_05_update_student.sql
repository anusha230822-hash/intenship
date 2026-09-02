-- SQLite3 Final Challenge - Student Management System
-- Menu Option 4: Update Student

-- Update student name (using parameterized query pattern)
-- Pattern: UPDATE students_management SET name = ? WHERE student_id = ?;
UPDATE students_management SET name = 'John Updated' WHERE student_id = 1;

-- Update student marks
-- Pattern: UPDATE students_management SET marks = ? WHERE student_id = ?;
UPDATE students_management SET marks = 95.5 WHERE student_id = 1;

-- Update student course
-- Pattern: UPDATE students_management SET course = ? WHERE student_id = ?;
UPDATE students_management SET course = 'Java' WHERE student_id = 1;

-- Update multiple fields for one student
UPDATE students_management 
SET name = 'John Updated', marks = 90.0, course = 'Python' 
WHERE student_id = 1;

-- Verify the update
SELECT * FROM students_management WHERE student_id = 1;
