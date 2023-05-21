i=int(input("enter a number:"))
reves=0
while i>0:
    reves=reves*10+i%10
    i=i//10
    print(reves)