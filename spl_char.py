sc="!@#$%^&*()`~-_=+]}[{\|;:'/?.>,<"
str=input()
count=0
for i in str:
  if i in sc:
    count+=1
print(count)
