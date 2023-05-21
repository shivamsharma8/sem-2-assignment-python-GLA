n=int(input("enter a number"))
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print(n,'number is perfect')
else:
        print(n,'number is composite')
  # by while loop
n=int(input("enter a number")) 
sum=0
i=1
while n%1==0:
     sum=sum+1
     i=i+1
if sum==n:
     print(sum )