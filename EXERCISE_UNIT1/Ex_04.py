# Armstrong

for i in range(1,11):
    num = int(input(f"Enter Number {i} : "))
    
    digits = str(num)
    n = len(digits)
    
    total = sum(int(digit) ** n for digit in digits)
    
    if num==total:
        print(f"This is Armstrong Number - {num} ")

    else:
        print(f"This is not a Armstrong Number - {num} ")
    

     
