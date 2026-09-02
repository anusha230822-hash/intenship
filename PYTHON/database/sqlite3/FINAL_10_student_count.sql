-- SQLite3 Final Challenge - Student Management System
-- Menu Option 9: Student Count

-- Total number of students
SELECT COUNT(*) as total_students FROM students_management;

-- Count by course
SELECT 
    course,
    COUNT(*) as student_count
FROM students_management
GROUP BY course
ORDER BY course;

-- Detailed count with percentages
SELECT 
    course,
    COUNT(*) as student_count,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM students_management)), 2) as percentage
FROM students_management
GROUP BY course
ORDER BY student_count DESC;

-- Count statistics
SELECT 
    (SELECT COUNT(*) FROM students_management) as total_students,
    (SELECT COUNT(DISTINCT course) FROM students_management) as total_courses;
