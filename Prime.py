# Date:20/5/2025
# Author:Vrushti Patel
# program:Check Prime number
no=int(input("Enter a number"))
flag=1
if no<=1 :
    flag=1
else:
    for i in range(2,(no//2)+1):
        if no%i==0:
            flag=1
            break
if flag==1:
    print(no," is prime number")
else:
    print(no,"is not prime number")