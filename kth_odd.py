n,k=map(int,input().split(' '))
lis=list(map(int,input().split(' ')))
arr=[]
for i in lis:
  if(i%2!=0):
    arr.append(i)
print(arr[k-1])
