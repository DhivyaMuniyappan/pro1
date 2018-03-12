n=int(input("Enter the total num:"))
a=[]
for i in range(n):
  b=int(input("Enter the num:"))
  a.append(b)
print(a)
tot=sum(a)
avg=tot/n
print("Total,Avg is :",tot, avg)
