with open("input.txt") as f:
    nums = []
    line_nums = 0
    for line in f:
        line = line.rstrip()
        line_nums += 1
        if len(nums) == 0:
            nums = [0] * len(line)
            
        for ind in range(0,len(line)):
            bit = line[ind]
            if bit == "1":
                nums[ind] += 1
                
    bit_list = [(round(num/line_nums)) for num in nums]
    
    gamma_bit_str = "".join([str(bit) for bit in bit_list])
    epsilon_bit_str = "".join([str(1-bit) for bit in bit_list])

    gamma_rate = int(gamma_bit_str,2)        
    epsilon_rate = int(epsilon_bit_str,2)
    
    print(gamma_rate * epsilon_rate)
                
        
with open("input.txt") as f:
    