# Result

python = int(input("Enter Marks of Python Subject : "))
os = int(input("Enter Marks of OS Subject : "))
java = int(input("Enter Marks of Java Subject : "))
ds = int(input("Enter Marks of DS Subject : "))

print("\n--------RESULT--------")

total = python + os + java + ds
print("\n Total Marks Of Four Subjects : ",total)

per = total/4
print("\n Percentage is : ",per)

if per>=90 and per<=100:
    print("\n Grade : O")

elif per>=80 and per<90:
    print("\n Grade : A")

elif per>=70 and per<80:
    print("\n Grade : B")

elif per>=60 and per<70:
    print("\n Grade : C")

elif per>=40 and per<60:
    print("\n Grade : D")

else:
    print("\n You are Fail Your Percentage is : ",per)
