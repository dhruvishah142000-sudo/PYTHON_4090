'''Consider a student table with following columns for all database related 
programs (rollno, name, gender, age, email, mobile, city)
1) Write a program to display all the records of student table (make use of 
fetchone() method)'''
import sqlite3

# Connect to database (creates file if not exists)
con = sqlite3.connect("student.db")
cur = con.cursor()

# Create table (run only once – it will skip if exists)
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    rollno INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    age INTEGER,
    email TEXT,
    mobile TEXT,
    city TEXT
)
""")

# Select all records
cur.execute("SELECT * FROM student")

print("=== Student Records ===")
record = cur.fetchone()   # fetch first row

# Fetch records one-by-one
while record:
    print(record)         # display tuple data
    record = cur.fetchone()

# Close connection
con.close()
