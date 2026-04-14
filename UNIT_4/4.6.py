'''6) Write a program to enter age of 50 students and create a histogram to 
display age as group of 0-10, 11-20, 21-30, 31-40, 41-50, 51-60, 60-120'''
import matplotlib.pyplot as plt

ages = []

print("Enter age of 50 students:")
for i in range(50):
    age = int(input(f"Enter Age of Student {i+1}: "))
    ages.append(age)

# Age groups (bins)
bins = [0, 10, 20, 30, 40, 50, 60, 120]

# Plot histogram
plt.hist(ages, bins=bins, edgecolor='black')

# Labels & Title
plt.title("Age Distribution of Students")
plt.xlabel("Age Groups")
plt.ylabel("Number of Students")

# Display graph
plt.show()
