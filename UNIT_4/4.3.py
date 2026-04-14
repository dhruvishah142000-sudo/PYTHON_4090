'''3) Write a program to load above excel file and use dropna() and fillna() 
functions separately.'''
import pandas as pd

# Load Excel file
df = pd.read_excel("students.xlsx")

print("=== Original Data ===")
print(df)

# -------------------------------
# 1) Using dropna()
# -------------------------------
print("\n=== Data after dropna() ===")
drop_data = df.dropna()   # removes rows with any missing values
print(drop_data)

# -------------------------------
# 2) Using fillna()
# -------------------------------
print("\n=== Data after fillna() ===")

# Fill missing values with default values
fill_data = df.fillna({
    'Name': 'Unknown',
    'Gender': 'Not Specified',
    'E-Mail': 'noemail@gmail.com',
    'Mobile': '0000000000',
    'Age': df['Age'].mean(),   # fill with average age
    'City': 'Unknown'
})

print(fill_data)
