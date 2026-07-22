# conditions
# true/false
# if block

x = int(input("Enter the number: "))
if x>15 :
    print("number is greater than 15 ")



x = int(input("Enter the number: "))
if x>15 :
    print("number is greater than 15 ")    
else :
    print("num is smaller ") 



x = int(input("Enter the number: "))
if x>15 :
    print("number is greater than 15 ")  
elif x==15 :
    print("number is equal to 15")  
else :
    print("num is smaller ") 


marks = 85

if marks >=90 :
    print("A")
elif marks>80 :
    print("B")
elif marks>70 :
    print("C")
elif marks>60 :
    print("D")
else :
    print("study more")




if "" :
    print("Inside if")
else :
    print("inside else")



if 0 :
    print("Inside if")
else :
    print("inside else")


# nested condition

x = 4

if x>5 :
    print("x is greater than 5")
    
    if x%2==0 :
        print("x is also even")
    else :
        print("x is odd")
else:
    print("x is less than 5 , so not calculating even or add")
        