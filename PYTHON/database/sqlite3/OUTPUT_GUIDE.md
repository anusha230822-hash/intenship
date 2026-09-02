# SQLite3 Practice with Expected Output - Complete Guide

This folder contains **SQL files WITH expected output** for all practice questions across four levels.

## 📁 File Naming Convention

Files are organized as:
```
OUTPUT_[LEVEL]_[NUMBER]_[DESCRIPTION].sql
```

- **Level**: A (Basic), B (Intermediate), C (Advanced), FINAL (Challenge)
- **Number**: Question/Topic sequence
- **Description**: What the query does

## 📊 File Structure

Each output file contains:
1. **SQL Comment** - Describes what the query does
2. **SQL Query** - The actual code to run
3. **Expected Output** - What results you should see

### Example Format:
```sql
-- SQLite3 Practice - Part A: Basic SQL
-- Question 4: Display All Students
-- Expected Output: All 5 student records

-- SQL Query:
SELECT * FROM students;

-- Expected Output:
-- id | name             | marks | course
-- ---|------------------|-------|--------
-- 1  | Alice Johnson    | 85.5  | Python
-- ...
```

---

## 🗂️ Part A: Basic SQL (9 Files)

### OUTPUT_A_01_create_table.sql
- **Topic**: Create Table
- **Expected**: Table created (no output message)
- **Key**: DDL operation

### OUTPUT_A_02_insert_5_students.sql
- **Topic**: Insert Records
- **Expected**: 5 rows inserted
- **Verification**: COUNT(*) returns 5

### OUTPUT_A_03_select_all_students.sql
- **Topic**: Select All Records
- **Expected**: 5 student records displayed
- **Columns**: id, name, marks, course

### OUTPUT_A_04_select_names_only.sql
- **Topic**: Column Projection
- **Expected**: 5 names listed
- **SQL**: SELECT name

### OUTPUT_A_05_select_high_scorers.sql
- **Topic**: WHERE Clause with Comparison
- **Expected**: 3 students (marks > 75)
- **Result**: Alice, Charlie, Eve

### OUTPUT_A_06_select_python_course.sql
- **Topic**: WHERE Clause with String Match
- **Expected**: 2 Python students
- **Result**: Alice, Charlie

### OUTPUT_A_07_select_by_id.sql
- **Topic**: Search by Primary Key
- **Expected**: 1 student record
- **Result**: Alice Johnson (ID=1)

### OUTPUT_A_08_update_marks.sql
- **Topic**: UPDATE Statement
- **Expected**: 1 row affected, marks changed to 80.5
- **Verification**: Bob Smith's marks updated

### OUTPUT_A_09_delete_student.sql
- **Topic**: DELETE Statement
- **Expected**: 1 row deleted, 4 records remain
- **Verification**: Eve Brown removed, COUNT=4

---

## 🔧 Part B: Intermediate SQL (13 Files)

### OUTPUT_B_03_order_by_marks_desc.sql
- **Topic**: ORDER BY with DESC
- **Expected**: 10 students sorted highest to lowest
- **First 3**: Eve (95), Alice (92), Henry (91)
- **Output**: Sorted list

### OUTPUT_B_04_top_3_students.sql
- **Topic**: LIMIT for Result Limiting
- **Expected**: Top 3 students by marks
- **Result**: Eve, Alice, Henry

### OUTPUT_B_05_count_students.sql
- **Topic**: COUNT() Aggregate Function
- **Expected**: Single value = 10
- **Column Name**: total_students

### OUTPUT_B_06_average_marks.sql
- **Topic**: AVG() Aggregate Function
- **Expected**: Single value ≈ 81.3
- **Column Name**: average_marks

### OUTPUT_B_07_max_min_marks.sql
- **Topic**: MAX() and MIN() Functions
- **Expected**: Two values - highest (95), lowest (65)
- **Columns**: highest_marks, lowest_marks

