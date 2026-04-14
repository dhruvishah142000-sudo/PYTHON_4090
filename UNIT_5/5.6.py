'''6) Write a program to delete the details of student in above table'''
import mysql.connector

# Establish connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

cur = con.cursor()

# Input: which record to delete
rno = int(input("Enter roll number of student to delete: "))

# Check if record exists
cur.execute("SELECT * FROM student WHERE rollno = %s", (rno,))
record = cur.fetchone()

if record:
    print("Record Found:")
    print("Roll No:", record[0])
    print("Name:", record[1])
    print("Marks:", record[2])

    confirm = input("Are you sure you want to delete this record? (yes/no): ")

    if confirm.lower() == "yes":
        cur.execute("DELETE FROM student WHERE rollno = %s", (rno,))
        con.commit()
        print("\nRecord deleted successfully!")
    else:
        print("\nDelete operation cancelled.")

else:
    print("❌ Student not found!")

# Close connection
cur.close()
con.close()
