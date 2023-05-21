a=int(input("enter a first number"))
b=int(input("enter a number"))
maxnum=max(a,b)
while(True):
 if(maxnum%a==0 and maxnum%b==0):
  break
maxnum=maxnum+1
print(maxnum)


