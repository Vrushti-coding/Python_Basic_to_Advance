n=int(input("Enter number of terms:"))
n1,n2=0,1
for _ in range(n):
    print(n1)
    temp=n1
    n1=n2
    n2=temp+n2