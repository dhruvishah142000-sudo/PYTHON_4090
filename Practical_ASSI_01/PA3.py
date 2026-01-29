# Print the sum of square of number

num = int(input("Enter Number : "))
total = 0

for i in range(1,num+1):
    sq = i*i
    print(f"Square of {i} is : {sq}")
    total += sq

print(f"\n Sum of square of number is : {total} ")    

 
