a=[]

size=int(input("how many number want to enter"))
for i in range (size):
    val=int(input("enter a number"))
    a.append(val)
a.reverse()
print(a)
a.reverse()
for i in range(size):
    
        print(a[i],end=" ")
    
print("")
for i in range(size):

    print(a[i])