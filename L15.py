# loop questions

sum =0

for num in range(1,21):
    if num%2 ==0:
        sum += num
    print("sum of even num are ",sum)



str = input("please provide the string")
count = 0
for ch in str :
    # check if ch is a vowel or not
    if ch. lower() in ['a','e','i','o','u']:
        count+=1

print("total count of vowel is ", count)


# nth tern

n= int(input("please enter the value of -upto which we want the fibpnacci series"))

if (n<=0):
    print("nuber enterd is not correct . it should be >0 . entered num ", n )

    print(1, end=" ")
    if (num==1):
        pass
    else :
        print(1,end="")
        if (n==2):
            pass
        else:
            # print teh remaining of the series
            prev = 1
            prev_prev=1
            for num in (3, n+1):
                print(prev+prev_prev, end=",")
                prev, prev_prev = prev+prev_prev,prev




# prime or not

num = int(input("enter the num"))

isprime = True
if(num<=1):
    isprime = False

for i in range (2,int(num/2)+1):
    if num%i ==0:
     isprime =False 
    break

print("number passsed is prime :",isprime)


# 

num = int(input("enter the number to genrate the multipliction table"))

for i in range(1,11):
    print(num,"*",i,"=",num*i)




# pattern

for row in range(5):
    for j in range(row+1):
     print("*",end="")
    print()