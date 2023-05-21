a=input("enter a string:")
for index , letter1 in enumerate (a):
 for letter2 in a [index+1:]:
  if letter1 ==letter2:
   print( letter1)
  exit(0)
 else:
  print("number is not mathched")
