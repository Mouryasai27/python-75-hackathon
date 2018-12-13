#Lists in Python
List = ["I","Love","Programming"]
print(List)

#Access elements in a List
print(List[0])
print(List[1])
print(List[2])

#Append the elements to a List1
List1 = ["I","Love","Python"]
List1.append("Programming")
print(List1)

#changing elements in a List1
List1[2] = "Java"
print(List1)

#printing all elements in a List1 using for loop
for i in List1:
     print(i,end=" ")
print("\n")

#Finding length of a List
print("Length of the List is: ",end="")
print(len(List))
print("Length of the List1 is: ",end="")
print(len(List1))

