'''8) Write a program to enter course and no. of students in each course. 
Display information using pie graph. The course with maximum students 
shall be displayed separately as a separate slice of pie graph.'''
import matplotlib.pyplot as plt

courses = []
students = []

# Input course data
print("Enter course name and number of students:")

n = int(input("How many courses? "))

for i in range(n):
    course = input(f"Enter Course {i+1} Name: ")
    count = int(input(f"Enter Number of Students in {course}: "))

    courses.append(course)
    students.append(count)

# Find course with maximum students
max_index = students.index(max(students))

# Create explode list (0 for others, 0.2 for max)
explode = [0] * n
explode[max_index] = 0.2

# Plot pie chart
plt.pie(students, labels=courses, autopct="%0.1f%%", explode=explode, shadow=True)

# Title
plt.title("Students in Each Course")

# Display
plt.show()
