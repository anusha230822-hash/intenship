-- SQLite3 Practice - Part C: Advanced SQL
-- Question 3: Display Student Names with Their Course Names Using JOIN

SELECT 
    s.name, 
    c.course_name, 
    c.credits
FROM students_advanced s
LEFT JOIN enrollments e ON s.student_id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id
ORDER BY s.name;
