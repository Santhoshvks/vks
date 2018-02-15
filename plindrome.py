s= input('Enter the  number : ')

try:
  
  val = int(s)
    
if s == str(s)[::-1]:
        
print('The given number is PALINDROME')
   
else:
       
 print('The given number is NOT a palindrome')

except ValueError:
   
 print("That's not a valid number, Try Again !")
