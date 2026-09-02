# SQLite3 Practice Assignment - Complete Solutions

This folder contains comprehensive solutions for all levels of SQLite3 practice exercises.

## 📁 File Structure

```
sqlite3/
├── part_a_basic_student.py          # Part A: Basic SQL Operations
├── part_b_intermediate.py            # Part B: Intermediate SQL Operations
├── part_c_advanced.py                # Part C: Advanced SQL with Relationships
├── final_challenge_student_system.py # Final Challenge: Complete Management System
└── README.md                         # This file
```

---

## 📋 Part A: Basic SQL Operations (`part_a_basic_student.py`)

**Difficulty Level:** Beginner

### Topics Covered:
1. ✅ Create SQLite database (`college.db`)
2. ✅ Create students table with columns (id, name, marks, course)
3. ✅ Insert 5 student records
4. ✅ Display all students
5. ✅ Display only student names
6. ✅ Display students with marks > 75
7. ✅ Filter students by course (Python)
8. ✅ Find student by ID
9. ✅ Update student marks
10. ✅ Delete a student

### Key Concepts:
- SQLite3 connection and disconnection
- CREATE TABLE operations
- INSERT queries
- SELECT queries with WHERE clause
- UPDATE operations
- DELETE operations
- Parameterized queries

### How to Run:
```bash
python part_a_basic_student.py
```

### Expected Output:
```
==================================================
SQLite3 - Part A (Basic) Practice
==================================================
✓ Database connection established
✓ Table 'students' created successfully
✓ 5 student records inserted successfully

--- All Students ---
ID: 1, Name: Alice Johnson, Marks: 85.5, Course: Python
...
```

---

## 🔧 Part B: Intermediate SQL Operations (`part_b_intermediate.py`)

**Difficulty Level:** Intermediate

### Topics Covered:
1. ✅ Insert 10 students using `executemany()`
2. ✅ Display students in descending order (ORDER BY)
3. ✅ Display top 3 students (LIMIT)
4. ✅ Count total students (COUNT())
5. ✅ Calculate average marks (AVG())
6. ✅ Find highest and lowest marks (MAX/MIN)
7. ✅ Count students course-wise (GROUP BY)
8. ✅ Average marks per course
9. ✅ Search names starting with a letter (LIKE)
10. ✅ Search marks within range (BETWEEN)
11. ✅ Menu-driven CRUD application
12. ✅ Exception handling with try-except
13. ✅ Parameterized queries
14. ✅ Transaction management (commit/rollback)

### Key Concepts:
- Class-based database management
- Aggregate functions (COUNT, AVG, MAX, MIN)
- GROUP BY clause
- ORDER BY clause
- LIMIT clause
- LIKE operator for pattern matching
- BETWEEN operator
- Transaction handling

### How to Run:
```bash
python part_b_intermediate.py
```

### Expected Output:
```
============================================================
SQLite3 - Part B (Intermediate) Practice
============================================================
✓ Task 1: 10 students inserted using executemany()

--- Task 2: Students by Marks (Descending) ---
  Eve Brown: 95 marks (Python)
  ...
```

---

## 🚀 Part C: Advanced SQL Operations (`part_c_advanced.py`)

**Difficulty Level:** Advanced

### Topics Covered:
1. ✅ Create three tables (students, courses, enrollments)
2. ✅ Establish relationships with PRIMARY KEY and FOREIGN KEY
3. ✅ Display student-course relationships using JOIN
4. ✅ Find students not enrolled in any course
5. ✅ Count students per course
6. ✅ Database class with CRUD methods
7. ✅ Multi-filter student search
8. ✅ Pagination using LIMIT and OFFSET
9. ✅ Create indexes on frequently searched columns
10. ✅ Transactions for safe multi-record operations

### Database Schema:
```
courses
├── course_id (PRIMARY KEY)
├── course_name
└── credits

students
├── student_id (PRIMARY KEY)
├── name
├── marks
└── gpa

enrollments (Junction Table)
├── enrollment_id (PRIMARY KEY)
├── student_id (FOREIGN KEY)
├── course_id (FOREIGN KEY)
└── enrollment_date
```

