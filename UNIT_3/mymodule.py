# EX-4 Unit-2 Create a module with 4 functions of your choice.Import and use the functions using module in different ways.

import mymodule

n1 = int(input("Enter num1 : "))
n2 = int(input("Enter num2 : "))

def sum(num1,num2):
    add=num1+num2
    print(f"Sum of {num1} and {num2} is - {add}")

def sub(num1,num2):
    subt=num1-num2
    print(f"Sub of {num1} and {num2} is - {subt}")

def mul(num1,num2):
    mult=num1*num2
    print(f"Mul of {num1} and {num2} is - {mult}")

def div(num1,num2):
    divi=num1/num2
    print(f"Div of {num1} and {num2} is - {divi}")

mymodule.sum(n1,n2)
mymodule.sub(n1,n2)
mymodule.mul(n1,n2)
mymodule.div(n1,n2)
