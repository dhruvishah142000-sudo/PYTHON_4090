'''4) Write a program to insert the details of student in above table'''
import sqlite3

# Connect to database
con = sqlite3.connect("student.db")
cur = con.cursor()

# Create table (only first time)
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

# Input student details
print("Enter Student Details:")
rollno = int(input("Roll No: "))
name = input("Name: ")
gender = input("Gender: ")
age = int(input("Age: "))
email = input("Email: ")
mobile = input("Mobile: ")
city = input("City: ")

# Insert record
cur.execute("""
INSERT INTO student (rollno, name, gender, age, email, mobile, city)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (rollno, name, gender, age, email, mobile, city))

# Save changes
con.commit()

print("Student record inserted successfully!")

# Close connection
con.close()
