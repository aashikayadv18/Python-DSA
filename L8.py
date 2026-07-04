# sets 
# all elements are unique
# unorderdd
# hecharogenious


my_set = {2,5,6,7,87,7}
print(my_set)
print(type(my_set))
 

s1 = {1,3,4,5,1,7,5,4,7}
print(s1)

s2 =set()
print(s2)

s3 = set({3,5,7})
print(s3)

#Add
s = set()
s.add(3)
s.add(13)
s.add(23)
s.add(43)
s.add(73)
print(s)


# Remove

s1 ={2,5,6,7,8,9}
s1.discard(9)
print(s1)


# immutable set (frozen set)


fs = frozenset([2,5,7,8,9,8])
print(fs)
print(type(fs))

dict1 ={fs , "aashi"}
print(dict1)