def power(base,exp1):
   
 if(exp1==1):
        
return(base)
    
if(exp1!=1):
        
return(base*power(base,exp1-1))

base=int(input("Enter base: "))

exp1=int(input("Enter exponential value: "))

print("Result:",power(base,exp1))
