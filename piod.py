num_list = list(range(1, 100))
 
odd_nums = []
even_nums = []
 
for x in num_list:    
    if x % 2 == 0:        
        even_nums.append(x)
    else:       
        odd_nums.append(x)
 

print(odd_nums)
