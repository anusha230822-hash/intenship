-- SQLite3 Practice - Part C: Advanced SQL
-- Question 7: Student Search Feature with Multiple Filters

-- Filter by minimum marks (>= 80)
SELECT * FROM students_advanced WHERE marks >= 80;

-- Filter by minimum GPA (>= 3.5)
SELECT * FROM students_advanced WHERE gpa >= 3.5;

-- Filter by both marks and GPA
SELECT * FROM students_advanced WHERE marks >= 80 AND gpa >= 3.5;

-- Filter by name pattern
SELECT * FROM students_advanced WHERE name LIKE 'A%';

-- Complex filter: Marks between 70-90 AND GPA >= 3.0
SELECT * FROM students_advanced 
WHERE marks BETWEEN 70 AND 90 AND gpa >= 3.0
ORDER BY marks DESC;
