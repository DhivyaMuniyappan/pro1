def fib(n):
  if(n<=1):
    return n
  else:
    return (fib(n-1)+fib(n-2))
a=int(input("enter your num:"))
for i in range(a):
    print(fib(i))
