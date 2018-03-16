num_list = list(range(1, 100))
 
odd_nums = []
even_nums = []
 
for i in num_list:    
    if i % 2 == 0:        
        even_nums.append(i)
    else:       
        odd_nums.append(i)
 

 print(odd_nums)
