-- SQLite3 Practice - Part C: Advanced SQL
-- Question 3: Display Student Names with Their Course Names Using JOIN
-- Expected Output: Students and their enrolled courses

-- SQL Query:
SELECT 
    s.name, 
    c.course_name, 
    c.credits
FROM students_advanced s
LEFT JOIN enrollments e ON s.student_id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id
ORDER BY s.name;

-- Expected Output:
-- name             | course_name      | credits
-- ------------------|------------------|--------
-- Alice Johnson     | Python           | 3
-- Alice Johnson     | Database Design  | 3
-- Bob Smith         | Java             | 3
-- Charlie Davis     | Python           | 3
-- Charlie Davis     | C++              | 4
-- Diana Wilson      | Java             | 3
-- Eve Brown         | Python           | 3
-- Eve Brown         | C++              | 4
-- Eve Brown         | Database Design  | 3
-- Frank Miller      | (NULL)           | (NULL)
