with open("input.txt") as f:
    hex_packet = f.readline().rstrip()
    packet = int(hex_packet, 16)
    packet_length = len(hex_packet) * 4
    

n_last = 0

def next_n_digits(n):
    global packet
    global n_last
    offset = (packet_length - n_last) - n 
    ones = (0b1 << n) - 1
    n_digits = (packet & (ones << offset)) >> offset
    n_last += n
    # print(n_digits, n_last)
    return n_digits

def is_end():
    remaining_bits = packet & ((0b1 << (packet_length - n_last)) - 1)
    return remaining_bits == 0
 
version_total = 0

def gt(nums): return nums[0] > nums[1]
def lt(nums): return nums[0] < nums[1]
def eq(nums): return nums[0] == nums[1]
def prod(nums):
    i = 1
    for num in nums:
        i *= num
    return i

def parse():
    
    type_to_func = {0: sum, 1: prod, 2: min, 3: max, 5:gt, 6:lt, 7:eq}

    global version_total
    version = next_n_digits(3)
    type_id = next_n_digits(3)
    
    version_total += version
    
    if type_id == 4:
        literal = 0
        while not is_end():
            keep_reading = next_n_digits(1)
            next_subpacket = next_n_digits(4)

            literal = (literal << 4) | next_subpacket
            if not keep_reading:
                return literal
    
    length_type_id = next_n_digits(1)
    length = 15 if length_type_id == 0 else 11
    
    count_remaining = next_n_digits(length)
    
    parse_list = []
    while not is_end():
        n_initial = n_last
        next_parse = parse()
        parse_list.append(next_parse)
        
        count_remaining -= (n_last - n_initial if length_type_id == 0 else 1)
            
        if count_remaining <= 0 or is_end():
            func = type_to_func[type_id]
            return func(parse_list)
        
while not is_end():
    final_num = parse()
            
#Part 1
print(version_total)
        
#Part 2
print(final_num)
