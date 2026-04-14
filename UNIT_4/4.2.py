'''2) Write a program to load above excel file and display following information
- List of students from Rajkot City
- List of Male students
- List of Male students from Rajkot City 
FACULTY OF COMPUTER APPLICATIONS
Master of Computer Applications
- List of students whose age >= 20'''
import pandas as pd

# Load Excel file
df = pd.read_excel("students.xlsx")

print("=== Students from Rajkot City ===")
print(df[df['City'].str.lower() == 'rajkot'])

print("\n=== List of Male Students ===")
print(df[df['Gender'].str.lower() == 'male'])

print("\n=== Male Students from Rajkot City ===")
print(df[(df['Gender'].str.lower() == 'male') &
         (df['City'].str.lower() == 'rajkot')])

print("\n=== Students whose Age >= 20 ===")
print(df[df['Age'] >= 20])
