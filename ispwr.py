def is_pwr(n):
  n=n/2
  if(n==2):
    print("Yes, it is a power of 2")
  elif(n>2):
    return is_pwr(n)
  else:
    print("No, it is not a power of 2")
n=int(input("Enter your choice:"))
is_pwr(n)
