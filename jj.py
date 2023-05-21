s=lambda x:x*x*x
print(s(16))
l=[1,2,3,4,5]
def cube(x):
    return x*x*x
new=list(map(cube,l))
print(new)
l=[1,4,5,7,89,5]
def filter_funtion(a):
    return a>5
new=list(filter_funtion,l)
print(new)