N=int(input(''))
pro=1
while(N>0):
  G=N%10
  pro=pro*G
  N=N//10
print("Product of digits:",pro)
