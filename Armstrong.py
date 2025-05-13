# Date:9/5/2025
# Author:Vrushti Patel
# program:Number is armstrong or not
n=153
s=n
b=len(str(n))
sum=0
while(n!=0):
    r=n%10
    sum=sum+(r**b)
    n=n//10
if(s==sum):
    print(s,"is armstrong number")
else:
    print(s,"is not armstrong number")