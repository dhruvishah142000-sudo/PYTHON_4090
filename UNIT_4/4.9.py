'''9) Write a program to read above file and use regular expression in order to 
display records who has valid emails'''
import pandas as pd
import re

# Load Excel file
df = pd.read_excel("students.xlsx")

# Regular expression for validating email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("=== Records with Valid Emails ===")

# Filter rows with valid email
valid_email_df = df[df['E-Mail'].apply(lambda x: bool(re.match(email_pattern, str(x))))]

print(valid_email_df)
