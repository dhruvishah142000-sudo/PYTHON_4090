# WAP to given year is leap year or not

year = int(input("Enter Year : "))

if (year%400)==0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
