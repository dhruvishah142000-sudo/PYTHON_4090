# Perform diffrent kind of operation on list..

print("\n1. For Access an element from a list")
print("2. Add a value in a list")
print("3. Remove a value from list.")
print("4. To do sum of a list values.")
print("5. To find a value.")


menu = [10,20,30,40,50,60]

choice = int(input("\n Enter Your Choice : "))

if choice==1:
    ch = int(input("Enter index to get a value from list : "))
    print(menu[ch])

elif choice==2:
    ch = int(input("Enter a value in list : "))
    menu.append(ch)
    print(f"Element {ch} is added.")
    print(menu)
    
elif choice==3:
    ch = int(input("Enter a value to delete of list : "))
    menu.remove(ch)
    print(f"Element {ch} is removed.")

elif choice==4:
    total=sum(menu)
    print(f"The total of lists all elements is : {total}")

elif choice==5:
    ch = int(input("Enter a value to find from list : "))
    if ch in menu:
        print(f"{ch} is available in the list.")
    else:
        print(f"{ch} is not available in the list.")

else:
    print("Choose Right Option")
    
    
