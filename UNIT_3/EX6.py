# Write a program to read a file which contains only numbers.
# Display total of all numbers with maximum and minimum number.

file1 = open("file1.txt","w")
numbers = ["\n10","\n20","\n30","\n40","\n50","\n60"]
file1.writelines(numbers)
file1.close()

file1 = open("file1.txt","r+")
content = file1.read()
print(content)
data = list(map(int,content.split()))

print(f"Sum of total elements is :",sum(data))
print(f"Maximum elements is :",max(data))
print(f"Minimum elements is :",min(data))

file1.close()
