n=int(input())
a = (n // 10) * 10
b = a + 10
if(abs(n-a)>abs(n-b)):
  print(b)
else:
  print(a)

 
