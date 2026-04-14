'''9) Write a program to create a list with 3 columns for name, data type and 
size. Create table as per the information entered. Consider following 
example
name varchar 20
qualification varchar 20
post varchar 20
salary int 6
Once above information is stored in list, program shall create a table from 
above information.'''
import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

cur = con.cursor()

# List to store column details (name, datatype, size)
columns = []

n = int(input("Enter number of columns: "))

for i in range(n):
    col_name = input(f"Enter column {i+1} name: ")
    data_type = input(f"Enter data type for {col_name} (varchar/int): ").lower()
    
    # Size only for varchar or int
    size = input(f"Enter size for {col_name}: ")

    columns.append((col_name, data_type, size))

# Build CREATE TABLE query dynamically
table_name = input("Enter table name: ")

query = f"CREATE TABLE {table_name} ("

col_defs = []

for col in columns:
    name, dtype, size = col

    if dtype == "varchar":
        col_defs.append(f"{name} VARCHAR({size})")
    elif dtype == "int":
        col_defs.append(f"{name} INT({size})")

# Join all column definitions
query += ", ".join(col_defs) + ")"

# Execute query
cur.execute(query)

print(f"Table '{table_name}' created successfully!")

# Close connection
cur.close()
con.close()
