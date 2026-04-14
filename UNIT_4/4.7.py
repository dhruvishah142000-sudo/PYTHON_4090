'''7) Write a program to read above excel file and how many male and female 
students are there using bar graph'''
import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("students.xlsx")

# Count male and female students
gender_count = df['Gender'].value_counts()

print("Gender Count:")
print(gender_count)

# Plot bar graph
plt.bar(gender_count.index, gender_count.values)

# Labels & Title
plt.title("Male vs Female Students")
plt.xlabel("Gender")
plt.ylabel("Number of Students")

# Show graph
plt.show()
