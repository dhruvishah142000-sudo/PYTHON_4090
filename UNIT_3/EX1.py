# WAP TO DISPLAY EXCEPTION HANDLING IN PYTHON

try:
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    
    div = a/b
    print(div)
    
except ZeroDivisionError:
    print("Not Divisible..")

except ValueError:
    print("Insert Integer Value..")

except NameError:
    print("Insert Integer Value..")

except Exception as e:
    print("Undefined Error")

else:
    print("Division Succesfull")

finally:
    print("Program Executed Succesfully with or without error ...")
