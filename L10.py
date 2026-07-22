# operators

# 3 + 4 (operants)
#7 type of operator

num1 = 10
num2 = 20

print(num1+num2)
print(num1*num2)
print(num1/num2)
print(num1-num2)
print(num2//num1)
print(num1%num2)
print(num1**num2)
# num = input("enter the number :" )

pos_inf = float("inf")
neg_inf = float("-inf")
print(neg_inf)
print(pos_inf)
print(pos_inf==neg_inf)
print(pos_inf<neg_inf)
print(pos_inf>neg_inf)

#comparison operator
num1 = 10
num2 = 20
print(num1==num2)
print(num1!=num2)
print(num1<num2)
print(num1<=num2)
print(num1>=num2)
print(num1>num2)

x=float('nan')
y=5
z=float('nan')
print(x == y)
print(x == z)


#Assignment operator

name = "Vishwa"

x = 5

x = x+5
x +=5
print(x)
x -=3
print(x)
x*=2
print(x)
x/=4
print(x)


#logical operator
# T and T
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(True)
print(False)
print(not True)

#bitwise operator

num1 = 5
num2 = 3

print(num1 & num2)
print(num1 | num2)

print(0.9-3*0.3)

num = 5
print(num << 1)

mum = 14
print(num << 1)
print(num>>1)

#identity operator

x = 5
y = 5
print(x is y)

arr1 = [1,2,3]
arr2 = [1,2,3]
print(arr1 is arr2)
print(arr1 is not arr2)

#membership operator

my_list = [1,2,3,4,5]

print( 5 in my_list)
print( 7 in my_list)

print( 5 not in my_list)
result = 4+5*6
print(result)


# terniory operator

num = 5

if num >= 0 :
    print("number is positive")
else :
    print("number is nagative")

# terniory operator

num = 5

result = "postive" if num >=0 else "negative"
print("number is :", result)