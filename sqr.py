s=int(input("enter the number:"))
l=[]
sum=0
while(s>0):
  rem=s%10
  s=int(s/10)
  l.append(rem)
for  i in  l:
  s+=(i**2)
print(s)
