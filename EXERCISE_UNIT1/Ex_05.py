# Largest Odd number

for i in range(1,11):
    num = int(input(f"Enter Number {i} : "))
    
    if num%2!=0:
        odd = max(n for n in num)
        print("Largest Odd Number is : ",odd)


        
