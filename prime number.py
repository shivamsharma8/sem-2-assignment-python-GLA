n=int(input("enter the number"))
count=0
i=1
while i<=n:
    if i%n==0:
        count=count+1
        i=i+1
if count==2:
    print("number is prime")   
else:
    print("number is coposite") 
    #sum of natural number
n=int(input("enter number"))  
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    print(sum)

