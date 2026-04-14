'''2) Write a program to display all the records of student table (make use of 
fetchall() method)'''
import sqlite3

# Connect to database
con = sqlite3.connect("student.db")
cur = con.cursor()

# Select all records
cur.execute("SELECT * FROM student")

# Fetch ALL records at once
records = cur.fetchall()

print("=== Student Records (Using fetchall) ===")

# Loop through the list and print each record
for row in records:
    print(row)

# Close connection
con.close()
