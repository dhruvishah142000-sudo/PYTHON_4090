''' 4. Function with Default Arguments
 Write a function to calculate simple interest.
 Keep rate default as 5%. '''

p = float(input("Enter Principle Amount : "))
r=5
n = float(input("Enter Number of years : "))


def Simple_Interest(pri,rate,no):
    si = (pri*rate*no)/100
    print(f"\nPrinciple is {pri} \n rate is {rate}% \n time is {no} year \n Simple Intrest is {si}")

Simple_Interest(p,r,n)
