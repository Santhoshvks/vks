n=int(input("Enter upper limit: "))
for x in range(2,n+1):
    l=0
    for i in range(2,x//2+1):
        if(x%i==0):
            l=l+1
    if(l<=0):
        print(x)
