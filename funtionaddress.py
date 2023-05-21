def display(a):
    a.append(100)
    print("inside funtion",a)
    print(id(a))
    a=[100,200]
    print(a)
    print(id(a))
    display(a)
    print("before funtion call",a)
    print(id(a))

def display(a):
    a.touple(90,80)
    print("inside funtion",a)
    print(id(a))
    a=[10,20]
    print(a)
    print(id(a))
    display(a)
    print("before funtion call",a)
    print(id(a))
def display(a):
    a=100
    print("inside funtion",a)
    
    a=50
    print("before funtion call",a)
    display(a)
    print("after funtion.call",a)

def display():
  global a
  a=100
print("inside funtion",a)
    
a=50
print("before funtion call",a)
display(a)
print("after funtion.call",a)
 
def display():
    a=10
    print("if",a)
def d():
    nonlocal a
    print("nested funtion",a)
    d()
    return a
    a=140
    print("bfc",a)
    print(display)



