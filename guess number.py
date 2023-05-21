import random
computer=random.randrange(1,100)
user=int(input("enter a number"))
if user>computer:
    print("number is highest ")
elif user<computer:
    print("number is less") 
else:
    print("number geranate ")   