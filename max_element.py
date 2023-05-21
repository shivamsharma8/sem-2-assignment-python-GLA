l = [2, 19.6, 54, 56646, 17]
lcopy = list(l)
print(l[::-1])
print(l[3:-2:1])
print(l[3:2:-1])
print(l[3:1:-1])
print(l[3:-2:-1])

print(l.pop(2))
l[2] = 21
l.insert(2, 456)
l.clear()
print(l)
del l

l = list(lcopy)
l.append(78)
print(sorted(l))
print(l)
print(l.sort(reverse=True))

l = ['e', 34, 'hello', 'class', 17]
print(l)
a, b, c, d, e = l
print(a, b, c, d, e)
print(l)
l = [a, b, c, d, e]
print(l, type(l))
t = (a, b, c, d, e)
print(t, type(t))
t = list(t)
print(t)
t[1] = 534
t = tuple(t)
print(t)
a, b, c, d, e = t
b = 'mishra'
t = (a, b, c, d, e)
print(t)
s = 'hello'
tup = tuple(s)
print(s)
print(tup)

#WAP to traverse each element of the list
#WAP to traverse each element of the tuple
#WAP to find even and odd element of the list
even, odd = 0, 0
l = [34,434,56,12,767,34,67]
for i in l:
    print(i)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("total even number :", even)
print("total odd number :", odd)
for i in t:
    print(i)

for i in range(len(l)):
    print(l[i])

print([x for x in range(1,11) if x % 2 == 0])



print(l)

a = 4, "hello"
print(type(a))

armstrong = int(input("enter the number"))
temp = armstrong
sum = 0
power = len(str(armstrong))
while temp != 0:

    rem = temp % 10
    sum = sum + (rem**power)
    temp = temp // 10
if sum == armstrong:
    print("armstrong number")
else:
    print("not armstrong")
