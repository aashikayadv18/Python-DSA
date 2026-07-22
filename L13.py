# loops - repeart multiple times
# for loop
# while loop


# for loop
fruits = ["apple","banana","cherry","date","elderberry"]

for fruit in fruits :
   print(fruit)

name = "Aashika Yadav"

for ch in name :
   print(ch, end=" ")


for i in range(10):
   print(i)

for i in range(2 , 7):
   print(i)

# the 3rd 2 in incriment value
for i in range(2,10,2): 
   print(i)

for i in range(2,10,3): 
   print(i)

for i in range(10,0,-1): 
   print(i)

for i in range(12,0,-3): 
   print(i)

# controling the flow of loop
# break
# contineu


for num in range(1,13): 
   if (num%4 ==0):
    break

   print(num)

# contineu

for x in range(11):
   if(1%2 !=0):
    continue
   print(x)

# nested loop

# for i in range(10):
#    for j in range(5):
#       print("Hello World")


for i in range(10):
   for j in range(5):
      if j%2==0 :
         break
      print(j) 
    #   break and cont always apply to the  