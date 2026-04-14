'''5) Write a program to update the details of student in above table'''
import mysql.connector

# Establish connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

cur = con.cursor()

# Input: which student to update
rno = int(input("Enter roll number of student to update: "))

# Check if student exists
cur.execute("SELECT * FROM student WHERE rollno = %s", (rno,))
record = cur.fetchone()

if record:
    print("Current Details:")
    print("Roll No:", record[0])
    print("Name:", record[1])
    print("Marks:", record[2])

    # Ask new values
    new_name = input("Enter new name: ")
    new_marks = int(input("Enter new marks: "))

    # Update Query
    cur.execute(
        "UPDATE student SET name = %s, marks = %s WHERE rollno = %s",
        (new_name, new_marks, rno)
    )

    con.commit()
    print("\nRecord updated successfully!")

else:
    print("❌ Student not found!")

# Close connection
cur.close()
con.close()
