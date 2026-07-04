#Sequance data type 
# (string )
#comprisses group of element , (string )group of charector\

name ='Aaasgika'
city = "Jabalpur"
country = '''India''' #(multiline)

name = 'Aashika Yadav'
print(name[3])
print(name[7])
print(name[-1])

str = "Aashika Yadav"
#  str[0]='x'
# print(str)

#here + is concatenation
first_name = "Vishwa"
last_name = "Mohan"
complete_name =first_name + " " +last_name # here + is concatenation
print(complete_name)

#Lenghth of the string

print(len(complete_name))

str = "Aashika Yadav"
print(str[2:4])
print(str[2:])
print(str[:])
print(str[:4])
print(str[-9:9])

str = "Aashika Yadav"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.strip())

#replace method

str = "Hello dera, I am very good, I am very nice , I am  wow"
print(str.replace("I am" , "we are",3))
print(str.replace("I am" , "we are"))

#Escape Character
print("Hello \n World") #\n new line
print("Hello\tWorld") #tab space
print("Hello \"World\"") #tab space