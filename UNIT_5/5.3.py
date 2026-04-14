'''3) Write a program to search for particular student and display the details of 
student. If student is not found, related message shall be displayed'''
import sqlite3

# Connect to database
con = sqlite3.connect("student.db")
cur = con.cursor()

# Input roll number to search
roll = int(input("Enter Roll Number to Search: "))

# Execute query
cur.execute("SELECT * FROM student WHERE rollno = ?", (roll,))

# Fetch result
record = cur.fetchone()

# Check if record exists
if record:
    print("=== Student Found ===")
    print("Roll No:", record[0])
    print("Name:", record[1])
    print("Gender:", record[2])
    print("Age:", record[3])
    print("Email:", record[4])
    print("Mobile:", record[5])
    print("City:", record[6])
else:
    print("Student not found!")

# Close connection
con.close()
