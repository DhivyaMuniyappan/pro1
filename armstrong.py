n=int(input("enter your value:"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
  print("Given num is an Armstrong number")
else:
  print("Given num is not an Armstrong number")