### OUTPUT_B_08_count_by_course.sql
- **Topic**: GROUP BY Clause
- **Expected**: 3 rows (one per course)
- **Courses**: Python (4), Java (3), C++ (3)

### OUTPUT_B_09_average_by_course.sql
- **Topic**: GROUP BY with AVG()
- **Expected**: Average per course
- **Results**: Python (91.5), Java (72.67), C++ (81.33)

### OUTPUT_B_10_search_names_like_A.sql
- **Topic**: LIKE Pattern Matching
- **Expected**: Students with names starting with 'A'
- **Result**: Alice Johnson only

### OUTPUT_B_11_search_marks_between.sql
- **Topic**: BETWEEN Operator
- **Expected**: 6 students with marks 60-90
- **Range**: From Diana (65) to Charlie (88)

---

## 🚀 Part C: Advanced SQL (7 Files)

### OUTPUT_C_03_join_students_courses.sql
- **Topic**: LEFT JOIN Operations
- **Expected**: Students with their enrolled courses
- **Result**: List of 10 rows with course details
- **Key**: Shows NULL for unenrolled students

### OUTPUT_C_04_unenrolled_students.sql
- **Topic**: Subquery with NOT IN
- **Expected**: Students not enrolled in any course
- **Result**: Frank Miller only

### OUTPUT_C_05_count_students_per_course.sql
- **Topic**: GROUP BY with Relationships
- **Expected**: Count of students per course
- **Results**: Python (3), Java (3), C++ (2), Database (2)

---

## 🎯 Final Challenge: Student Management (7 Files)

### OUTPUT_FINAL_03_view_all_students.sql
- **Option**: Menu Option 2
- **Expected**: All students displayed
- **Columns**: student_id, name, marks, course, enrollment_date
- **Format**: Ordered by name

### OUTPUT_FINAL_07_show_top_students.sql
- **Option**: Menu Option 6
- **Expected**: Top 5 students by marks
- **Format**: Ranked display
- **Sorting**: Highest to lowest marks

### OUTPUT_FINAL_08_course_statistics.sql
- **Option**: Menu Option 7
- **Expected**: Statistics grouped by course
- **Metrics**: Count, Average, Max, Min
- **Format**: Organized by course name

### OUTPUT_FINAL_09_average_marks.sql
- **Option**: Menu Option 8
- **Expected**: Overall and per-course averages
- **Query 1**: Overall average
- **Query 2**: Average by course

### OUTPUT_FINAL_10_student_count.sql
- **Option**: Menu Option 9
- **Expected**: Total and course-wise counts
- **Query 1**: Total count
- **Query 2**: Count by course
- **Query 3**: Percentage breakdown

---

## 💻 How to Use These Files

### Method 1: SQLite3 Command Line
```bash
# Open database
sqlite3 college.db

# Load and execute a file
.read OUTPUT_A_03_select_all_students.sql

# View the output on screen
```

### Method 2: Python Script
```python
import sqlite3

conn = sqlite3.connect('college.db')
with open('OUTPUT_A_03_select_all_students.sql') as f:
    cursor = conn.cursor()
    cursor.execute(f.read())
    results = cursor.fetchall()
    
    # Print results
    for row in results:
        print(row)
```

### Method 3: DB Browser GUI
1. Open DB Browser for SQLite
2. Open your database
3. Go to SQL Editor
4. Copy and paste the SQL query
5. Click Execute
6. Compare with Expected Output

### Method 4: VS Code SQLite Extension
1. Open SQL file in VS Code
2. Click "Run Query" button
3. View results in output panel
4. Compare with expected output

---

## 📋 Step-by-Step Learning Path

### Start with Part A (Basic)
1. Create table: `OUTPUT_A_01_create_table.sql`
2. Insert data: `OUTPUT_A_02_insert_5_students.sql`
3. Basic queries: `OUTPUT_A_03` through `OUTPUT_A_09`
4. Verify each output matches expected

