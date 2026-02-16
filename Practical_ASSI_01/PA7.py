''' WAP to perform the implement the following operations on following list:
list1 = [physics,chemistry, 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

i.List Concatenation , ii. Remove list1[3] , iii. Add “Java” in List1 iv. Update list2 as list2[3]=11
v. del list2[2] vi. Print “ Welcome to Marwadi University “ 4 times in output
vii . Slicing operations: list1[-2], list2[1:3], list1[-1:-3]
viii. Find the lengh of list 2
ix. Find maximum element in List1
x. Find minimum element in List2
xi. Use list2.append(2)= 100
xii. Perform extend operation on list
xiv. Illustrate difference between POP and remove practically
xv. Perform reverse() on list1
xvi. Arrange elements in descending order in list2
'''
from os import remove

list1 = ['physics','chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print("1.",end=" ")
print(list1+list2)
print("2.",end=" ")
del list1[3]
print(list1)
print("3.",end=" ")
list1.append('Java')
print(list1)
print("4.",end=" ")
list2[3] = 11
print(list2)
print("5.",end=" ")
print(list1[-2])
print(list2[1:3])
print(list1[-1:-3])
print("6.",end=" ")
print(len(list2))
print("7.",end=" ")
print(max(list2))
print("8.",end=" ")
print(min(list2))
print("9.list2.append(2) = 100 -> it returns an error")
print("10",end=" ")
list1.extend(list2)
print(list1)
print("11. Using POP :- ",end=" ")
list1.pop()
print(list1)
'''print("11. Using Remove :- ",end=" ")
list1.remove()
print(list1)'''
print("12.",end=" ")
list1.reverse()
print(list1)
print("13.",end=" ")
list2.sort()
list2.reverse()
print(list2)






