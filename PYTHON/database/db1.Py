import sqlite3
a= sqlite3.connect("std.db") 
c= a.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT (
        STUDENT_ID INTEGER PRIMARY KEY,
        STUDENT_NAME TEXT,
        STUDENT_AGE INTEGER
    )
""")
c.execute("""
               INSERT  INTO STUDENT VALUES (71, 'Anusha', 18)
               """)
c.execute("""
               INSERT INTO STUDENT VALUES (338, 'KING', 19)
               """)
c.execute("""
               INSERT  INTO STUDENT VALUES (13, 'YASU', 18)
               """)
c.execute("""
               INSERT  INTO STUDENT VALUES (43, 'TEJU', 20)
               """)
c.execute("""
               INSERT  INTO STUDENT VALUES (14, 'ROHANTH', 21)
               """)
c.execute("""
               INSERT INTO STUDENT VALUES (15, 'ABHIRAM', 22)
               """)
a.commit()


print("Students aged 18:")
c.execute("SELECT * FROM STUDENT WHERE STUDENT_AGE = 18")
students = c.fetchall()
for student in students:
    print(student)


c.execute("UPDATE STUDENT SET STUDENT_AGE = 19 WHERE STUDENT_ID = 71")
a.commit()


print("\nStudents ordered by age:")
c.execute("SELECT * FROM STUDENT ORDER BY STUDENT_AGE DESC")
students = c.fetchall()
for student in students:
    print(student)


print("\nNumber of students in each age group:")
c.execute("""
    SELECT STUDENT_AGE, COUNT(*)
    FROM STUDENT
    GROUP BY STUDENT_AGE
    ORDER BY STUDENT_AGE
""")
age_groups = c.fetchall()
for age_group in age_groups:
    print(age_group)

print("\nAggregate values:")
c.execute("""
    SELECT COUNT(*) as total_students 
    FROM STUDENT
""")
result = c.fetchone()
print("Total students:", result[0])
c.execute("""
    SELECT AVG(STUDENT_AGE) as average_age 
    FROM STUDENT
""")
result = c.fetchone()
print("Average age:", result[0])
c.execute("""
    SELECT MIN(STUDENT_AGE) as youngest_age 
    FROM STUDENT
""")
result = c.fetchone()
print("Youngest age:", result[0])
c.execute("""
    SELECT MAX(STUDENT_AGE) as oldest_age 
    FROM STUDENT
""")
result = cursor.fetchone()
print("Oldest age:", result[0])


c.execute("""
               INSERT OR IGNORE INTO STUDENT VALUES (999, 'Temporary Student', 20)""")
c.execute("""
               DELETE FROM STUDENT WHERE STUDENT_ID = 999""")
a.commit()


a.close()