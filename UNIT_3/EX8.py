''' 8) Write a program to read file which has marks entry of student and display details with total,
percentage and grade (Consider a file which has comma separated data with RollNo, Student Name,
Mark1, Mark2, Mark3 and Mark4)'''

# Open the file in read mode
with open("student.txt", "r") as file:
    print("RollNo | Name   | Total | Percentage | Grade")
    print("---------------------------------------------")

    for line in file:
        # Remove newline and split by comma
        data = line.strip().split(",")

        roll_no = data[0]
        name = data[1]
        marks = list(map(int, data[2:]))

        total = sum(marks)
        percentage = total / (len(marks) * 100) * 100  # assuming each subject is out of 100

        # Inline grade calculation
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"{roll_no} | {name:<6} | {total}   | {percentage:.2f}%     | {grade}")



