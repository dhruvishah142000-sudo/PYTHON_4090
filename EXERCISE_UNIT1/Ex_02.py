
# Arithmatic Operation

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
n3 = input("Enter Operator : ")

if n3=="+":
    add=n1+n2 #Addition
    print("Addition is : ",add)

elif n3=="-":
    sub=n1-n2 #Subtraction
    print("Subtraction is : ",sub)

elif n3=="*":
    mul=n1*n2 #Multiplication
    print("Multiplication is : ",mul)

elif n3=="/":
    div=n1/n2 #Division
    print("Division is : ",div)

else:
    print("Choose Valid Operator")

    
