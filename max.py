a=[]
size=int(input("enter size of list"))
for i in (size):
 val=int(input("enter a number"))
a.append(val) 
max=a[0]
for i in range(size):
    if a[i]>max:
        max=a[i]
        print(max)
