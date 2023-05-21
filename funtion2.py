#a=2
#=4
#def add():
 #   c=a+b
  #  return c
#print(add()
#default
#def display(name,mb,rollno,country='india'):
 #   print('hello',name,mb,rollno,country)
#display("ayush",4,4,'UK')
#display("ayush",4,4)
#def display(*args):
 #   print(args)
  #  print(len(args))
   # print(type(args))
#display()    
#display(10)
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
def greater(x,y,z):
    if (y>x and y>z):
        return y
    elif (x>y and x>z):
        return x 
    else :
        return z
r=greater(a,b,c)   
print(r)
    



