# WAP TO EXECUTE USER DEFINED EXCEPTION IN PYTHON - Not solved

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter Age : "))
    if age>=18 or age<=90:
        print("You are eligible for vote. ")
    else:
        raise InvalidAgeError(age)

except InvalidAgeError as ie:
    print("You are not eligible for vote.")
    print("Your age is - ",ie)
        
finally:
    print("Your age is greater then 18 so you are eligible for vote..")
        
