a=[]
size=int(input("how many number want to enter"))
for i in range (size):
    val=int(input("enter a number"))
    a.append(val)
    even=0
    odd=0
for i in range(size):
    if a[i]%2==0:
       even=even+1
       print('even number')
    else:
        odd=odd+1
        print(odd)   


     