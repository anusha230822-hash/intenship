-- SQLite3 Practice Assignment - All SQL Files Index
-- Organized by difficulty level: Part A (Basic), Part B (Intermediate), Part C (Advanced), Final Challenge

================================================================================
PART A: BASIC SQL (10 Questions)
================================================================================

A_01_create_table.sql
   - Question 1: Create Students Table
   - Create table with id, name, marks, course columns

A_02_insert_5_students.sql
   - Questions 2-3: Insert 5 Student Records
   - Insert sample data with different courses and marks

A_03_select_all_students.sql
   - Question 4: Display All Students
   - SELECT * query to view complete records

A_04_select_names_only.sql
   - Question 5: Display Only Student Names
   - SELECT name column projection

A_05_select_high_scorers.sql
   - Question 6: Display Students with Marks > 75
   - WHERE clause with comparison operator

A_06_select_python_course.sql
   - Question 7: Find Students in Python Course
   - WHERE clause with string matching

A_07_select_by_id.sql
   - Question 8: Find Student by ID
   - WHERE clause with specific ID search

A_08_update_marks.sql
   - Question 9: Update Student Marks
   - UPDATE query with WHERE clause

A_09_delete_student.sql
   - Question 10: Delete a Student
   - DELETE query with verification

================================================================================
PART B: INTERMEDIATE SQL (14 Questions)
================================================================================

B_01_create_table.sql
   - Question 1: Create Students Table (Intermediate Level)
   - Fresh table for intermediate exercises

B_02_insert_10_students.sql
   - Question 1: Insert 10 Students
   - Multi-row INSERT using VALUES list

B_03_order_by_marks_desc.sql
   - Question 2: Display Students by Marks (Descending)
   - ORDER BY with DESC clause

B_04_top_3_students.sql
   - Question 3: Display Top 3 Students
   - LIMIT clause for result limiting

B_05_count_students.sql
   - Question 4: Count Total Students
   - COUNT() aggregate function

B_06_average_marks.sql
   - Question 5: Calculate Average Marks
   - AVG() aggregate function

B_07_max_min_marks.sql
   - Question 6: Find Highest and Lowest Marks
   - MAX() and MIN() aggregate functions

B_08_count_by_course.sql
   - Question 7: Count Students by Course
   - GROUP BY clause for grouping

B_09_average_by_course.sql
   - Question 8: Average Marks per Course
   - GROUP BY with AVG() function

B_10_search_names_like_A.sql
   - Question 9: Search Names Starting with "A"
   - LIKE operator for pattern matching

B_11_search_marks_between.sql
   - Question 10: Search Marks Between 60-90
   - BETWEEN operator for range queries

B_12_crud_operations.sql
   - Questions 11-13: CRUD Operations
   - CREATE (INSERT), READ (SELECT), UPDATE, DELETE examples
   - Parameterized query patterns shown

B_13_transactions.sql
   - Question 14: Transactions with Commit/Rollback
   - BEGIN TRANSACTION, COMMIT, ROLLBACK examples

================================================================================
PART C: ADVANCED SQL (10 Questions)
================================================================================

C_01_create_tables_with_relationships.sql
   - Question 1: Create Three Tables with Relationships
   - students_advanced, courses, enrollments tables
   - PRIMARY KEY and FOREIGN KEY constraints

C_02_insert_sample_data.sql
   - Insert sample data for all three tables
   - Demonstrates relationships between tables

C_03_join_students_courses.sql
   - Question 3: Display Students with Courses Using JOIN
   - LEFT JOIN operation for relationships

C_04_unenrolled_students.sql
   - Question 4: Find Unenrolled Students
   - Subquery with NOT IN clause

C_05_count_students_per_course.sql
   - Question 5: Count Students per Course
   - GROUP BY with LEFT JOIN

C_06_crud_methods.sql
   - Question 6: Database CRUD Methods
   - Comprehensive CREATE, READ, UPDATE, DELETE examples
   - Class-like structure documentation

C_07_multi_filter_search.sql
   - Question 7: Multi-Filter Student Search
   - Multiple WHERE conditions and AND/OR operators

C_08_pagination.sql
   - Question 8: Pagination with LIMIT and OFFSET
   - Demonstrates page-based result retrieval
   - Includes formula for calculating OFFSET

