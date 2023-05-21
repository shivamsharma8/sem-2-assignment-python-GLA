import time
t=time.strftime ('%H:%M:%S')
min=int (time.strftime('%M'))
print(min)
if min>44:
    print("sleeping time")
elif min<50:
    print("eating time")