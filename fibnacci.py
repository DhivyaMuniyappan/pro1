def fib(d):
  if(d<=1):
    return(d)
  else:
    return(fib(d-1) + fib(d-2))
a=int(input("Enter your choice:"))
for i in range(a):
  print(fib(i))
