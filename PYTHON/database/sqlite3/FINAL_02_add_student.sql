-- SQLite3 Final Challenge - Student Management System
-- Menu Option 1: Add Student

-- Insert a new student (using parameterized query pattern)
-- Pattern: INSERT INTO students_management (name, marks, course) VALUES (?, ?, ?);

-- Example 1: Add a student with valid marks
INSERT INTO students_management (name, marks, course) VALUES ('John Doe', 85.5, 'Python');

-- Example 2: Add multiple students
INSERT INTO students_management (name, marks, course) VALUES 
('Jane Smith', 92.0, 'Java'),
('Mike Johnson', 78.5, 'C++'),
('Sarah Davis', 88.0, 'Python');

-- Verify insertion
SELECT * FROM students_management;
