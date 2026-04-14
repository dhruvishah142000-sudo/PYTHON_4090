'''
9) Write a program to do student operations using menu as follows
a) Add Student
b) Search Student
c) List All Students
d) Update Student
e) Delete Student
f) Exit '''

list=["Dhruvi","Hemang"]
while True:
    print("\n 1) Add Student ")
    print("\n 2) Search Student ")
    print("\n 3) List All Students ")
    print("\n 4) Update Student ")
    print("\n 5) Delete Student ")
    print("\n 6) Exit.. ")

    ch = int(input("\n Enter your Choice : "))

    match ch:
        case 1:
            std = input("\n Enter Student Name : ")
            list.append(std)
            print(list)
            
        case 2:
            name = input("\n Search Student Name : ")
            if name in list:
                print(f"\n {name} is in the list..")
            else:
                print(f"\n {name} is not in the list..")

        case 3:
            print("\n List of all students : \n",list)

        case 4:
            index = int(input("Enter Index No : "))
            lst = input("Enter Name for Update : ")

            list[index]=lst
            print("After Change in list : ",list)

        case 5:
            print(list)
            i = int(input("\n Enter Index to delete from the list : "))
            del list[i]
            print("\n",list)

        case 6:
            print("\n You are exited")
            exit()

        case _:
            print("Choose Right Option..")
            

        
        

        
            
