-- SQLite3 Final Challenge - Student Management System
-- Menu Option 8: Average Marks

-- Overall average marks
SELECT ROUND(AVG(marks), 2) as overall_average_marks 
FROM students_management;

-- Average marks by course
SELECT 
    course,
    ROUND(AVG(marks), 2) as average_marks
FROM students_management
GROUP BY course
ORDER BY average_marks DESC;

-- Detailed average statistics
SELECT 
    COUNT(*) as total_students,
    ROUND(AVG(marks), 2) as average_marks,
    ROUND(MIN(marks), 2) as min_marks,
    ROUND(MAX(marks), 2) as max_marks
FROM students_management;
