s=int(input("enter the number:"))
m=[]
sum=0
while(s>0):
  rem=s%10
  s=int(s/10)
  m.append(rem)
for  i in  m:
  s+=(i**2)
print(s)
