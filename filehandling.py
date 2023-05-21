f = open(r"C:\Users\Asus\Desktop\trial\new.txt ", 'a')

f.write("hello world ")
f.close()

f = open(r"C:\Users\Asus\Desktop\trial\new.txt ", 'r')
obj = f.read()
print(obj)
f.close()
