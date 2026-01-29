# WAP to display grade of student based on per. :

per = float(input("Enter Percentage : "))

if per>=90 and per<100:
    print(f"Grade - O ,Your Percentage is - {per}")
elif per>=80 and per<90:
    print(f"Grade - A ,Your Percentage is - {per}")
elif per>=60 and per<80:
    print(f"Grade - B ,Your Percentage is - {per}")
elif per>=50 and per<60:
    print(f"Grade - C ,Your Percentage is - {per}")
elif per>=40 and per<50:
    print(f"Grade - D ,Your Percentage is - {per}")
