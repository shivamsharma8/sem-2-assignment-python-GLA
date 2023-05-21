d={1:'a',1:'b'}
del d
print(d)
#append 
d={1:'a',2:'b'}
d[1]="hello"
print(d)
d.update({7:"ayush"})
print( d)
#pop
a={1:'a',2:"b"}
print(a.len())
#from keys
v={1:'a',2:'b',3:'c'}
d=dict.fromkeys(v,'vowels')
print(d)
#write a program to enter a item on a dictionary.
a={}
n=int(input('size'))
for i in range(n): 
 k=input('enter a key')
v=input('value')
a.update({k:v})
print(a)





