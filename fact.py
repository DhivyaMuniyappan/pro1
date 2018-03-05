x=int(input("enter your choice:"))
fact=1
if(x<0):
  print("plz enter positive num")
elif(x==0):
  print("fact of 0 is 1")
else:
  for i in range(1,x+1):
    fact=fact*i
  print("factorial of the given num is:",fact)
