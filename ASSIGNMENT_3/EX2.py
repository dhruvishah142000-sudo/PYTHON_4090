''' 2. Function to Find Largest of Three Numbers
       Accept three numbers as parameters.
       Return the largest number. '''

num1=int(input("Enter Num1 : "))
num2=int(input("Enter Num2 : "))
num3=int(input("Enter Num3 : "))


def large(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(f"{n1} is the largest number.")
    elif n2>n1 and n2>n3:
        print(f"{n2} is the largest number.")
    else:
        print(f"{n3} is the largest number.")

large(num1,num2,num3)
