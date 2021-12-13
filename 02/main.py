with open("input.txt", "r+") as f:
    data = [(direction, int(num))for direction, num in [line.split() for line in f]]

dir_map = {"forward": (0,1), "up": (1,-1), "down": (1,1)}

#Part 1
total = [0,0]
for direction, num in data:
    dir_ind, mult = dir_map[direction]
    total[dir_ind] += mult * num
    
print(total[0] * total[1])
    
#Part 2
aim = 0
depth, distance = (0,0)
for direction, num in data:
    _, mult = dir_map[direction]
    
    if direction != "forward":
        aim += mult * num
    else:
        distance += mult * num
        depth += aim * num
    
print(distance * depth)