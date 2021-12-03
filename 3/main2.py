# PART 2
def get_rating(inv_bool = False):
    cgr_list = bin_list.copy()
    index = 0
    while len(cgr_list) > 1:
        cgr_map = {"0": 0, "1": 0}
        for item in cgr_list:
            cgr_map[item[index]] += 1
            
        max_bit = "1"* (1-inv_bool) + "0" * inv_bool
        if cgr_map["0"] <= cgr_map["1"]:
            max_bit = "0"* (1-inv_bool) + "1" * inv_bool
            
        cgr_list = list([string for string in cgr_list if string[index] == max_bit])
        index += 1
    cgr = int(cgr_list[0],2)
    
    return cgr
    
bin_list = []
with open("input.txt") as f:
    for line in f:
        bin_list.append(line.rstrip())
        
cgr = get_rating(False)
ogr = get_rating(True)

print(cgr*ogr)