C_09_create_indexes.sql
   - Question 9: Create Indexes
   - INDEX creation on frequently searched columns
   - Single and composite indexes
   - PRAGMA commands to view indexes

C_10_transactions_advanced.sql
   - Question 10: Advanced Transactions
   - Multi-record INSERT/UPDATE within transactions
   - COMMIT and ROLLBACK demonstrations

================================================================================
FINAL CHALLENGE: STUDENT MANAGEMENT SYSTEM (10 Menu Options)
================================================================================

FINAL_01_create_table.sql
   - Create main students_management table
   - CHECK constraint for marks validation (0-100)

FINAL_02_add_student.sql
   - Menu Option 1: Add Student
   - INSERT queries with validation examples

FINAL_03_view_all_students.sql
   - Menu Option 2: View All Students
   - SELECT all students ordered by name

FINAL_04_search_student.sql
   - Menu Option 3: Search Student
   - Search by ID, name (partial), or course

FINAL_05_update_student.sql
   - Menu Option 4: Update Student
   - UPDATE queries for name, marks, course

FINAL_06_delete_student.sql
   - Menu Option 5: Delete Student
   - DELETE query with verification

FINAL_07_show_top_students.sql
   - Menu Option 6: Show Top Students
   - ORDER BY DESC LIMIT for ranking
   - ROW_NUMBER window function example

FINAL_08_course_statistics.sql
   - Menu Option 7: Course-wise Statistics
   - GROUP BY with COUNT, AVG, MAX, MIN

FINAL_09_average_marks.sql
   - Menu Option 8: Average Marks
   - Overall and per-course averages

FINAL_10_student_count.sql
   - Menu Option 9: Student Count
   - Total and per-course counts with percentages

================================================================================
HOW TO USE THESE SQL FILES
================================================================================

Option 1: Use SQLite3 Command Line
```
sqlite3 college.db
.read A_01_create_table.sql
.read A_02_insert_5_students.sql
.read A_03_select_all_students.sql
```

Option 2: Use Python Script with sqlite3
```python
import sqlite3
conn = sqlite3.connect('college.db')
with open('A_01_create_table.sql') as f:
    conn.executescript(f.read())
conn.commit()
```

Option 3: Use GUI Tools
- DB Browser for SQLite
- VS Code SQLite Extension
- MySQL Workbench (with SQLite plugin)

================================================================================
SUMMARY OF SQL CONCEPTS
================================================================================

BASIC (Part A):
  - CREATE TABLE
  - INSERT
  - SELECT (with WHERE)
  - UPDATE
  - DELETE

INTERMEDIATE (Part B):
  - GROUP BY
  - ORDER BY
  - LIMIT
  - LIKE (pattern matching)
  - BETWEEN
  - Aggregate functions (COUNT, AVG, MAX, MIN)
  - CRUD operations
  - Transactions

ADVANCED (Part C):
  - Relationships (PRIMARY KEY, FOREIGN KEY)
  - JOINs (LEFT JOIN)
  - Subqueries
  - Pagination (OFFSET)
  - Indexes
  - Complex transactions

FINAL CHALLENGE:
  - Complete application SQL
  - Data validation
  - Parameterized queries
  - Multiple table operations

================================================================================
TESTING SEQUENCE
================================================================================

For best learning experience, follow this order:

1. Start with Part A (Basic):
   Run each file in sequence: A_01 → A_02 → A_03 → ... → A_09

2. Progress to Part B (Intermediate):
   Create fresh database and run: B_01 → B_02 → B_03 → ... → B_13

3. Learn Part C (Advanced):
   Create new database and run: C_01 → C_02 → C_03 → ... → C_10

4. Complete Final Challenge:
   Create final database and run: FINAL_01 → FINAL_02 → ... → FINAL_10

================================================================================
NOTES
================================================================================

- All file patterns follow: [LEVEL]_[NUMBER]_[DESCRIPTION].sql
- Numbers help identify question/topic order
- Each file is independent and can be run separately
- Some files may reference data inserted by previous files
- Comments in each file explain the SQL concept
- Parameterized query patterns are shown (using ? placeholders)

Happy Learning! 🎓
