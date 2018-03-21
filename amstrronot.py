low= int(input("Enter low range: "))
upp= int(input("Enter upp range: "))
 
for num in range(lowupp + 1):
   
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   if num == sum:
       print(num)
