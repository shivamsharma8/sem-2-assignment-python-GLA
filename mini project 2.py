srt=int(input("enter the starting point: "))
end=int(input("enter the ending point: "))
upd=int(input("enter the updation: "))
r=end-srt
a=input("enter 'series' to print series in assending order and 'reverse' to print it in descending order: ")
b=input("enter 'H' to print the series in horizontal and 'V' to print in vertical: ")
if(upd>r):
   print("series cannot be printed,enter the correct parameters")
elif(a=='series'): 
    if(b=='H'):
       for i in range(srt,end+1,upd):
          print(i,end=' ')
    elif(b=='V'):
       for i in range(srt,end+1,upd):
          print(i,end='\n')
elif(a=='reverse'):
    if(b=='H'):
       for i in range(end,srt-1,-upd):
          print(i,end=' ')
    elif(b=='V'):
       for i in range(end,srt-1,-upd):
          print(i,end='\n')