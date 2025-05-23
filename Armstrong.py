# Date:9/5/2025
# Author:Vrushti Patel
# program:Number is armstrong or not
n=153 #1*1*1+ 5*5*5+ 3*3*3= 153
s=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10 #r=3 r=5 r=1
    sum=sum+(r**b) #sum=27 sum=125+27=152 sum=1+152=153 
    n=n//10 #n=15 n=1 n=0
if s==sum:
    print(s,"is armstrong number")
else:
    print(s,"is not armstrong number")