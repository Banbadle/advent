dir_map = {"forward": (0,1), "up": (1,-1), "down": (1,1)}

with open("input.txt", "r+") as f:
    total = [0,0]
    for line in f:
        direction, num = line.split()
        ind, mult = dir_map[direction]
        
        total[ind] += int(mult) * int(num)
        
    print(total[0] * total[1])
    
with open("input.txt", "r+") as f:
    aim = 0
    total = [0,0]
    for line in f:
        direction, num = line.split()
        ind, mult = dir_map[direction]
        
        if direction != "forward":
            aim += int(mult) * int(num)
        
        else:
            total[0] += int(mult) * int(num)
            total[1] += aim * int(num)
        
    print(total[0] * total[1])