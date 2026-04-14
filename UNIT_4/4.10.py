'''10) Write a program to read above file and use regular expression to 
display only those records who have mobile number with country code. 
For example, 91-9999933333 (2 digits of country code and 10 digits of
mobile)'''
import pandas as pd
import re

# Load Excel file
df = pd.read_excel("students.xlsx")

# Regular Expression: CC-XXXXXXXXXX
mobile_pattern = r'^\d{2}-\d{10}$'

print("=== Records with Mobile Number Having Country Code ===")

# Filter rows with valid country-code mobile numbers
valid_mobile_df = df[df['Mobile'].apply(lambda x: bool(re.match(mobile_pattern, str(x))))]

print(valid_mobile_df)
