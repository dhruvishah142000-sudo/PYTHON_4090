'''5) Write a program to enter the name of 5 companies and its employee size 
and display as bar graph'''
import matplotlib.pyplot as plt

# Lists to store company data
companies = []
employees = []

print("Enter details of 5 companies:")

for i in range(5):
    name = input(f"Enter Company {i+1} Name: ")
    emp = int(input(f"Enter number of Employees in {name}: "))
    
    companies.append(name)
    employees.append(emp)

# Plot bar graph
plt.bar(companies, employees)

# Labels and title
plt.title("Employee Size of Companies")
plt.xlabel("Company Name")
plt.ylabel("Employee Size")

# Display graph
plt.show()
