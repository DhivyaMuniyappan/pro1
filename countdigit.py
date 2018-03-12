n=int(input("Enter your lucky num:"))
count=0
while(n>0):
  count=count+1
  n=n//10
print("Lucky num of digit is:",count)
