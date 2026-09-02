-- SQLite3 Practice - Part C: Advanced SQL
-- Question 9: Create Indexes for Frequently Searched Columns

-- Create index on student name (for quick name searches)
CREATE INDEX IF NOT EXISTS idx_student_name ON students_advanced(name);

-- Create index on student marks (for quick mark-based searches)
CREATE INDEX IF NOT EXISTS idx_student_marks ON students_advanced(marks);

-- Create index on student ID in enrollments (for quick joins)
CREATE INDEX IF NOT EXISTS idx_enrollment_student ON enrollments(student_id);

-- Create index on course ID in enrollments (for quick course lookups)
CREATE INDEX IF NOT EXISTS idx_enrollment_course ON enrollments(course_id);

-- Create composite index (for queries filtering by both marks and GPA)
CREATE INDEX IF NOT EXISTS idx_student_marks_gpa ON students_advanced(marks, gpa);

-- Verify indexes were created
-- Note: To check indexes, use SQLite pragma:
PRAGMA index_list(students_advanced);
PRAGMA index_info(idx_student_name);
