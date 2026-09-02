-- SQLite3 Practice - Part C: Advanced SQL
-- Insert Sample Data for Testing

-- Insert courses
INSERT INTO courses (course_name, credits) VALUES 
('Python', 3),
('Java', 3),
('C++', 4),
('Database Design', 3);

-- Insert students
INSERT INTO students_advanced (name, marks, gpa) VALUES 
('Alice Johnson', 92, 3.8),
('Bob Smith', 78, 3.2),
('Charlie Davis', 88, 3.6),
('Diana Wilson', 65, 2.8),
('Eve Brown', 95, 3.9),
('Frank Miller', 72, 3.0);

-- Insert enrollments
INSERT INTO enrollments (student_id, course_id) VALUES 
(1, 1),  -- Alice - Python
(1, 4),  -- Alice - Database Design
(2, 2),  -- Bob - Java
(3, 1),  -- Charlie - Python
(3, 3),  -- Charlie - C++
(4, 2),  -- Diana - Java
(5, 1),  -- Eve - Python
(5, 3),  -- Eve - C++
(5, 4),  -- Eve - Database Design
-- Frank is not enrolled in any course (for testing unenrolled students)
