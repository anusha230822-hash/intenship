-- SQLite3 Practice - Part A: Basic SQL
-- Questions 2 & 3: Insert 5 Student Records
-- Expected Output: 5 rows inserted successfully

-- SQL Query:
INSERT INTO students (name, marks, course) VALUES 
('Alice Johnson', 85.5, 'Python'),
('Bob Smith', 72.0, 'Java'),
('Charlie Davis', 91.0, 'Python'),
('Diana Wilson', 68.5, 'C++'),
('Eve Brown', 78.5, 'Java');

-- Expected Output:
-- ✓ 5 rows inserted successfully
-- (Verify with: SELECT COUNT(*) FROM students;)
-- Output: 5
