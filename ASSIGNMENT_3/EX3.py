''' 3. Function to Calculate Factorial (Using Recursion) Implement factorial using:
        o Normal function
        o Recursive function '''

fact = int(input("Enter Number : "))

def factorial(f):
    for i in range(1,f):
        f = f * i
    print("\n Normal Function")
    print(f"Factorial is : {f}")

factorial(fact)

def fact_recu(f):
    if f<0:
        return "do not give input negative numbers."
    else:
        factt=1
        for i in range(1,f+1):
            factt=factt*i
        return factt

print("\n Recusrsion Function")
print(fact_recu(fact))


    
