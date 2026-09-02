-- SQLite3 Practice - Part C: Advanced SQL
-- Question 4: Find Students Who Are Not Enrolled in Any Course

SELECT 
    s.student_id, 
    s.name, 
    s.marks
FROM students_advanced s
WHERE s.student_id NOT IN (SELECT student_id FROM enrollments);
