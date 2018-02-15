year = int(input(" Enter the Year you wish: "))

 
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
 
   print("%d It is a Leap Year" %year)
else:
    
print("%d  It is Not the Leap Year" %year)
