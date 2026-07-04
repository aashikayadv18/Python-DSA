#list data type
#collection of element

students =["Aashi","Ariba","Anushka","Aakanksha"]
print(students)
print(type(students))

list2 = list(students) #list is constructor here
print(list2)

list3 = list("Ashika")
print(list3)

list4 = list((3,4,"Aashi"))
print(list4)

#Accessing the elemnts of the list

l1 = [1,2,3,4,5,6,7,8,9]
print(l1[3])

arr =[1,6,7,8,9]
arr.append(11)
print(arr)
arr.insert(3,43)
print(arr)

l1 = [1,2]
l2 = ["Vishwa", "Mohan"]
l1.extend(l2)
print(l1)

#remove elemnts from the lisst

l1 = [1,2,3,4,5,6,7,8,9]
l1.pop()
print(l1)

l1 = [1,2,3,4,5,6,7,8,9]
l1.pop(2) #remove by the index
print(l1)

l1 = [1,2,3,4,5,6,7,8,9]
l1.remove(1)  #it will remove first accurance of 1
print(l1)

#Replace the value at a index
#Replace the value at a range

students = ['a','b','c','d','e','f']

students[3]='f'
print(students)

students[1:4]='m','n','o'
print(students)

l1 = [1,2,3,4,5,6,7,8,9]
l1.reverse()
print(l1)

l1_copy = l1.copy() #new list which is a diffrent object
print(l1_copy)
print(id(l1_copy),id(l1))

l1.sort()
print(l1)