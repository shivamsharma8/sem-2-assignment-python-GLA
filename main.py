start = int(input("enter start"))
stop = int(input("enter where to stop"))
jump = int(input("enter the spaces"))
option =(input("enter 0 for serial and 1 for reverse"))
align =(input("enter 5 for vertical and 6 for horizontal"))
if option != "0" or option != "1":
    print("invalid input")
else:
    if start > stop:
        if align == "5":
            for i in range(start, stop, -jump):
                print(i)
        elif align == "6":
            for i in range(start, stop, -jump):
                print(i, end=" ")
        else:
            print("invalid input")
    else :
        if align == "5":
            for i in range(start, stop, jump):
                print(i)
        elif align == "6":
            for i in range(start , stop, jump):
                print(i, end=" ")
        else:
            print("invalid input")