### Progress to Part B (Intermediate)
1. Create fresh database
2. Insert 10 students
3. Run aggregate queries (`B_05-B_07`)
4. Run GROUP BY queries (`B_08-B_09`)
5. Run search queries (`B_10-B_11`)

### Learn Part C (Advanced)
1. Create 3 tables with relationships
2. Insert sample data
3. Execute JOIN queries (`C_03`)
4. Execute subqueries (`C_04`)
5. Execute GROUP BY with JOINs (`C_05`)

### Complete Final Challenge
1. Create management table
2. Run each menu option in sequence
3. Verify output format
4. Test data retrieval

---

## ✅ Verification Checklist

After running each query:
- [ ] Query executes without errors
- [ ] Number of rows matches expected
- [ ] Column names are correct
- [ ] Data values match expected output
- [ ] Sorting/ordering is correct
- [ ] Aggregations show correct calculations

---

## 📊 Output Interpretation

### Table Format:
```
column1 | column2 | column3
--------|---------|--------
value1  | value2  | value3
```

### Aggregation Results:
```
COUNT(*) = 10          -- Number of rows
AVG(marks) = 81.3      -- Average value
MAX(marks) = 95        -- Highest value
MIN(marks) = 65        -- Lowest value
```

### GROUP BY Results:
```
course | count
--------|-------
Python | 4
Java   | 3
C++    | 3
```

### JOINs Results:
Shows combined data from multiple tables with potential NULL values for unmatched rows.

---

## 🔍 Common Output Examples

### Single Value Output:
```sql
SELECT COUNT(*) FROM students;
-- Output: 5
```

### Multiple Rows:
```sql
SELECT name FROM students;
-- Output: (5 rows)
-- Alice, Bob, Charlie, Diana, Eve
```

### Aggregate with GROUP:
```sql
SELECT course, COUNT(*) FROM students GROUP BY course;
-- Output: (3 rows)
-- Python, 2
-- Java, 2
-- C++, 1
```

### JOIN Output:
```sql
SELECT s.name, c.course_name FROM students s JOIN courses c ...
-- Output: (multiple rows with data from both tables)
```

---

## 🎓 Learning Tips

1. **Before Running**: Read the Expected Output section
2. **While Running**: Compare your actual output with expected
3. **After Running**: Understand WHY the output looks this way
4. **Modify and Test**: Change parameters and see how output changes
5. **Document**: Keep notes on what each SQL concept does

---

## 🐛 Troubleshooting

### Output Doesn't Match Expected

**Issue**: Different number of rows
- **Solution**: Check if data was properly inserted before query

**Issue**: Column values are different
- **Solution**: Verify sample data matches what's shown in comments

**Issue**: No output when expected rows
- **Solution**: Check WHERE clause conditions - may be filtering all rows

**Issue**: NULL values appearing
- **Solution**: This is normal for LEFT JOINs - check expected output

---

## 📚 Summary by Complexity

| Level | Files | Concepts | Key Topics |
|-------|-------|----------|-----------|
| **A (Basic)** | 9 | DDL, DML | CREATE, INSERT, SELECT, UPDATE, DELETE |
| **B (Intermediate)** | 13 | Aggregation | COUNT, AVG, MAX, MIN, GROUP BY, ORDER BY |
| **C (Advanced)** | 7 | Relationships | JOINs, Subqueries, Complex Grouping |
| **Final** | 7 | Complete App | Multi-table operations, Statistics |

---

## 🎯 Quick Reference

### To View Specific Output:
- **All students**: `OUTPUT_A_03` or `OUTPUT_FINAL_03`
- **Statistics**: `OUTPUT_FINAL_08`
- **Top students**: `OUTPUT_FINAL_07`
- **Aggregations**: `OUTPUT_B_05` through `OUTPUT_B_07`
- **JOINs**: `OUTPUT_C_03`, `OUTPUT_C_05`

---

**Total Files**: 35+ SQL files with expected outputs  
**Total Queries**: 50+ different SQL patterns  
**Total Learning Hours**: 10-15 hours depending on practice

Happy Learning! 🚀
