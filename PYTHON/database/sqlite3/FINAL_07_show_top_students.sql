-- SQLite3 Final Challenge - Student Management System
-- Menu Option 6: Show Top Students

-- Top 5 students by marks
SELECT 
    student_id,
    name,
    marks,
    course
FROM students_management
ORDER BY marks DESC
LIMIT 5;

-- Top 3 students by marks
SELECT 
    student_id,
    name,
    marks,
    course
FROM students_management
ORDER BY marks DESC
LIMIT 3;

-- Top students with rank
-- SQLite: Use ROW_NUMBER window function (SQLite 3.25+)
SELECT 
    ROW_NUMBER() OVER (ORDER BY marks DESC) as rank,
    name,
    marks,
    course
FROM students_management
LIMIT 5;
