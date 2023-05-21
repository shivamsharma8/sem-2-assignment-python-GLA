a=[]
size=int(input("how many number want to enter"))
for i in range (size):
    val=int(input("enter a number"))
    a.append(val)
non_dublicate_value=set(a)
print(non_dublicate_value) 