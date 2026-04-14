'''7) Write a program to display only those records who have valid email 
address as their information. Use regular expression here.'''
import mysql.connector
import re

# Email validation regex pattern
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

cur = con.cursor()

# Fetch all records
cur.execute("SELECT rollno, name, email FROM student")
records = cur.fetchall()

print("Students with Valid Emails:\n")

valid_found = False

for r in records:
    rollno, name, email = r

    # Check email with regex
    if re.match(email_pattern, email):
        valid_found = True
        print(f"Roll No: {rollno}, Name: {name}, Email: {email}")

if not valid_found:
    print("No valid email IDs found!")

# Close connection
cur.close()
con.close()
