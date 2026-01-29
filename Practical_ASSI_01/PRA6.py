# Find Largest number from given 3 number

n1 = int(input("Enter Number 1 :"))
n2 = int(input("Enter Number 2 :"))
n3 = int(input("Enter Number 3 :"))

if n1>n2 and n1>n3:
    print(f"{n1} is Big")
elif n2>n1 and n2>n3:
    print(f"{n2} is Big")
else:
    print(f"{n3} is Big.")
    
