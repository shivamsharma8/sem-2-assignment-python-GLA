
f=open("C:\Users\Ayushman\Desktop\\u\\sum.txt","w")
a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=a+b
f.write("first number"+str(a))
f.write("\tsecond number"+str(b))
f.write("/taddition"+str(c))
f.close()

