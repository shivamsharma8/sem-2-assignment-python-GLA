import os

print(os.getcwd())
#os.mkdir("data")
for i in range(0,100):
    if os.path.exists(f"data{i+1}"):
        os.remove(f"data{i+1}")
    else:
        print("the file do not exist")

#    path = os.path.join("C:\Users\Asus\PycharmProjects\pythonProject2",f"dta{i+1}")
#    os.remove(path)


