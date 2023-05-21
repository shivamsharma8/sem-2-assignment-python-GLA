i=int(input("enter the number:"))
orig=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
    if orig==sum:
        print("number is amstrong")
    else:
        print("number is not amstrong")                                