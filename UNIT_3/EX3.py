# WAP TO LOG FILE OF

#CREATE LOG FILE :

import logging
logging.basicConfig(filename="error.txt",level=logging.ERROR)

try:
    n1 = int(input("Enter a num1 : "))
    n2 = int(input("Enter a num2 : "))
    res = n1/n2
    print(res)

except Exception as e:
    print("Can't divide by zero..")
    logging.error(e)        
