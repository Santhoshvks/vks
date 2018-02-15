num1 = 33

num2 = 67

num3 = 51


if (num1 > num2) and (num1 > num3):
 biggest = num1
elif (num2 > num1) and (num2 > num3):
 biggest = num2
else:
 biggest = num3

print("The biggest number between",num1,",",num2,"and",num3,"is",biggest)
