a=[]
size=int(input("how many number want to enter"))
for i in range (size):
    val=int(input("enter a number"))
    a.append(val)
    print(a)
    sum=0
for i in range (size):
    sum=sum+a[i]
    i=i+1
    print(sum)
