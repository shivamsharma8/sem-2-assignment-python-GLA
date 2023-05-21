a=[]
size=int(input("how many number want to enter"))
for i in range(size):
    val=int(input("enter a number"))
    a.append(val)
    print(a)
even=[]
odd=[]
for j in a:
    if j%2==0:
      even .append (j) 
    else:
       odd.append(j)
       print(even) 
       print(odd)
