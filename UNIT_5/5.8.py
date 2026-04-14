'''8) Write a program to load all the records from table and display only those details
where names start with "N" and has length of 5 characters.'''
import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

cur = con.cursor()

# Load all records
cur.execute("SELECT rollno, name, gender, age, email, mobile, city FROM student")
records = cur.fetchall()

print("Students whose name starts with 'N' and length = 5:\n")

found = False

for r in records:
    rollno, name, gender, age, email, mobile, city = r

    # Condition: starts with N and length 5
    if name.startswith("N") and len(name) == 5:
        found = True
        print(f"Roll No: {rollno}, Name: {name}, Gender: {gender}, Age: {age}, "
              f"Email: {email}, Mobile: {mobile}, City: {city}")

if not found:
    print("No record found matching the criteria.")

# Close
cur.close()
con.close()
