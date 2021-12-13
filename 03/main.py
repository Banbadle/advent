# PART 1
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
                
  
# PART 2
class Node():
    def __init__(self, depth=0):
        if depth>=0:
            self.one = Node(depth-1)
            self.zero = Node(depth-1)
            self.num = 0
        else:
            self.one = None
            self.zero = None
            self.num = None
            
    def add(self, string):
        if string == "":
            return
        
        char = string[0]
        if char == "1":
            self.one.num += 1
            self.one.add(string[1:])
        elif char == "0":
            self.zero.num += 1
            self.zero.add(string[1:])
        else:
            raise Exception("Not 0's and 1's")
                
    def get_ones(self):
        return self.one.num
    def get_zeros(self):
        return self.zero.num
            
        
with open("input.txt") as f:
    tree = None
    for line in f:
        line = line.rstrip()
        if tree == None:
            tree = Node(len(line))
            
        tree.add(line)

def get_ogr_cgr(cgr=False):
    ogr_list = []
    curr_node = tree
    while curr_node.get_ones() != None:
        ones = curr_node.get_ones()
        zeros = curr_node.get_zeros()
        
        condition = condition = zeros <= ones
        if cgr==True:
            condition = (zeros > ones and ones > 0) or zeros == 0
    
        if condition:
            ogr_list.append("1")
            curr_node = curr_node.one
        else:
            ogr_list.append("0")
            curr_node = curr_node.zero
            
    ogr_bit_str = "".join([str(bit) for bit in ogr_list])
    ogr_rate = int(ogr_bit_str,2) 

    return ogr_rate

ogr = get_ogr_cgr()
cgr = get_ogr_cgr(True)

print(ogr * cgr)
        
