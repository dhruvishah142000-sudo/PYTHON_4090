'''Create an excel file with columns RollNo, Name, Gender, E-Mail, Mobile, Age 
and City. Enter atleast 20 records and then perform following exercise
1) Write a program to load above excel file and display columns of file and 
data type of each column.'''
import pandas as pd

# Load Excel file
df = pd.read_excel("students.xlsx")   # change file name if needed

# Display column names
print("Columns in the Excel file:")
print(df.columns)

# Display data types of each column
print("\nData Types of Each Column:")
print(df.dtypes)
