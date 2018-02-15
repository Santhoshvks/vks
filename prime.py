a=int(input("Enter number: "))
num=0
for i in range(2,a//2+1):
    if(a%i==0):
        num=num+1
if(num<=0):
    print("Number is prime")
else:
    print("Number isn't prime")
