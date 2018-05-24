Hoo=input('')
if(len(Hoo)%2==0):
  Hoo=Hoo[:int((len(Hoo)/2))-1]+'**'+Hoo[int((len(Hoo)/2))+1:]
else:
  Hoo=Hoo[:int((len(Hoo)/2))]+'*'+Hoo[int((len(Hoo)/2))+1:]
print(Hoo)


