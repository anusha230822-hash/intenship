-- SQLite3 Practice - Part C: Advanced SQL
-- Question 6: Database CRUD Methods

-- CREATE: Add a new student
INSERT INTO students_advanced (name, marks, gpa) VALUES ('New Student', 85, 3.5);

-- READ: Get student by ID
SELECT * FROM students_advanced WHERE student_id = 1;

-- READ: Get all students
SELECT * FROM students_advanced;

-- READ: Get student with courses
SELECT s.name, c.course_name 
FROM students_advanced s
LEFT JOIN enrollments e ON s.student_id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id
WHERE s.student_id = 1;

-- UPDATE: Update student marks
UPDATE students_advanced SET marks = 90 WHERE student_id = 1;

-- UPDATE: Update student GPA
UPDATE students_advanced SET gpa = 3.7 WHERE student_id = 1;

-- DELETE: Delete student enrollments first
DELETE FROM enrollments WHERE student_id = 1;

-- DELETE: Delete student
DELETE FROM students_advanced WHERE student_id = 1;
