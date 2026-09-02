-- SQLite3 Final Challenge - Student Management System
-- Menu Option 3: Search Student

-- Search by ID (using parameterized query pattern)
-- Pattern: SELECT * FROM students_management WHERE student_id = ?;
SELECT * FROM students_management WHERE student_id = 1;

-- Search by Name (partial match)
-- Pattern: SELECT * FROM students_management WHERE name LIKE ?;
SELECT * FROM students_management WHERE name LIKE '%John%';

-- Search by Course
-- Pattern: SELECT * FROM students_management WHERE course = ?;
SELECT * FROM students_management WHERE course = 'Python';

-- Combined search examples
SELECT * FROM students_management 
WHERE (student_id = 1 OR name LIKE '%John%' OR course = 'Python')
ORDER BY name;
