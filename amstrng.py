i = int(input("Enter a number: "))
sum = 0
temp = i
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if i == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