### Key Concepts:
- Relational database design
- PRIMARY KEY and FOREIGN KEY constraints
- JOIN operations (LEFT JOIN)
- Subqueries
- Index creation
- Pagination implementation
- CRUD pattern implementation
- Advanced transaction handling

### CRUD Methods Implemented:
- `add_student()` - Create new student
- `read_student()` - Retrieve student by ID
- `update_student()` - Modify student details
- `delete_student()` - Remove student record

### How to Run:
```bash
python part_c_advanced.py
```

### Expected Output:
```
======================================================================
SQLite3 - Part C (Advanced) Practice - Relationships & CRUD
======================================================================
✓ Table created successfully
✓ Sample data inserted into all tables
✓ Indexes created on frequently searched columns

--- Task 3: Students with Their Courses (JOIN) ---
  Alice Johnson: Python (3 credits)
  ...
```

---

## 🎯 Final Challenge: Complete Student Management System (`final_challenge_student_system.py`)

**Difficulty Level:** Professional

This is a complete, production-ready Student Management System with a menu-driven interface.

### Features:
1. ✅ **Add Student** - Insert new student with validation
2. ✅ **View All Students** - Display all records in tabular format
3. ✅ **Search Student** - Search by ID, Name, or Course
4. ✅ **Update Student** - Modify any student attribute
5. ✅ **Delete Student** - Remove student with confirmation
6. ✅ **Show Top Students** - Display highest scorers
7. ✅ **Course-wise Statistics** - Stats (count, avg, max, min) by course
8. ✅ **Average Marks** - Overall and course-wise averages
9. ✅ **Student Count** - Total and by course breakdown
10. ✅ **Exit** - Graceful application termination

### Technical Features:
- ✅ Full exception handling with try-except blocks
- ✅ Input validation for marks (0-100 range)
- ✅ Parameterized queries for SQL injection prevention
- ✅ Transaction management (commit/rollback)
- ✅ User-friendly error messages
- ✅ Formatted tabular output
- ✅ Confirmation dialogs for destructive operations
- ✅ Persistent SQLite3 database

### Key Implementation Details:
```python
# Parameterized query example (prevents SQL injection)
cursor.execute(
    'INSERT INTO students (name, marks, course) VALUES (?, ?, ?)',
    (name, marks, course)
)

# Transaction with rollback
try:
    cursor.execute(...)
    self.conn.commit()
except Error as e:
    self.conn.rollback()
    print(f"Error: {e}")
```

### How to Run:
```bash
python final_challenge_student_system.py
```

### Interactive Menu:
```
==================================================
STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Top Students
7. Course-wise Statistics
8. Average Marks
9. Student Count
10. Exit
==================================================
Enter your choice (1-10): 
```

### Database Structure:
```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL NOT NULL CHECK(marks >= 0 AND marks <= 100),
    course TEXT NOT NULL,
    enrollment_date TEXT DEFAULT CURRENT_DATE
)
```

### Sample Operations:

**Add Student:**
```
Enter student name: John Doe
Enter marks (0-100): 85.5
Enter course name: Python
✓ Student 'John Doe' added successfully! (ID: 1)
```

**View All Students:**
```
ID    Name                 Marks    Course         
----- -------------------- -------- ---------------
1     John Doe             85.5     Python         
2     Jane Smith           92.0     Java           
Total students: 2
```

---

## 🎓 Learning Path

### Recommended Order to Study:

1. **Start with Part A (Basic)**
   - Understand basic CRUD operations
   - Learn SQL fundamentals
   - Get comfortable with SQLite3 connections

2. **Progress to Part B (Intermediate)**
   - Learn aggregate functions
   - Understand sorting and filtering
   - Implement exception handling
   - Learn transactions

3. **Move to Part C (Advanced)**
   - Design relational databases
   - Implement complex JOINs
   - Create CRUD classes
   - Learn pagination and indexing

4. **Complete with Final Challenge**
   - Build a complete application
   - Practice user input validation
   - Implement menu-driven interface
   - Deploy professional-grade code

---

## 💡 Key Concepts Summary

### Basic Concepts (Part A):
- Database connections
- Table creation
- CRUD operations
- Parameterized queries

