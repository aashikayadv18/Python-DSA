#Sequance data type
#Tuple data type 
#orderd,sequance,diffrent typr of data
#immutable

tup1 = (1,2,3,4,5,6,76,8)
print(tup1)
print(type(tup1))

t1 = tuple([1,3,6])
print(t1)

t2 = tuple("Ashika")
print(t2)

t = (34) #python confused
print(t)
print(type(t))

t = (34,)
print(t)
print(type(t))

fruit = ('apple','banana','mango','apple','papaya','banana','apple','graps')
print(fruit.count('apple'))
print(fruit.index('apple'))
print(len(fruit))

print(fruit[3])

# fruit[3] = 'appa'

#slicing

print(fruit[2:4])