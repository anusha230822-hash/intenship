-- SQLite3 Practice - Part C: Advanced SQL
-- Question 8: Pagination Using LIMIT and OFFSET

-- Page 1: First 2 records
SELECT student_id, name, marks, gpa FROM students_advanced
ORDER BY name
LIMIT 2 OFFSET 0;

-- Page 2: Next 2 records
SELECT student_id, name, marks, gpa FROM students_advanced
ORDER BY name
LIMIT 2 OFFSET 2;

-- Page 3: Next 2 records
SELECT student_id, name, marks, gpa FROM students_advanced
ORDER BY name
LIMIT 2 OFFSET 4;

-- General formula: OFFSET = (page_number - 1) * page_size
-- Example: Get page 2 with page size 3
-- OFFSET = (2 - 1) * 3 = 3
SELECT student_id, name, marks, gpa FROM students_advanced
ORDER BY name
LIMIT 3 OFFSET 3;
