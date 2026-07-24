# function is a block of code which can be reuse or recolled

def myfunc():
    print("hello student")
myfunc()

def add(a,b):
    sum=a+b
    return sum


print(add(20,20))
# global variable /scope
x = 101 
def func():
    x =102
    print(x)


func()
print(x)

# difffrent type of argument
# default argument

# def greet(name,masage="good morning"):
#     print(name,masage)
# greet("AAshi")

# keyword argument
def greet(name,age,masage):
    print(masage,name,"your age is",age)
greet(age=19,masage="hello",name="aashi")

# position argument

def add_numbers(x,y):
    print("x",x)
    print("y",y)
    print(x+y)

add_numbers(12,13)

def sum_numbers(*args):
    print(type(args))
    print(args)

    sum = 0
    for num in args :
        sum +=num
    return sum

print(sum_numbers(1,2,3,4,5))

def sum_numbers (a,b,*args):
    print(a)
    print(b)
    print(args)
    print(*args)

sum_numbers(5,6,8,9,7)

# 

# def display_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

#     for key, value in kwargs :
#         print(key, " -> ",value)

# # display_info(name="aashi",age=19,city ="jabalpur")

# def dunc(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# func(5,6,7,89,name="aashi",age=19)

# return type

def add_numbers(a: int,b:int) -> int:
    return a+b 
print(add_numbers(5,6,7,7))


# nested function
def outer():
    print("Hello from the outer")
    def inner():
      print("Hello from the inner")

      return inner
func(outer)