# 5. Write a function inside another function. 

def Arith(n1,n2):
    def add():
        sum = n1+n2
        return sum

    def subt():
        sub = n1-n2
        return sub
    
    print("Addition :- ",add())
    print("Subtration :- ",subt())

    
Arith(5,2)