### Intermediate Concepts (Part B):
- Aggregate functions
- Grouping and sorting
- Pattern matching
- Exception handling
- Transactions

### Advanced Concepts (Part C):
- Relational design
- Foreign keys and constraints
- Complex queries (JOINs, subqueries)
- Indexing
- Class-based database management

### Professional Concepts (Final Challenge):
- User input validation
- Error messages
- Menu-driven interface
- Database persistence
- Confirmation dialogs

---

## 🔒 Security Best Practices Implemented

1. **Parameterized Queries**: All user inputs use `?` placeholders to prevent SQL injection
   ```python
   cursor.execute('SELECT * FROM students WHERE id = ?', (user_id,))
   ```

2. **Input Validation**: All user inputs are validated before processing
   ```python
   if marks < 0 or marks > 100:
       print("Invalid marks!")
   ```

3. **Exception Handling**: All database operations wrapped in try-except blocks
   ```python
   try:
       cursor.execute(...)
   except Error as e:
       self.conn.rollback()
   ```

4. **Confirmation Dialogs**: Destructive operations require user confirmation

---

## 📊 Database Operations Cheat Sheet

### SELECT Operations:
```python
# All records
cursor.execute('SELECT * FROM students')

# With condition
cursor.execute('SELECT * FROM students WHERE marks > ?', (75,))

# Sorting
cursor.execute('SELECT * FROM students ORDER BY marks DESC')

# Limit
cursor.execute('SELECT * FROM students LIMIT 10')

# Aggregate
cursor.execute('SELECT COUNT(*), AVG(marks) FROM students')

# Grouping
cursor.execute('SELECT course, COUNT(*) FROM students GROUP BY course')

# JOIN
cursor.execute('''
    SELECT s.name, c.course_name 
    FROM students s 
    JOIN enrollments e ON s.id = e.student_id
    JOIN courses c ON e.course_id = c.id
''')
```

### INSERT Operations:
```python
# Single record
cursor.execute('INSERT INTO students VALUES (?, ?, ?)', (name, marks, course))

# Multiple records
cursor.executemany(
    'INSERT INTO students VALUES (?, ?, ?)', 
    [(name1, marks1, course1), (name2, marks2, course2)]
)
```

### UPDATE Operations:
```python
cursor.execute('UPDATE students SET marks = ? WHERE id = ?', (new_marks, student_id))
```

### DELETE Operations:
```python
cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
```

### Transactions:
```python
try:
    cursor.execute('INSERT ...')
    cursor.execute('UPDATE ...')
    conn.commit()
except:
    conn.rollback()
```

---

## 🐛 Troubleshooting

### Common Issues:

**Issue:** Database file not found
- **Solution:** Check if the database file is created in the correct directory

**Issue:** "table students already exists"
- **Solution:** Use `CREATE TABLE IF NOT EXISTS` or delete the .db file

**Issue:** "no such column"
- **Solution:** Check table schema and column names match your query

**Issue:** SQL injection warnings
- **Solution:** Always use parameterized queries with `?` placeholders

---

## 📝 Notes for Students

- Always close database connections: `conn.close()`
- Use `commit()` after INSERT, UPDATE, DELETE operations
- Use `rollback()` if an error occurs during transaction
- Test with sample data before deploying
- Keep backups of important databases
- Use meaningful column names and table structures

---

## 🎓 Additional Learning Resources

- SQLite3 Official Documentation: https://www.sqlite.org/
- Python sqlite3 Module: https://docs.python.org/3/library/sqlite3.html
- SQL Tutorial: https://www.w3schools.com/sql/
- Relational Database Concepts: https://en.wikipedia.org/wiki/Relational_database

---

## ✅ Verification Checklist

After running each file, verify:

- [ ] No SQL errors appear
- [ ] Data is correctly inserted
- [ ] Queries return expected results
- [ ] Transactions commit successfully
- [ ] Exception handling works
- [ ] User input is validated
- [ ] Database file is created

---

## 📧 Need Help?

- Check the error messages - they usually indicate what's wrong
- Print intermediate values to debug
- Review the SQL syntax for your operations
- Verify database schema matches your queries
- Check for typos in table and column names

---

**Happy Learning! 🚀**

*Last Updated: 2026*
