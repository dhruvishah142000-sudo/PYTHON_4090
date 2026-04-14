'''4) Write a program to enter the profit of 5 years and display the profit as 
line graph.'''
import matplotlib.pyplot as plt

# Input profit for 5 years
profits = []
years = []

print("Enter profit for 5 years:")

for i in range(5):
    year = int(input(f"Enter Year {i+1}: "))
    profit = float(input(f"Enter Profit for Year {year}: "))
    years.append(year)
    profits.append(profit)

# Plot line graph
plt.plot(years, profits, marker='o')

# Labels and Title
plt.title("Profit Over 5 Years")
plt.xlabel("Year")
plt.ylabel("Profit")

# Show grid
plt.grid()

# Display graph
plt.show()
