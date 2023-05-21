numa=int(input("enter a number"))
numb=int(input("enter a number"))
if numb>numa:
    mn=numa 
else:
    mn=numb
for i in range (1,mn+1,):
 if numa%i==0 and numb%i==0:
    hcf=i
    print(hcf)
