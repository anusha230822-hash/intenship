-- SQLite3 Final Challenge - Student Management System
-- Menu Option 7: Course-wise Statistics

SELECT 
    course,
    COUNT(*) as student_count,
    AVG(marks) as average_marks,
    MAX(marks) as highest_marks,
    MIN(marks) as lowest_marks
FROM students_management
GROUP BY course
ORDER BY course;

-- Alternative: With ROUND for cleaner averages
SELECT 
    course,
    COUNT(*) as student_count,
    ROUND(AVG(marks), 2) as average_marks,
    MAX(marks) as highest_marks,
    MIN(marks) as lowest_marks
FROM students_management
GROUP BY course
ORDER BY course;
