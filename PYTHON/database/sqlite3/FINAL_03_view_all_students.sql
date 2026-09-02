-- SQLite3 Final Challenge - Student Management System
-- Menu Option 2: View All Students

SELECT 
    student_id,
    name,
    marks,
    course,
    enrollment_date
FROM students_management
ORDER BY name;
